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

personal_dictionary = []
def init_personalinfo_dictionary():
    for i in range(47):
        personal_dictionary.append(["no-pi"]*13)

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

def generate_nopersonalinfo_files():
    for file in set(personal_clans):
        prefix = file[0:5].split("_")
        print "original: {}".format(prefix)
        prefix = [int(prefix[0]), prefix_to_array_index(prefix[1])]
        print "new: {}".format(prefix)

        personal_dictionary[prefix[0]][prefix[1]] = "**PI**"
    with open("clan_personalinfo_table.csv", "wb") as table:
        writer = csv.writer(table)
        writer.writerow(["subject-visit", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18"])
        for index, subject in enumerate(personal_dictionary[1:]):
            writer.writerow([index+1] + subject)

def prefix_to_array_index(prefix):
    if prefix == '06':
        return 0
    elif prefix == '07':
        return 1
    elif prefix == '08':
        return 2
    elif prefix == '09':
        return 3
    elif prefix == '10':
        return 4
    elif prefix == '11':
        return 5
    elif prefix == '12':
        return 6
    elif prefix == '13':
        return 7
    elif prefix == '14':
        return 8
    elif prefix == '15':
        return 9
    elif prefix == '16':
        return 10
    elif prefix == '17':
        return 11
    elif prefix == '18':
        return 12



if __name__ == "__main__":
    csv_file = sys.argv[1]
    print "hello"
    #filter_spacing()
    #find_duplicates()
    #count_all_files()
    #filter_set_file = sys.argv[1]
    #find_bak_files()
    init_personalinfo_dictionary()
    find_personal_info()
    generate_nopersonalinfo_files()