import os
from fastapi import FastAPI, Request
from fps.main import app


ROOT_PATH = os.environ.get("JUPYTERHUB_SERVICE_PREFIX", None)
ACTIVITY_URL = os.environ.get("JUPYTERHUB_ACTIVITY_URL", None)
if ROOT_PATH:
    hub_fps_app = FastAPI()
    hub_fps_app.mount(ROOT_PATH.rstrip('/'), app)
    
    if ACTIVITY_URL:
        @hub_fps_app.middleware("http")
        async def add_process_time_header(request: Request, call_next):
            ''' Report activities back to JupyterHub
            '''
            response = await call_next(request)
            return response
else:
    hub_fps_app = app
