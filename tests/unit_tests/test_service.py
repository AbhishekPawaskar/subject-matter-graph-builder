import json
import pytest
from unittest.mock import Mock, patch, call
from src.datamodels.models import GraphDataModel
from src.service.content_extractor import get_website_content
from src.service.graph_ops import GraphOps
from src.utility.utilities import process_result

@pytest.fixture
def web_data_feeder():
    with open('/app/tests/data/web_content_data.json') as f:
        data = json.load(f)
    return data


def test_get_website_content_util(web_data_feeder):
    web_content = web_data_feeder["data"]
    url = web_data_feeder["url"]
    test_content = get_website_content(url=url)
    assert web_content == test_content

@patch("src.service.graph_ops.GraphDBConnection")
def test_upload_nodes(mock_graph_db_connection):
    mock_session = Mock()
    mock_session.execute_query.return_value = ([], "Mocked summary", "Mocked keys")
    mock_graph_db_connection.return_value.get_driver.return_value.__enter__.return_value = mock_session
    graph_ops = GraphOps()
    result = graph_ops.upload_nodes(name="TestNode")
    mock_session.verify_connectivity.assert_called_once()
    mock_session.execute_query.assert_called_once_with(
        "CREATE (n:Node {name: $name}) RETURN n;",
        name="TestNode",
        database_="memgraph",
    )
    assert result is True

@patch("src.service.graph_ops.GraphDBConnection")
def test_upload_edges(mock_graph_db_connection):
    mock_session = Mock()
    mock_session.execute_query.return_value = ([], "Mocked summary", "Mocked keys")
    mock_graph_db_connection.return_value.get_driver.return_value.__enter__.return_value = mock_session
    graph_ops = GraphOps()
    result = graph_ops.upload_edges(fromEntity="Node1", toEntity="Node2", relation="REL")
    mock_session.verify_connectivity.assert_called_once()
    mock_session.execute_query.assert_called_once_with(
        "MATCH (f:Node {name:'Node1'}), (t:Node {name:'Node2'}) CREATE (f)-[r:REL]->(t) RETURN f,r,t;",
        database_="memgraph",
    )
    assert result is True


@patch("src.service.graph_ops.GraphDBConnection")
def test_nodes_exists(mock_graph_db_connection):
    mock_session = Mock()
    mock_session.execute_query.return_value = ([], Mock(), Mock())
    mock_graph_db_connection.return_value.get_driver.return_value.__enter__.return_value = mock_session
    graph_ops = GraphOps()
    result = graph_ops.nodes_exists(name="TestNode")
    mock_session.verify_connectivity.assert_called_once()
    mock_session.execute_query.assert_called_once_with(
        "MATCH (n:Node {name: $name}) RETURN n;",
        name="TestNode",
        database_="memgraph",
    )
    assert result is False


@patch("src.service.graph_ops.GraphDBConnection")
def test_full_upload(mock_graph_db_connection):
    mock_session = Mock()
    mock_graph_data_model = Mock(spec=GraphDataModel)
    mock_graph_data_model.relation = [{"fromEntity": "NODE1", "toEntity": "NODE2", "relationship": "REL"}]
    mock_graph_db_connection.return_value.get_driver.return_value.__enter__.return_value = mock_session
    graph_ops = GraphOps()
    graph_ops.nodes_exists = Mock(side_effect=[False, False])
    graph_ops.upload_nodes = Mock(return_value=True)
    graph_ops.upload_edges = Mock(return_value=True)
    result = graph_ops.full_upload(graph_data_dict=mock_graph_data_model)
    graph_ops.upload_nodes.assert_has_calls([call("NODE1"),call("NODE2"),], any_order=False)
    graph_ops.upload_edges.assert_called_once_with(fromEntity="NODE1", toEntity="NODE2", relation="REL")
    assert result is True


@pytest.fixture
def llm_output_data_feeder():
    with open('/app/tests/data/llm_output_data.json') as f:
        data = json.load(f)
    return data

def test_process_result(llm_output_data_feeder):
    test_data = llm_output_data_feeder["data"]
    test_result = llm_output_data_feeder["result"]

    result = process_result(llm_result=test_data)
    assert test_result == result


