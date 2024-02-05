from fastapi import FastAPI
from starlette.routing import Mount

#only for debugging
# import debugpy
# debugpy.listen(("0.0.0.0", 5678))

from src.routes.route_controller import content_routes, graph_routes

app = FastAPI()
app.mount("/content", content_routes)
app.mount("/graph", graph_routes)