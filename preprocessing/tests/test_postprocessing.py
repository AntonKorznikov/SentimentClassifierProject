# test_postprocessing.py

import unittest
import os
import shutil
import json
from postprocessing import postprocess

class TestPostprocessing(unittest.TestCase):
    def setUp(self):
        self.output_raw = 'examples/test_output_raw'
        self.output = 'examples/test_output'
        os.makedirs(self.output_raw, exist_ok=True)
        sample_data = {'label': 'POSITIVE', 'score': 0.99}
        with open(os.path.join(self.output_raw, 'test.json'), 'w') as f:
            json.dump(sample_data, f)
    
    def tearDown(self):
        shutil.rmtree(self.output_raw)
        if os.path.exists(self.output):
            shutil.rmtree(self.output)
    
    def test_postprocess(self):
        postprocess()
        self.assertTrue(os.path.exists(self.output))
        self.assertTrue(os.path.isfile(os.path.join(self.output, 'test.txt')))
        with open(os.path.join(self.output, 'test.txt'), 'r') as f:
            content = f.read()
        self.assertIn('POSITIVE', content)
        self.assertIn('0.99', content)

if __name__ == '__main__':
    unittest.main()