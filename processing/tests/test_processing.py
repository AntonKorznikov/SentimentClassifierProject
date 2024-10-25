# test_processing.py

import os
import json
import unittest
from transformers import pipeline  # Ensure transformers is installed
from ..processing import process, INPUT_DIR, OUTPUT_RAW_DIR

class TestProcessFunction(unittest.TestCase):

    def setUp(self):
        # Create input and output directories
        os.makedirs(INPUT_DIR, exist_ok=True)
        os.makedirs(OUTPUT_RAW_DIR, exist_ok=True)

        # Create a sample input text file
        with open(os.path.join(INPUT_DIR, 'test1.txt'), 'w') as f:
            f.write("This is a test sentence.\nAnother sentence.\n")

    def tearDown(self):
        # Clean up created directories and files after tests
        if os.path.exists(INPUT_DIR):
            for filename in os.listdir(INPUT_DIR):
                os.remove(os.path.join(INPUT_DIR, filename))
            os.rmdir(INPUT_DIR)

        if os.path.exists(OUTPUT_RAW_DIR):
            for filename in os.listdir(OUTPUT_RAW_DIR):
                os.remove(os.path.join(OUTPUT_RAW_DIR, filename))
            os.rmdir(OUTPUT_RAW_DIR)

    def test_process(self):
        # Call the process function
        process()

        # Check that the output file was created
        output_file_path = os.path.join(OUTPUT_RAW_DIR, 'test1.json')
        self.assertTrue(os.path.exists(output_file_path))

        # Check that the content of the output file is as expected
        with open(output_file_path, 'r') as out_file:
            actual_output = json.load(out_file)

        # Validate the structure of results (assuming model returns positive sentiment)
        expected_output = [
            {'label': 'POSITIVE', 'score': 0.9810278415679932},  # Example result for first sentence
            {'label': 'POSITIVE', 'score': 0.9927107095718384}   # Example result for second sentence
        ]

        # Note: The actual scores may vary depending on the model's predictions.
        # You might want to adjust expected values based on your model's behavior.
        
        self.assertEqual(len(actual_output), len(expected_output))
        
        for i in range(len(expected_output)):
            self.assertIn('label', actual_output[i])
            self.assertIn('score', actual_output[i])
            self.assertAlmostEqual(actual_output[i]['score'], expected_output[i]['score'], places=2)  # Check scores with some tolerance

if __name__ == '__main__':
    unittest.main()
