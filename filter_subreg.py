import csv
import sys

def filter_subreg_comments(comments):
    result = []
    for row in comments:
        if "subregion" in  row[3]:
            result.append(row)
    return result

if __name__ == "__main__":
    comments_file = sys.argv[1]
    output_file = sys.argv[2]

    with open(comments_file, "rU") as input:
        reader = csv.reader(input)
        header = reader.next()
        print header
        filtered = filter_subreg_comments(reader)

        with open(output_file, "wb") as output:
            writer = csv.writer(output)
            writer.writerow(header)
            writer.writerows(filtered)
