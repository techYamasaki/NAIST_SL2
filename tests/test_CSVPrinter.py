import unittest

from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):

    def test_read1(self):
        printer = CSVPrinter("tests/sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

    def test_read2(self):
        printer = CSVPrinter("tests/sample.csv")
        line = printer.read()
        self.assertEqual("bbb2", line[1][1])
    
    def test_read3_2(self):
        try:
            printer = CSVPrinter("tests/sample.csv")
            printer.read()
            unittest.TestCase.fail("This line should not be invoked")
        except FileNotFoundError as e:
            print(e)

    def test_read3(self):
        with self.assertRaises(FileNotFoundError):
            # tests/sample.csvならAssertionError: FileNotFoundError not raised
            printer = CSVPrinter("tests/samfgple")
            printer.read()

            

if __name__ == "__main__":
    unittest.main()