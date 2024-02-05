from pydantic import BaseModel
from typing import List

class ProcessContentRequest(BaseModel):
   url: str

class ProcessContentResponse(BaseModel):
   nodes: List
   edges: List

class BuildGraphRequest(BaseModel):
   url: str

class BuildGraphResponse(BaseModel):
   nodes: List
   edges: List
   buildStatus:bool

class UpdateGraphRequest(BaseModel):
   entities: List
   relation: List

class UpdateGraphResponse(BaseModel):
   buildStatus: bool

class GraphDataModel(BaseModel):
   entities: List
   relation: List
   
