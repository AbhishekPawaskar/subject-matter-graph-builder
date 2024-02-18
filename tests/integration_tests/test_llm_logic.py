import json
import unittest

class TestLlmLogic(unittest.TestCase):
    def setUp(self):
        
        with open('/app/tests/data/web_content_data.json') as f:
            self.input_data = json.load(f)
    
    def test_get_graph_raw_data(self):
        from src.service.llm_logic import get_graph_raw_data
        result = get_graph_raw_data(website_content=self.input_data["data"])
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()