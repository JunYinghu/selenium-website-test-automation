import csv


class CSVWriter(object):
    def __init__(self, filename, columns):
        self.outfile = open(filename, 'wb')
        self.writer = csv.writer(self.outfile, dialect='excel')
        self.writer.writerow(columns)

    def write(self, *values):
        self.writer.writerow(values)

    def close(self):
        self.outfile.close()
