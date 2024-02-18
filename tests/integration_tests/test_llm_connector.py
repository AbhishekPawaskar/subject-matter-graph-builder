import unittest
from openai import OpenAI

class TestLlmConnector(unittest.TestCase):

    def setUp(self):
        from src.connector.openai_connector import OpenAIConnection
        self.client = OpenAIConnection().client

    def test_graphdb_connection(self):
        self.assertIsInstance(self.client, OpenAI)
        self.assertFalse(self.client.is_closed())
    
    def tearDown(self):
        self.client.close()


if __name__ == '__main__':
    unittest.main()
