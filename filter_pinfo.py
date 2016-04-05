import csv
import sys
import os

import collections

csv_file = ""

bak_filtered_file = ""

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
                   "pesonal",
                   "PI",
                   "p.i."]

personal_clans = []

personal_dictionary = []




def filter_bak_files():
    global bak_filtered_file
    with open(csv_file, "rU") as file:
        reader = csv.reader(file)
        reader.next()
        with open("bak_removed.csv", "wb") as output:
            bak_filtered_file = "bak_removed.csv"
            writer = csv.writer(output)
            writer.writerow(["filename","line_num","timestamp","comment"])
            for row in reader:
                if ".bak" in row[0]:
                    print row
                    continue
                else:
                    writer.writerow(row)


def filter_personal_info():
    with open(bak_filtered_file, "rU") as input:
        reader = csv.reader(input)
        reader.next()
        with open(output_file, "wb") as output:
            writer = csv.writer(output)
            writer.writerow(["file", "linenum", "timestamp", "comment"])
            for row in reader:
                print row
                if any(x in row[3] for x in personal_string):
                    writer.writerow(row)
                    personal_clans.append(row[0])
            with open("list_personal_clanfiles.csv", "wb") as clan_list:
                clan_list.write("file\n")
                for file in set(personal_clans):
                    clan_list.write(file+"\n")


def list_of_all_files():
    files = []
    with open(csv_file, "rU") as file:
        reader = csv.reader(file)
        reader.next()
        for row in reader:
            files.append(row[0])

    return list(set(files))


if __name__ == "__main__":
    csv_file = sys.argv[1]

    output_file = csv_file.replace(".csv", "_pinfo_filtered.csv")

    all_files = list_of_all_files()
    filter_bak_files()


    filter_personal_info()

    os.remove(bak_filtered_file)