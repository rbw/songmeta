import uvicorn
from os import environ as env

from .controllers import AlbumController, TrackController
from .server import Server

# Set up config from environment
listen_host, listen_port = env.get("AIOLI_LISTEN", "127.0.0.1:5000").split(":")
pg_username = env.get("AIOLI_PG_USERNAME", "songmeta")
pg_password = env.get("AIOLI_PG_PASSWORD", "songmetasecret")
pg_address = env.get("AIOLI_PG_ADDRESS", "localhost:5432")
pg_database = env.get("AIOLI_PG_DATABASE", "songmeta")
log_config = env.get("AIOLI_LOG_CONFIG", "logging.conf")
log_debug = env.get("AIOLI_LOG_DEBUG", "1") == "1"


def main():
    return Server(
        db_url=f"postgresql+asyncpg://{pg_username}:{pg_password}@{pg_address}/{pg_database}",
        debug=log_debug,
        controllers=[AlbumController, TrackController],
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
