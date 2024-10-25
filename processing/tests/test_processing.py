# test_processing.py

import unittest
import os
import shutil
import json
from processing import process

class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.input = 'examples/test_input'
        self.output_raw = 'examples/test_output_raw'
        os.makedirs(self.input, exist_ok=True)
        with open(os.path.join(self.input, 'test.txt'), 'w') as f:
            f.write("I love this product!")
    
    def tearDown(self):
        shutil.rmtree(self.input)
        shutil.rmtree(self.output_raw)
    
    def test_process(self):
        process()
        self.assertTrue(os.path.exists(self.output_raw))
        self.assertTrue(os.path.isfile(os.path.join(self.output_raw, 'test.txt.json')))
        with open(os.path.join(self.output_raw, 'test.txt.json'), 'r') as f:
            result = json.load(f)
        self.assertIn('label', result)
        self.assertIn('score', result)

if __name__ == '__main__':
    unittest.main()