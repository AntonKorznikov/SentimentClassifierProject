# test_postprocessing.py

import os
import json
import unittest
from ..postprocessing import postprocess, OUTPUT_RAW_DIR, OUTPUT_DIR

class TestPostprocessFunction(unittest.TestCase):

    def setUp(self):

        os.makedirs(OUTPUT_RAW_DIR, exist_ok=True)
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        sample_data = [
            {"label": "POSITIVE", "score": 0.99},
            {"label": "NEGATIVE", "score": 0.01}
        ]
        with open(os.path.join(OUTPUT_RAW_DIR, 'test1.json'), 'w') as f:
            json.dump(sample_data, f)

    def tearDown(self):

        if os.path.exists(OUTPUT_RAW_DIR):
            for filename in os.listdir(OUTPUT_RAW_DIR):
                os.remove(os.path.join(OUTPUT_RAW_DIR, filename))
            os.rmdir(OUTPUT_RAW_DIR)

        if os.path.exists(OUTPUT_DIR):
            for filename in os.listdir(OUTPUT_DIR):
                os.remove(os.path.join(OUTPUT_DIR, filename))
            os.rmdir(OUTPUT_DIR)

    def test_postprocess(self):

        postprocess()


        output_file_path = os.path.join(OUTPUT_DIR, 'test1.txt')
        self.assertTrue(os.path.exists(output_file_path))


        expected_output_content = "Sentiment: POSITIVE, Score: 0.99\nSentiment: NEGATIVE, Score: 0.01\n"
        
        with open(output_file_path, 'r') as out_file:
            actual_output_content = out_file.read()

        self.assertEqual(actual_output_content, expected_output_content)

if __name__ == '__main__':
    unittest.main()
