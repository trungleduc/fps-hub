import logging
import os
import sys
from urllib.parse import urlparse
from fps.config import Config
import typer
from fps_uvicorn.cli import parse_extra_options, store_extra_options
from fps_uvicorn.config import UvicornConfig
from fps.logging import configure_loggers, get_loggers_config
import uvicorn

hub_app = typer.Typer()


@hub_app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def app(
    ctx: typer.Context,
    root_path: str = None,
    reload: bool = typer.Option(
        None,
        help=(
            "Enable/disable automatic reloading of the server when sources are modified"
        ),
    ),
    reload_dirs: str = ".",
    config: str = None,
    workers: int = None,
):
    service_url = os.environ.get("JUPYTERHUB_SERVICE_URL", None)
    port = 8888
    host = "0.0.0.0"
    if service_url:
        url = urlparse(service_url)
        port = url.port
        host = url.hostname

    # Write config file
    
    start(app="fps_hub.main:hub_fps_app")
    # uvicorn.run(
    #     "fps_hub.main:hub_fps_app",
    #     host=host,
    #     port=port,
    #     workers=workers,
    #     log_config=get_loggers_config(),
    #     reload=reload,
    #     reload_dirs=reload_dirs,
    # )
