import logging.config

from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware

from app.exceptions import RequestError
from app.errors import on_error
from app.protocol import HttpMethod


class Server(Starlette):
    log = logging.getLogger(__name__)

    def __init__(self, controllers, *args, debug=False, **kwargs):
        logging.config.fileConfig(
            "logging.conf",
            defaults={"level": "DEBUG" if debug else "INFO"},
            disable_existing_loggers=True,
        )

        super(Server, self).__init__(*args, **kwargs)

        # Register controllers with app
        for ctrl_cls in controllers:
            self._controller_register(ctrl_cls)

        # Set up CORS
        self.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        # Event handlers
        self.add_event_handler("startup", self.on_app_start)
        self.add_event_handler("shutdown", self.on_app_stop)

        # Error handlers
        self.add_exception_handler(RequestError, on_error)
        self.add_exception_handler(Exception, on_error)

    def _controller_register(self, ctrl_cls):
        ctrl = ctrl_cls.init(app=self)
        path_base, routes = ctrl.routes_make()

        # Load routes
        for path_rel, method, handler in routes:
            method = HttpMethod(method.upper()).value
            path = path_base + path_rel.rstrip("/")
            self.log.info(f"Adding route: {method} {path} [{handler}]")
            self.add_route(path, handler, [method])

    async def on_app_start(self):
        pass

    async def on_app_stop(self):
        pass
