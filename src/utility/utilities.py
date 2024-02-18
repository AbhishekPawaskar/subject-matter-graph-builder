import json
import pydantic

from src.datamodels.models import GraphDataModel

def process_result(llm_result:str):
    
    try:
        processed_string_result = llm_result[llm_result.find('{'):llm_result.rfind('}') + 1]
        graph_data = json.loads(processed_string_result)
        graph_result = GraphDataModel(**graph_data)
        return graph_result
    except pydantic.ValidationError as e:
        return GraphDataModel(entities=[],relation=[])