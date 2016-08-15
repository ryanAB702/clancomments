import os
import sys
import csv
import itertools
import re

start_dir = ""
output_path = ""

interval_regx = re.compile("(\x15\d+_\d+)")

comments = []

def parse_comments(clan_file):
    comments = []
    with open(clan_file, "rU") as file:
        filename = os.path.split(clan_file)[1]
        print "Processing {}......".format(clan_file)
        last_buffer = None

        curr_index = 0
        for index, lines in enumerate(itertools.izip_longest(*[file]*7)):
            for line_index, line in enumerate(lines):
                temp_comment = [None, None, None, None] # (index, timestamp, comment)
                if not line:
                    continue

                curr_index = 7*index+line_index
                #print "curr_index: {}".format(curr_index)
                if line.startswith("%com:") or line.startswith("%xcom:"):
                    temp_comment[0] = filename
                    temp_comment[1] = curr_index
                    temp_comment[3] = line
                    temp_buffer = lines[0:line_index]

                    interval_string = reverse_interval_lookup(temp_buffer)
                    if interval_string is None:

                        interval_string = reverse_interval_lookup(last_buffer)

                    temp_comment[2] = interval_string
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
    with open(output_path, "wb") as file:
        writer = csv.writer(file)
        writer.writerow(["filename", "line_num", "timestamp", "comment"])
        writer.writerows(comments)

def filter_comments(comments):
    filtered_comments = []

    for comment in comments:
        if "|" in comment[3]:
            continue
        else:
            filtered_comments.append(comment)
    return filtered_comments

def walk_tree():
    global comments
    for root, dirs, files in os.walk(start_dir):
        if subject_files:
            if os.path.split(root)[1] == "Audio_Annotation":
                for file in files:
                    if "_newclan_merged.cha" in file or "_final.cha" in file:
                        try:
                            all_comments = parse_comments(os.path.join(root, file))
                            filtered_comments = filter_comments(all_comments)
                            comments += filtered_comments
                        except Exception:
                            print "File: {}      was a problem".format(file)
        else:
            for file in files:
                if "_newclan_merged.cha" in file or "_final.cha" in file:
                    try:
                        all_comments = parse_comments(os.path.join(root, file))
                        filtered_comments = filter_comments(all_comments)
                        comments += filtered_comments
                    except Exception:
                        print "File: {}      was a problem".format(file)

if __name__ == "__main__":

    start_dir = sys.argv[1]
    output_path = sys.argv[2]

    subject_files = False
    if len(sys.argv) > 3:
        if sys.argv[3] == "--subj-files":
            subject_files = True


    walk_tree()
    # all_comments = parse_comments("data/14_09_newclan_merged.cha")
    # filtered_comments = filter_comments(all_comments)
    output_comment_csv(comments)
