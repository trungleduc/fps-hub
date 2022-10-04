import os
from urllib.parse import urlparse

import typer
from fps_uvicorn.cli import start

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
    open_browser: bool = typer.Option(
        None,
        help=("Enable/disable automatic automatic opening of the browser"),
    ),
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

    start(
        ctx,
        port=port,
        host=host,
        root_path=root_path,
        reload=reload,
        reload_dirs=reload_dirs,
        open_browser=open_browser,
        config=config,
        workers=workers,
    )
