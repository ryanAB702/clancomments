# clancomments

This is a collection of scripts for pulling out all the comments from a collection of CLAN files.

## usage

#### clancomments.py

```bash
$: python clancomments.py /path/to/Subject_Files  output_file.csv
```

This will generate a csv file with all the comments found in each .cha file.

#### filter_pinfo.py

```bash
$: python filter.py clancomments_output.csv
```

This will filter out all the comments except for the personal info comments and get rid of .bak versions of files.

The output file will have the same name/path as the input, except with "pinfo_filtered" tagged on at the end.

#### pinfo_table.py

```bash
$: python pinfo_table.py unfiltered_comments.csv filter_py_output.csv
```

This will generate a table filled with different values based on the personal info status of every subject/visit file.

You should pass it the unfiltered comments csv and the output of the filter_pinfo.py script (all comments filtered down to just the personal info comments).
