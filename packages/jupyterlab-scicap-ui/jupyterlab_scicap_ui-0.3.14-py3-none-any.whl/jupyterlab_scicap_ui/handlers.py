import json
import os

from jupyter_server.base.handlers import APIHandler
from jupyter_server.utils import url_path_join
import tornado


class ScApiUrlRouteHandler(APIHandler):
    """
    Obtain the Science Capsule API URL(s) from the environment variable
    and share with the frontend extension so that it can send requests
    to the sc events API.

    The Science Capsule API runs on different ports for windows and non-windows machines,
    therefore there are two separate environment variables.
    The client detects whether it is a windows or non-windows machine.
    """
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps({
            "data": {
                "apiUrl": os.environ.get("SC_API_URL", None),
                "apiUrlWindows": os.environ.get("SC_API_URL_WINDOWS", None)
            }
        }))


def setup_handlers(web_app):
    host_pattern = ".*$"

    base_url = web_app.settings["base_url"]
    web_app.add_handlers(host_pattern, [
        (url_path_join(base_url, "@codytodonnell/jupyterlab-scicap-ui", "sc_api_url"), ScApiUrlRouteHandler)
    ])