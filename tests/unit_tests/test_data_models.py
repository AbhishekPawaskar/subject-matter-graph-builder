import json
import pytest
from src.datamodels.models import ProcessContentRequest, ProcessContentResponse, GraphDataModel, BuildGraphRequest, BuildGraphResponse, UpdateGraphRequest, UpdateGraphResponse

@pytest.fixture
def data_feeder():
    with open('/app/tests/data/unit_test.json') as f:
        data = json.load(f)
    return data

def test_ProcessContentRequest_model(data_feeder):
    test_data = data_feeder["ProcessContentRequest"]
    model = ProcessContentRequest(**test_data)
    assert model.url == test_data["url"]

def test_ProcessContentResponse_model(data_feeder):
    test_data = data_feeder["ProcessContentResponse"]
    model = ProcessContentResponse(**test_data)
    assert model.nodes == test_data["nodes"]
    assert model.edges == test_data["edges"]

def test_BuildGraphRequest_model(data_feeder):
    test_data = data_feeder["BuildGraphRequest"]
    model = BuildGraphRequest(**test_data)
    assert model.url == test_data["url"]

def test_BuildGraphResponse_model(data_feeder):
    test_data = data_feeder["BuildGraphResponse"]
    model = BuildGraphResponse(**test_data)
    assert model.nodes == test_data["nodes"]
    assert model.edges == test_data["edges"]
    assert model.buildStatus == test_data["buildStatus"]

def test_GraphDataModel_model(data_feeder):
    test_data = data_feeder["GraphDataModel"]
    model = GraphDataModel(**test_data)
    assert model.entities == test_data["entities"]
    assert model.relation == test_data["relation"]

def test_UpdateGraphRequest_model(data_feeder):
    test_data = data_feeder["UpdateGraphRequest"]
    model = UpdateGraphRequest(**test_data)
    assert model.entities == test_data["entities"]
    assert model.relation == test_data["relation"]

def test_UpdateGraphResponse_model(data_feeder):
    test_data = data_feeder["UpdateGraphResponse"]
    model = UpdateGraphResponse(**test_data)
    assert model.buildStatus == test_data["buildStatus"]
    
    