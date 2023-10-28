from flask import Flask, abort, request, redirect
from urllib.parse import urlparse, urlunparse
import json
import os

def redirect_app_init():
    print("starting...")
    app = Flask(__name__)

    # Extract TARGET_ prefixed environment variables and create a mapping
    redirect_map = {}
    for key, value in os.environ.items():
        if key.startswith("TARGET_"):
            target_sites = value.split(';')
            for site in target_sites:
                value = key.replace("TARGET_","").replace("_",".").lower();
                redirect_map[site.strip().lower()] = value
    

    @app.route('/', defaults={'path': None})
    @app.route('/<path:path>')
    def redirect_url(path):
        parsed_url = urlparse(request.url)
        if parsed_url.hostname in redirect_map:
            netloc=""
            if(parsed_url.port):
                netloc="{}:{}".format(redirect_map[parsed_url.hostname],parsed_url.port)
            else:
                netloc=redirect_map[parsed_url.hostname]
            new_parsed_url = parsed_url._replace(netloc = netloc)
            new_url = urlunparse(new_parsed_url)
            return redirect(new_url, code=301)
        else:
            abort(404)

    return app