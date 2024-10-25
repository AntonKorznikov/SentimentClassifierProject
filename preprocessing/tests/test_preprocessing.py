import os
import shutil
import unittest

from ..preprocessing import preprocess, INPUT_RAW_DIR, INPUT_DIR

class TestPreprocess(unittest.TestCase):

    def setUp(self):

        os.makedirs(INPUT_RAW_DIR, exist_ok=True)

        with open(os.path.join(INPUT_RAW_DIR, 'test1.txt'), 'w') as f:
            f.write('This is a test file 1.')
        with open(os.path.join(INPUT_RAW_DIR, 'test2.txt'), 'w') as f:
            f.write('This is a test file 2.')
        with open(os.path.join(INPUT_RAW_DIR, 'test3.md'), 'w') as f:
            f.write('This is not a text file.')

    def tearDown(self):

        shutil.rmtree(INPUT_RAW_DIR)
        if os.path.exists(INPUT_DIR):
            shutil.rmtree(INPUT_DIR)

    def test_preprocess_creates_input_dir(self):

        if os.path.exists(INPUT_DIR):
            shutil.rmtree(INPUT_DIR)
        
        preprocess()
        
        self.assertTrue(os.path.exists(INPUT_DIR))

    def test_preprocess_copies_txt_files(self):
        preprocess()
        
        copied_files = os.listdir(INPUT_DIR)
        
        self.assertIn('test1.txt', copied_files)
        self.assertIn('test2.txt', copied_files)
        self.assertNotIn('test3.md', copied_files)

    def test_preprocess_no_txt_files(self):

        for filename in os.listdir(INPUT_RAW_DIR):
            os.remove(os.path.join(INPUT_RAW_DIR, filename))
        
        preprocess()
        
        self.assertEqual(len(os.listdir(INPUT_DIR)), 0)

if __name__ == '__main__':
    unittest.main()
