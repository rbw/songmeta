import uvicorn
from os import environ as env

from .server import Server

# Set up config from environment
listen_host, listen_port = env.get("AIOLI_LISTEN_ADDR", "127.0.0.1:5000").split(":")
log_config = env.get("AIOLI_LOG_CONFIG", "logging.conf")
log_debug = env.get("AIOLI_LOG_DEBUG", "1") == "1"


def main():
    return Server(
        debug=log_debug,
        controllers=[],
    )


if __name__ == "__main__":
    uvicorn.run(
        f"{__name__}:main",
        factory=True,
        log_config=log_config,
        host=listen_host,
        port=int(listen_port),
        log_level="debug" if log_debug else "info",
    )
