import unittest
from neo4j import GraphDatabase

class TestGraphDBConnection(unittest.TestCase):

    def setUp(self):
        from src.connector.graph_db_connector import GraphDBConnection
        self.driver = GraphDBConnection().get_driver()
        
    def test_graphdb_connection(self):
        
        self.assertIsInstance(self.driver, GraphDatabase.driver)
        with self.driver as session:
            session.verify_connectivity()
            records, summary, keys = session.execute_query("MATCH (n:Node {name: $name}) RETURN n;",
                                                           name="test",
                                                           database_="memgraph",)
            self.assertEquals(first=len(records), second=0)
    
    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
