import os
from src.datamodels.models import (
   ProcessContentRequest,
   ProcessContentResponse,
   BuildGraphRequest,
   BuildGraphResponse
)
from src.utils.content_extractor import get_website_content
from src.utils.llm_logic import get_graph_raw_data, process_result
from src.utils.graph_ops import GraphOps

graph_operator = GraphOps()

def process_content(request_body:ProcessContentRequest):
    web_content = get_website_content(url=request_body.url)
    llm_output = get_graph_raw_data(website_content=web_content)
    graph_data = process_result(llm_result=llm_output)
    return ProcessContentResponse(nodes=graph_data['entities'],edges=graph_data['relation'])

def build_graph(request_body:BuildGraphRequest):
    web_content = get_website_content(url=request_body.url)
    llm_output = get_graph_raw_data(website_content=web_content)
    graph_data = process_result(llm_result=llm_output)
    build_status = graph_operator.full_upload(graph_data_dict=graph_data)
    return BuildGraphResponse(nodes=graph_data['entities'], edges=graph_data['relation'], buildStatus=build_status)