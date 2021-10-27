"""This module solves file problem number 1 from code-questions-python.pdf"""
import argparse
import os
import re


def phrase_finder(phrase, text_file):
    """
    Takes takes a phrase and a text file as inputs, and returns True if the
    phrase is found in the document, False otherwise.
    :param phrase: (str) A case insensitive phrase to look for in the text file
    :param text_file: (str) path to text file relative to project root
    :return: (bool) Whether or not the phrase is in the text file
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
    text_file_directory = os.path.join(local_directory, text_file)

    with open(text_file_directory) as document:
        text_generator = read_large_file(document)

        # scan doc line by line until match is found or end of file is reached
        while True:
            try:
                text = next(text_generator).lower()
            except StopIteration:
                return False

            phrase = phrase.lower()
            # first check to see if entire phrase is in line,
            # if so no more work to be done
            if type(re.search(re.compile(phrase), text)) == re.Match:
                return True
            # otherwise we have to check if the phrase bleeds into another line
            # Work In Progress
            '''
            phrase_list = phrase.split()
            if type(re.search(re.compile(phrase_list[0]), text)) == re.Match:
                phrase_list.pop(0)
                text = text.split()
                # find where first occurance of word appears, and check if its 
                # the only occurance of that word, if so while next word is not
                # last word check to see if it's the next word in the phrase
                # and continue to next line if you reach end of current line
                start_index = text.index(phrase_list[0])
                while len(phrase_list) > 0:
            '''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--phrase', type=str, required=True,
                        help='Phrase to look for in file.')
    parser.add_argument('-fp', '--file_path', type=str, required=True,
                        help='Path relative to root of project to file to '
                             'search')
    args = parser.parse_args()

    print(phrase_finder(args.phrase, args.file_path))
