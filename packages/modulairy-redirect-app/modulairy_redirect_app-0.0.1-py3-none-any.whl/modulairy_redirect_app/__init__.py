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
    
    print(json.dumps(redirect_map,indent=4))

    @app.route('/')
    def redirect_url():
        # Get the incoming host information
        request_host = request.host.lower().strip()
        if key in redirect_map:
            parsed_url = urlparse(request.url)
            new_parsed_url = parsed_url._replace(netloc=redirect_map[request_host])
            new_url = urlunparse(new_parsed_url)
            return redirect(new_url, code=301)
        else:
            abort(403)

    return app