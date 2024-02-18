import unittest

class TestGraphOps(unittest.TestCase):
    def setUp(self):
        from src.service.graph_ops import GraphOps
        from src.datamodels.models import GraphDataModel
        self.graph_operator = GraphOps()
        self.full_upload_data = GraphDataModel(entities=[], 
                                               relation=[{"fromEntity":"FROMENTITY", 
                                                          "toEntity":"TOENTITY", 
                                                          "relationship":"RELATION"}])
    
    def test_node_exist(self):
        self.assertFalse(self.graph_operator.nodes_exists(name="testNodeExists"))

    def test_upload_node(self):
        self.assertTrue(self.graph_operator.upload_nodes(name="testUploadNode"))

    def test_upload_edge(self):
        self.assertTrue(self.graph_operator.upload_nodes(name="testFromNode"))
        self.assertTrue(self.graph_operator.upload_nodes(name="testToNode"))
        self.assertTrue(self.graph_operator.upload_edges(fromEntity="testFromNode",toEntity="testToNode", relation="testUploadEdgeRel"))

    def test_node_exist(self):
        self.assertTrue(self.graph_operator.full_upload(graph_data_dict=self.full_upload_data))

    def tearDown(self):
        self.graph_operator.driver_connection.close()

if __name__ == '__main__':
    unittest.main()