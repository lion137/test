# returns list of the all files matched against regex
# pattern in the given directory
import os
import re
import sys

from pprint import pprint



def open_file(fname, mode='r'):
    """Open a file and return a file object.
    """
    try:
        return open(fname, mode)
    except IOError as e:
        print("File {} could not be opened: {}".format(fname, e))
        sys.exit(1)


def read_file_lines(file):
    """Read all lines from a file and return a list of strings.
    """
    lines = []
    with open_file(file) as f:
        for line in f:
            lines.append(line.rstrip())
    return lines


def get_file_paths(dir_path):
    """Get all file paths in a directory.
    """
    file_paths = []
    for root, dirs, files_dir in os.walk(dir_path):
        for file in files_dir:
            file_paths.append(os.path.abspath(os.path.join(root, file)))
    return file_paths


def get_match_fnames(files, pattern):
    """Get all matches files from a list of file names.
    """
    def is_match_in_file(fname, pattern):
        strings = read_file_lines(fname)
        for string in strings:
            if re.search(pattern, string):
                return fname
    return [f for f in files if is_match_in_file(f, pattern)]
    

if __name__=='__main__':
    p = re.compile("(?=assertAlmostEqual\(.*[\d]+\.?[\d]{6,}\))")
    pprint(get_match_fnames(get_file_paths(sys.argv[1]), p))