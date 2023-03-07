import sys

def replace_single(single: list):
    """
    replace a letter in a single string that will be called for each string by replacer()
    :param single: list
    """
    try:
        index = int(single[0])
    except TypeError as error:
        return error
    else:
        if index >= len(single[1]) or index < -1*len(single[1]):
            raise ValueError(f"Error: index value shouldn't exceed the string length! ")

    try:
        new_string = single[1][:index] + single[2]
        if index + 1 < len(single[1]) or index < -1:
            new_string += single[1][index+1:]
    except TypeError as error:
            return error
    else:
        return new_string


def replacer(params):
    """
    using Exceptions, that knows to replace a character at a given
    index in a string with a different single character. It can handle multiple strings at the same time.
    replacer() function will:
    ● receive from main() a list of all the inputs that were given by caller on the comman line beside the argv[0]
    where the Python file name is given (ex2-replacer.py)
    ● return a list of changed strings
    ● not print any messages to the user, we got it covered in main()
    ● main() (already implemented and should not be touched) will print the result or error message

    Usage:
    ex2-replacer.py --help; - displays help message
    ex2-replacer.py num_replacements [index1 str1 char_to_replace_with1 [index2 str2 char_to_replace_with2]...];

    Examples:
    ex2-replacer.py 0&quot; - do not do any replacements. Will print "" - empty string
    ex2-replacer.py 1 0 boat g - will print "goat"
    ex2-replacer.py 2 0 boat g 2 boat o - will print "goat boot"
    """
    try:
        num_replacements = int(params[0])
    except TypeError:
        print(f'Error: expecting integer as number of replacements but got {type(params[0])}!')
    else:
        if len(params) != 1 + (3 * num_replacements):
            raise ValueError(f'Error: expecting {(3 * num_replacements) + 1} elements but received {len(params)}!')
        elif num_replacements == 0:
            return [""]

    output_list = []
    for i in range(1, len(params), 3):
        sub_list = params[i: i+3]
        temp = replace_single(sub_list)
        if isinstance(temp, BaseException):
            return temp
        else:
            output_list.append(temp)

    return output_list


# WARNING: DO NOT CHANGE CODE BELOW THIS LINE


HELP_STRING = """Welcome to the replacer!
Replacer knows to replace a character at a given index in a string with a different single character.
It knows to do so for multiple strings.
It prints a the strings after replacement.

Usage:
"ex2-replacer.py --help" - display this message
"ex2-replacer.py num_replacements [index1 str1 char_to_replace_with1 [index2 str2 char_to_replace_with2]...]"

Examples:
"ex2-replacer.py 0" - do not do any replacements.  Will print "" - empty string
"ex2-replacer.py 1 0 boat g" - will print "goat"
"ex2-replacer.py 2 0 boat g 2 boat o" - will print "goat boot"
"""

NUM_ARGS_NO_ARGS = 1
NUM_ARGS_HELP = 2


def main():
    if len(sys.argv) == NUM_ARGS_HELP and sys.argv[1] == '--help':
        print(HELP_STRING)
        return
    elif len(sys.argv) == NUM_ARGS_NO_ARGS:
        print(f'ERROR: No arguments were given.\nFor proper usage:\n{HELP_STRING}')
        return

    try:
        result = replacer(sys.argv[1:])
    except Exception as ex:
        print(f'ERROR: {ex}\n\nUsage instructions:\n{HELP_STRING}')
    else:
        print(f'SUCCESS: Result of replacing the letters is:\n', ' '.join(result))


if __name__ == '__main__':
    main()
