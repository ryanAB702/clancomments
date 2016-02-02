import csv
import sys
import os

import collections

csv_file = ""
filter_set_file = ""

all_files = []
file_set = None
counter = None

# bunch of misspelled versions of "personal"
personal_string = ["personal",
                   "prsonal",
                   "pwrsonal",
                   "persanal",
                   "personl",
                   "pursanal",
                   "pesonal"]

personal_clans = []

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
    with open(csv_file, "rU") as file:
        reader = csv.reader(file)
        reader.next()
        for row in reader:
            print row

def find_personal_info():
    with open(csv_file, "rU") as input:
        reader = csv.reader(input)
        reader.next()
        with open("clan_personalinfo_comments.csv", "wb") as output:
            writer = csv.writer(output)
            writer.writerow(["file", "linenum", "timestamp", "comment"])
            for row in reader:
                if any(x in row[3] for x in personal_string):
                    writer.writerow(row)
                    personal_clans.append(row[0])
            with open("list_personal_clanfiles.csv", "wb") as clan_list:
                clan_list.write("file\n")
                for file in set(personal_clans):
                    clan_list.write(file+"\n")

if __name__ == "__main__":
    csv_file = sys.argv[1]

    #filter_spacing()
    #find_duplicates()
    #count_all_files()
    #filter_set_file = sys.argv[1]
    #find_bak_files()

    find_personal_info()