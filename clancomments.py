import os
import sys
import csv
import itertools
import re

start_dir = ""

interval_regx = re.compile("(\025\d+_\d+)")


def parse_comments(clan_file):
    comments = []
    with open(clan_file, "rU") as file:
        with open("test2.txt", "wb") as output:
            last_buffer = None



            curr_index = 0
            for index, lines in enumerate(itertools.izip_longest(*[file]*7)):
                temp_comment = [None, None, None] # (index, timestamp, comment)
                output.write("glob_index: {}\n".format(index))

                for line_index, line in enumerate(lines):
                    if not line:
                        continue
                    curr_index = 7*index+line_index
                    output.write("real_index: {} ::   ".format(curr_index))
                    output.write(line)


                    if line.startswith("%com:") or line.startswith("%xcom:"):
                        temp_comment[0] = curr_index
                        temp_comment[2] = line
                        temp_buffer = lines[0:line_index]

                        print "curr_index: {}\ntemp_buffer: {}\n".format(curr_index, temp_buffer)

                        interval_string = reverse_interval_lookup(temp_buffer)
                        if interval_string is None:
                            interval_string = reverse_interval_lookup(last_buffer)

                        temp_comment[1] = interval_string
                        comments.append(temp_comment)

                last_buffer = lines
    return comments

def reverse_interval_lookup(buffer):
    temp_interval_string = None
    for i, element in reversed(list(enumerate(buffer))):
        interval_regx_result = interval_regx.search(element)
        if not interval_regx_result:
            continue
        else:
            temp_interval_string = interval_regx_result.group()\
                                                       .replace("\025", "")
    return temp_interval_string


def output_comment_csv(comments):
    with open("comments.csv", "wb") as file:
        writer = csv.writer(file)
        writer.writerow(["line_num", "timestamp", "comment"])
        writer.writerows(comments)

def walk_tree():
    for root, dirs, files in os.walk(start_dir):
        if os.path.split(root)[1] == "Audio_Annotation":
            for file in files:
                if "_newclan_merged.cha" in file or "_final.cha" in file:
                    print file


if __name__ == "__main__":

    start_dir = sys.argv[1]

    #walk_tree()
    comments = parse_comments("data/15_10_coderSM_final.cha")
    output_comment_csv(comments)
