import json
import os
import sys

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado

class ExampleRouteHandler(APIHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({
            "data": "This is /jupyterlab-scicap-verdant/example endpoint! Verdant test 1!"
        }))


class ScApiUrlRouteHandler(APIHandler):
    """
    Obtain the Science Capsule API URL from the environment variable
    and share with the frontend extension so that it can send requests
    to the sc events API.
    """
    @tornado.web.authenticated
    def get(self):
        if sys.platform == "win32":
            api_url = os.environ["SC_API_URL_WINDOWS"]
        else:
            api_url = os.environ["SC_API_URL"]
        self.finish(json.dumps({
            "data": api_url
        }))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    web_app.add_handlers(host_pattern, [
        (url_path_join(base_url, "jupyterlab-scicap-verdant", "example"), ExampleRouteHandler),
        (url_path_join(base_url, "jupyterlab-scicap-verdant", "sc_api_url"), ScApiUrlRouteHandler)
    ])