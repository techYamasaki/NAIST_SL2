import unittest
from speciallecture.GetChunk import GetChunk

class TestGetChunk(unittest.TestCase):

    def test_read1(self):
        getter = GetChunk("tests/sample.txt")
        chunks = getter.get_chunk()
        print(chunks)
        self.assertNotIn('', chunks)

    def test_read2(self):
        with self.assertRaises(FileNotFoundError):
            # tests/sample.csvならAssertionError: FileNotFoundError not raised
            getter = GetChunk("tests/samfgple")
            getter.get_chunk()

if __name__ == "__main__":
    unittest.main()