from werkzeug.wrappers import Request, Response
from .main import has_ip_access, get_html
from functools import wraps
from flask import make_response, jsonify, render_template, request
from python_settings import settings 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent

def get_request_ip():
    x_forwarded_for = request.headers.getlist("X-Forwarded-For")
    print("x_forwarded_for",x_forwarded_for)
    if x_forwarded_for:
        # The header can contain multiple IP addresses; the first one is usually the client's IP
        client_ip = x_forwarded_for[0]
        client_ip = client_ip.split(",")[0]
    else:
        # If the header is not present, get the IP from the remote address
        client_ip = request.remote_addr
    return client_ip
    
class ProtechRemoteMiddleware:

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request_obj = Request(environ)
        ip_address = request_obj.remote_addr
        print(f"The client IP is: {ip_address}")
        if not has_ip_access(ip_address):
            # TODO: response type ( html or json)
            if settings.RENDER_HTML_PAGE:
                res = Response(get_html(), mimetype='text/html', status=401)
            else:
                res = Response(settings.RESTRICTED_MESSAGE, mimetype='text/plain', status=401)
            return res(environ, start_response)
        return self.app(environ, start_response)
    

def pr_access():
    def _pr_access(f):
        @wraps(f)
        def __pr_access(*args, **kwargs):
            # just do here everything what you need
            ip_address = get_request_ip()
            print(f"The client IP is: {ip_address}")
            if not has_ip_access(ip_address):
                if settings.RENDER_HTML_PAGE:
                    return make_response(get_html(), 401)
                else:
                    return make_response(settings.RESTRICTED_MESSAGE, 401)
            result = f(*args, **kwargs)
            return result
        return __pr_access
    return _pr_access