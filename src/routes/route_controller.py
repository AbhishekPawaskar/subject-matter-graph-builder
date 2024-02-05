# Routes APIs and its endpoints

from fastapi import APIRouter
from src.endpoints.content_endpoint import process_content, build_graph, update_graph

content_routes = APIRouter()
content_routes.add_api_route("/process-content", process_content, methods=["POST"])

graph_routes = APIRouter()
graph_routes.add_api_route("/build-graph", build_graph, methods=["POST"])
graph_routes.add_api_route("/update-graph", update_graph, methods=["POST"])
