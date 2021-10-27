"""This module solves file problem number 2 from code-questions-python.pdf"""
import argparse
import os
import re


def add_nums_of_col_x(x, csv_file):
    """
    Takes a Comma Separated File (CSV) and a column number (zero being the left
     most column) and returns the sum of all the entries in that column.
     Assuming that all the entries in the CSV are integers, and that there are
     no column headers.
    :param x: (sint) The xth column to sum, startingat zero
    :param csv_file: (str) path to CSV file relative to project root
    :return: (int) Whether or not the phrase is in the text file
    """

    def read_large_file(file_object):
        """
        Use a generator to read file in case the file is too large to fit in
        memory.
        :param file_object: File object returned by built-in open() method
        :return: Generator object that yields lines from file
        """
        while True:
            line = file_object.readline()

            if not line: # have reached end of file
                break
            yield line

    local_directory = os.path.abspath(os.path.dirname(__file__))
    csv_file_directory = os.path.join(local_directory, csv_file)

    count = 0
    with open(csv_file_directory) as document:
        text_generator = read_large_file(document)

        # scan doc line by line adding xth element to count
        while True:
            try:
                nums = next(text_generator).split(',')
                if x > len(nums) - 1:
                    raise IndexError('X is larger than number of columns in '
                                     'csv, choose a smaller x value')
            except StopIteration:  # reached end of file
                return count

            count += int(nums[x])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', type=int, required=True,
                        help='Xth column to sum up')
    parser.add_argument('-fp', '--file_path', type=str, required=True,
                        help='Path relative to root of project to CSV file')
    args = parser.parse_args()

    print(add_nums_of_col_x(args.x, args.file_path))