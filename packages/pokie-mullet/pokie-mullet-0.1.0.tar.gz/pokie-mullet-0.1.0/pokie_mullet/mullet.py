"""
Mullet - a quick'n dirty proxy for SPA applications

Mullet is a development http proxy that will mount a flask or pokie application on a specified prefix and either proxy
root requests to another http server or serve them from local storage.

The purpose is to aid development of single-page applications with backends written in python, allowing to mount
the backend on a specific route, and serve the frontend either from a node development server or from disk.

"""
import argparse
import importlib
import mimetypes
import os
import sys
from datetime import timezone, datetime
from pathlib import Path
from time import time
from urllib.parse import urlsplit
from zlib import adler32

from werkzeug.exceptions import NotFound
from werkzeug.http import http_date, is_resource_modified
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.middleware.http_proxy import ProxyMiddleware
from werkzeug.serving import run_simple
from werkzeug.utils import get_content_type
from werkzeug.wsgi import get_path_info, wrap_file


def is_valid_url(url):
    parts = urlsplit(url)
    return parts.scheme in ("http", "https")


def error(msg, code=-1):
    print(msg, file=sys.stderr)
    exit(code)


class RootProxy(ProxyMiddleware):
    def __init__(
        self,
        app: "WSGIApplication",
        target,
        chunk_size: int = 2 << 13,
        timeout: int = 10,
        remove_prefix: bool = False,
        host: str = "<auto>",
        headers: dict = None,
        ssl_context=None,
    ) -> None:
        super().__init__(app, {}, chunk_size, timeout)
        self.opts = {
            "target": target,
            "remove_prefix": remove_prefix,
            "host": host,
            "headers": {} if not headers else headers,
            "ssl_context": ssl_context,
        }

    def __call__(self, environ: "WSGIEnvironment", start_response: "StartResponse"):
        path = environ["PATH_INFO"]
        app = self.proxy_to(self.opts, path, "")
        return app(environ, start_response)


class StaticMiddleware:
    def __init__(
        self,
        app: "WSGIApplication",
        root_path: str,
        index: str = "index.html",
        cache: bool = True,
        cache_timeout: int = 60 * 60 * 12,
        fallback_mimetype: str = "application/octet-stream",
    ) -> None:
        self.app = app
        self.cache = cache
        self.cache_timeout = cache_timeout
        self.root_path = Path(root_path)
        self.index = index
        self.fallback_mimetype = fallback_mimetype

    def generate_etag(self, mtime: datetime, file_size: int, real_filename: str) -> str:
        real_filename = os.fsencode(real_filename)
        timestamp = mtime.timestamp()
        checksum = adler32(real_filename) & 0xFFFFFFFF
        return f"wzsdm-{timestamp}-{file_size}-{checksum}"

    def __call__(self, environ: "WSGIEnvironment", start_response: "StartResponse"):
        path = get_path_info(environ)
        path = path.lstrip("/")
        if len(path) == 0:
            path = self.index
        try_path = self.root_path / Path(path)

        # if actual path outside root path, error
        if not try_path.absolute().is_relative_to(self.root_path):
            return self.app(environ, start_response)

        # if no path exists or if it is just a folder, route to index.html
        if not try_path.exists() or try_path.is_dir():
            try_path = self.root_path / Path(self.index)

        # by now, it is either an existing file or index.html
        if not try_path.is_file():
            return self.app(environ, start_response)

        guessed_type = mimetypes.guess_type(try_path.name)
        mime_type = get_content_type(guessed_type[0] or self.fallback_mimetype, "utf-8")
        f = open(try_path, "rb")
        mtime = datetime.fromtimestamp(os.path.getmtime(try_path), tz=timezone.utc)
        file_size = int(os.path.getsize(try_path))

        headers = [("Date", http_date())]

        if self.cache:
            timeout = self.cache_timeout
            etag = self.generate_etag(mtime, file_size, try_path.name)  # type: ignore
            headers += [
                ("Etag", f'"{etag}"'),
                ("Cache-Control", f"max-age={timeout}, public"),
            ]

            if not is_resource_modified(environ, etag, last_modified=mtime):
                f.close()
                start_response("304 Not Modified", headers)
                return []

            headers.append(("Expires", http_date(time() + timeout)))
        else:
            headers.append(("Cache-Control", "public"))

        headers.extend(
            (
                ("Content-Type", mime_type),
                ("Content-Length", str(file_size)),
                ("Last-Modified", http_date(mtime)),
            )
        )
        start_response("200 OK", headers)
        return wrap_file(environ, f)


def frontend_factory(path, index_file, parent=NotFound()):
    if is_valid_url(path):
        return RootProxy(parent, path)

    folder = Path(path)
    if not folder.exists():
        error("Invalid frontend path or url '{}'".format(path))

    if not folder.is_dir():
        error("Specified frontend path '{}' is not a directory".format(path))

    result = StaticMiddleware(parent, folder.absolute(), index_file)
    if index_file:
        result.default_index = index_file
    return result


def create_app(flask_app, api_slug, frontend, index_file):
    frontend_app = frontend_factory(frontend, index_file)
    app = DispatcherMiddleware(
        frontend_app,
        {
            api_slug: flask_app,
        },
    )
    return app


def load_api_app(application: str):
    parts = application.split(":", 1)
    if len(parts) > 2 or len(parts) == 0:
        error("Invalid WSGI application format")
    if len(parts) == 1:
        var = "app"
        module = parts[0]
    else:
        module, var = parts[0], parts[1]

    try:
        api_module = importlib.import_module(module)
    except ModuleNotFoundError:
        if module.endswith(".py") and os.path.exists(module):
            error(
                "Application '{}' not found, did you mean '{}:{}'?".format(
                    module, module.rsplit(".", 1)[0], var
                )
            )
        error("Application '{}' not found".format(module))

    api_app = getattr(api_module, var, None)
    if not api_app:
        error("invalid application variable '{}'".format(var))

    return api_app


def run():
    # add running folder to import path
    sys.path.insert(0, ".")

    parser = argparse.ArgumentParser(
        description="mullet - quick'n dirty SPA proxy", add_help=False
    )
    parser.add_argument(
        "--help",
        help="Show usage arguments",
        required=False,
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-a",
        "--application",
        help="WSGI Application",
        required=False,
        default="main:app",
    )

    parser.add_argument(
        "-fe",
        "--frontend",
        help="frontend url or path (default: http://127.0.0.1:3000)",
        required=False,
        default="http://127.0.0.1:3000",
    )

    parser.add_argument(
        "-s", "--slug", help="api slug (default: /api)", required=False, default="/api"
    )

    parser.add_argument(
        "-i",
        "--index",
        help="index file for static serving (default: index.html)",
        required=False,
        default="index.html",
    )

    parser.add_argument(
        "-h",
        "--host",
        help="Host/IP to bind to (default: 127.0.0.1)",
        required=False,
        default="127.0.0.1",
    )

    parser.add_argument(
        "-p",
        "--port",
        help="The base port to bind to (default: 5000)",
        required=False,
        type=int,
        default=5000,
    )

    parser.add_argument(
        "-nd",
        "--no-debug",
        help="Disable debug mode",
        required=False,
        action="store_true",
        default=False,
    )

    parser.add_argument(
        "-nr",
        "--no-reload",
        help="Disable automatic reload",
        required=False,
        action="store_true",
        default=False,
    )

    args = parser.parse_args()
    if args.help:
        parser.print_help()
        exit(0)

    # get api flask app
    api_app = load_api_app(args.application)

    # build mullet app
    mullet_app = create_app(api_app, args.slug, args.frontend, args.index)

    debugger = not args.no_debug
    reloader = not args.no_reload
    run_simple(
        args.host, args.port, mullet_app, use_debugger=debugger, use_reloader=reloader
    )
