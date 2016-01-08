import unittest
from src import LoadFile
class TestInputFile(unittest.TestCase):

    def test_file_load(self):
        test_output = LoadFile.csv("input.csv")
        real_output = {"Id": "0", "File": "CMU-1.svs"}
        self.assertEqual(test_output, real_output)

if __name__ == '__main__':
    unittest.main()
