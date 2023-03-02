#!/usr/bin/python -tt
##   adapted in numerous ways by ITC to clarify instructions
##   adapted to Python3 for ITC - 17/10/18
##       - also added pep8 and naming convention compliance
##   instructions were changed to deal with proper handling of punctuation   
##
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete.  
    Depending on the flag provided by user on command line, it calls 
    print_words() or print_top() functions which you will implement.

Tip: don't build the whole program at once. Get it to an intermediate
    milestone and print your data structure. When that's working, try for the next milestone.

1. For the --count flag, implement a print_words(filename) function that counts
    how often each word appears in the text and prints:
word1 count1
word2 count2
...

    - Print the above list in alphabetical order.
    - Store all the words as lowercase, so 'The' and 'the' count as the same word.
    - Hint: Use str.split() (no arguments) to split into words by whitespace.
    - Hint: Do not assume that the file exists, print an appropriate message

2. Improve print_words() to deal with punctuation so it's not included as part of the word.
    For example:
    Alice     Alice:     "Alice      Alice,    Alice"   are all the same word   >>>> alice
    BUT - In words like  Alice's   or   they're, the apostrophe is part of the word
        so don't split them into into    Alice + s    or   they  +  re
        
    Tip: don't look for an exact definition. There is no such word as "Alice:",
        so it make sense to turn it into "alice".  
        But splitting Alice's by ' would create 2 words: "alice" and "s", and since "s" is 
        not a word, and for simplicity reasons since we are not in NLP course, and not doing
        proper tokenizining, let's keep it simple, and leave "alice's" as one word.
        

3. For the --topcount flag, implement a print_top(filename) function similar
    to print_words() but which prints just the top 20 most common words (and their counts) 
    sorted so the most common word is first, then the next most common, and so on.

    Tips:
    - Since print_words() and print_top() share similar functionality, 
    please use functions and reuse code to prevent writing duplicated code.  
    For example, in addition to  print_words(filename) and print_top(filename) functions,
    write additional functions that read a file, build a word/count dict and so on.

5. Make sure to write and submit tests for as much of your code and functions as possible.
    It's OK not to test 100% of your code 
    (it's OK not to test input from command line and actually reading files),
    but try to reach a high percentage of testing of the rest of the code.
    
    Tip: you might need to restructure your functions further to reach a high level of test coverage
"""

import sys

# constants used for main()
REQUIRED_NUM_OF_ARGS = 3
ARG_OPTION = 1
ARG_FILE_NAME = 2


# +++your code here+++
import re

ALICE_FILE = r'D:\Academy\Studying\Bootcamp\ITC Feb 23\Assignments\Python_1\Questions\ex2-alice.txt'
TOP_LIST_LENGTH = 20


def create_word_dictionary(file_path: str):
    """
    function reads the file at the given path, and create a dictionary of which keys and values are the words and their
    occurrences. function consider as a word any sequence that starts and ends with letters and in between may have
    apostrophe.
    :param file_path:
    :return word_dictionary:
    """
    word_dictionary = {}
    #  reading the file
    try:
        with open(file_path, 'r') as f:
            word_list = re.findall('[a-z]+\'*[a-z]+', f.read(), re.IGNORECASE)
    except FileNotFoundError as error:
        print('Error:', error)
    except OSError as error:
        print('Error:', error)
    except BaseException as error:
        print('Error:', error)
    else:
        #  creating dictionary of which keys and value are the words and their occurrences
        for word in word_list:
            if word.lower() in word_dictionary.keys():
                word_dictionary[word.lower()] += 1
            else:
                word_dictionary.update({word.lower(): 1})

        return word_dictionary


def sort_dictionary(sort_flag: str, given_dictionary: dict):
    """
    function receives a dictionary and returns a sorted list of tuples from the form : [(key, value), (key, value), ...].
    list is either sorted by the key or sorted by the value, according to the given sort_flag (i.e. key or value).
    sorting by key is done in ascending order and sorting by the value is done descending order.

    :param sort_flag:
    :param given_dictionary:
    """
    return sorted([(key, value) for key, value in given_dictionary.items()],
                  key=lambda a: a[0 if sort_flag == 'key' else 1], reverse=False if sort_flag == 'key' else True)


def print_words(filename=ALICE_FILE):
    """
    function read a file from a given path and prints the words and their number of occurrences.

    (function consider as a word any sequence that starts and ends with letters and in between may have
    apostrophe).
    :param filename:
    """
    word_dictionary = create_word_dictionary(filename)
    if word_dictionary:
        for word, occurrences in sort_dictionary(sort_flag='key', given_dictionary=word_dictionary):
            print(word, occurrences)


def print_top(filename=ALICE_FILE):
    """
    function read a file from a given path and prints the top common words and their number of occurrences.

    (function consider as a word any sequence that starts and ends with letters and in between may have
    apostrophe).
    :param filename:
    :return:
    """
    word_dictionary = create_word_dictionary(filename)
    if word_dictionary:
        i = 1
        for word, occurrences in sort_dictionary(sort_flag='occurrences', given_dictionary=word_dictionary):
            if i <= TOP_LIST_LENGTH:
                print(word, occurrences)
                i += 1
            else:
                break


def all_tests():
    # your code here
    assert sort_dictionary(sort_flag='key', given_dictionary={'a': 2, 'b': 1, 'c': 3}) == [('a', 2), ('b', 1), ('c', 3)]
    assert sort_dictionary(sort_flag='occurrences', given_dictionary={'a': 2, 'b': 1, 'c': 3}) == [('c', 3), ('a', 2), ('b', 1)]


### DO NOT CHANGE FOLLOWING THIS LINE ###################

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    """
    Gets user input - file name and which option --count or --topcount
    Reads text file, counts and sorts words
    """

    if len(sys.argv) != REQUIRED_NUM_OF_ARGS:
        print("usage: ./wordcount.py {--count | --topcount} file")
        return

    option = sys.argv[ARG_OPTION]
    filename = sys.argv[ARG_FILE_NAME]
    if option == "--count":
        print_words(filename)
    elif option == "--topcount":
        print_top(filename)
    else:
        print("unknown option: " + option)


if __name__ == "__main__":
    all_tests()
    main()
