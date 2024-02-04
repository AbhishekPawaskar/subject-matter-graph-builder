from pydantic import BaseModel
from typing import List, String, Bool

class ProcessContentRequest(BaseModel):
   url:String

class ProcessContentResponse(BaseModel):
   nodes: List
   edges: List

class BuildGraphRequest(BaseModel):
   url:String

class BuildGraphResponse(BaseModel):
   nodes: List
   edges: List
   buildStatus:Bool

class GraphDataModel(BaseModel):
   entities:List
   relation:List
   
