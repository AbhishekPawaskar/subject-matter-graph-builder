from fastapi import FastAPI
from starlette.routing import Mount

#only for debugging
# import debugpy
# debugpy.listen(("0.0.0.0", 5678))

from routes.route_controller import chat_routes

app = FastAPI()
app.mount("/content", chat_routes)
