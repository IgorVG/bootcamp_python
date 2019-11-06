#!/usr/bin/env python


class CsvReader():
    def __init__(self, file_name, sep=',', header=False, skip_top=0,
                 skip_bottom=0):
        self.file = open(file_name, 'r')
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom
        self.data = []
        self.table = []
        self.error = self.parse()

    def parse(self):
        self.data = [line for line in self.file]
        row_count = len(self.data)
        col_count = len(self.data[0].split(self.sep))
        if self.header:
            self.table[0] = [self.data[0]]
            self.data.pop(0)
        self.data = self.data[self.skip_top:]
        skip_bott = row_count - self.skip_bottom
        for i, l in enumerate(self.data):
            line = [e.strip()
                    for e in filter(lambda x: x != '\n', l.split(self.sep))]
            if len(line) != col_count:
                return True
            self.table.append(line)
            if i == skip_bott:
                break
        return False

    def getdata(self):
        return self.table

    def getheader(self):
        if self.header:
            return self.table[0]

    def __enter__(self):
        if self.error:
            return None
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()


if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        header = file.getheader()
        print(str(data[2]))
        print(len(data[2]))
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")

# if __name__ == "__main__":
#     import sys
#     args = sys.argv
#     args.pop(0)
#     if not len(args):
#         exit(0)
#     with Loadjson(args[0]) as file:
#         if file is None:
#             print("File is corrupted")
#         else:
#             data = file.getdata()
#             print(data)
#             header = file.getheader()
#             print(header)
