import json
import pytest
import requests
from fastapi.testclient import TestClient
from main import app

from src.datamodels.models import ProcessContentRequest, ProcessContentResponse, BuildGraphRequest, BuildGraphResponse, UpdateGraphRequest, UpdateGraphResponse

@pytest.fixture(scope="module")
def test_app():
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def data_feeder():
    with open('/app/tests/data/integration_test_data.json') as f:
        data = json.load(f)
    return data

def test_process_content_endpoint(test_app, data_feeder):
    data = data_feeder["request"]["process-content"]
    request_body = ProcessContentRequest(**data)
    response = test_app.post("/content/process-content", data=request_body.json())
    assert response.status_code == 200
    assert sorted(list(response.json().keys())) == sorted(ProcessContentResponse.schema()["required"])

def test_build_graph_endpoint(test_app, data_feeder):
    data = data_feeder["request"]["build-graph"]
    request_body = BuildGraphRequest(**data)
    response = test_app.post("/graph/build-graph", data=request_body.json())
    print(request_body.json())
    assert response.status_code == 200
    assert sorted(list(response.json().keys())) == sorted(BuildGraphResponse.schema()["required"])
    assert response.json()['buildStatus'] == True

def test_update_graph_endpoint(test_app, data_feeder):
    data = data_feeder["request"]["update-graph"]
    request_body = UpdateGraphRequest(**data)
    response = test_app.post("/graph/update-graph", data=request_body.json())
    print(response.json())
    assert response.status_code == 200
    assert sorted(list(response.json().keys())) == sorted(UpdateGraphResponse.schema()["required"])
    assert response.json()['buildStatus'] == True