# clancomments

This is a collection of scripts for pulling out all the comments from a collection of CLAN files.

## usage

#### clancomments.py

```bash
$: python clancomments.py /path/to/Subject_Files
```

This will generate a csv file with all the comments found in each .cha file.

#### filter.py

```bash
$: python filter.py clancomments_output.csv
```


This will filter out all the comments except for the personal info comments. And get rid of duplicates and .bak versions of files.

#### pinfo_table.py

```bash
$: python pinfo_table.py filter_py_output.csv
```

This will generate a table filled with different values based on the personal info status of every subject/visit file.
