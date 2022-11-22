import csv

class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        # a = 1/0
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        return lines