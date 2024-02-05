import json
import pydantic

from src.datamodels.models import GraphDataModel
from src.connector.openai_connector import OpenAIConnection

# Instructions to assistant to prvent going out of context. Internal Guardrail.
internal_instructions="""your task is to go through the user input content understand it and gives entities & relationships required for building the knowledge graph. Strictly follow the structure of the result as per following example as the result will be programmatically be parsed: \n\n\n{\n'entities':['entity1','entity2','entity3'],\n'relation':[\n{'fromEntity':'entity1','toEntity':'entity2','relationship':'is dependent on'},\n{'fromEntity':'entity2','toEntity':'entity3','relationship':'connected to'}\n]\n}"""

client = OpenAIConnection().client

def get_graph_raw_data(website_content:str):
    result = client.chat.completions.create(model="gpt-4-1106-preview",
                                            messages=[{"role": "system", "content": internal_instructions},
                                                      {"role": "user", "content": website_content}])
    return result

def process_result(llm_result:str):
    result = llm_result.choices[0].message.content
    processed_string_result = result[result.find('{'):result.rfind('}') + 1]
    graph_data = json.loads(processed_string_result)
    try:
        graph_result = GraphDataModel(**graph_data)
        return graph_result
    except pydantic.ValidationError as e:
        return GraphDataModel(entities=[],relation=[])
