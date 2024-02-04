# Routes APIs and its endpoints

from fastapi import APIRouter
from endpoints.content_endpoint import process_content, build_graph

chat_routes = APIRouter()

chat_routes.add_api_route("/process-content", process_content, methods=["POST"])
chat_routes.add_api_route("/build-graph", build_graph, methods=["POST"])
