import csv
import sys
import os

import collections

csv_file = ""
filter_set_file = ""

all_files = []
file_set = None
counter = None

def find_duplicates():
    with open(csv_file, "rU") as file:
        with open("filter_set.txt", "wb") as output:
            reader = csv.reader(file)
            reader.next()
            for row in reader:
                all_files.append(row[0])
            file_set = set(all_files)
            for element in file_set:
                output.write(element + "\n")

def count_all_files():
    counter = collections.Counter(all_files)
    with open("counted_files", "wb") as file:
        file.write(str(counter))

def find_bak_files():
    with open(filter_set_file, "rU") as file:
        reader = csv.reader(file)
        reader.next()
        with open("bak_removed.csv", "wb") as output:
            writer = csv.writer(output)
            writer.writerow(["filename","line_num","timestamp","comment"])
            for row in reader:
                if ".bak" in row[0]:
                    print row
                    continue
                else:
                    writer.writerow(row)

def filter_spacing():
    print csv_file
    with open(csv_file, "rU") as file:
        reader = csv.reader(file)
        reader.next()
        for row in reader:
            print row

if __name__ == "__main__":
    #csv_file = sys.argv[1]
    #filter_spacing()
    #find_duplicates()
    #count_all_files()
    filter_set_file = sys.argv[1]
    find_bak_files()
