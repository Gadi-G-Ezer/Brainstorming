def multiplier(given_str: str):
    """
    function receives a string and returns it with every character mutiplied.
    :param given_str: given string
    :return result: returned string with every character mutiplied.
    """
    result = ''
    for char in given_str:
        result += char*2
    return result


def main():
    given_str = input('insert string:\n')
    if given_str is None:
        print('you did not input any value :(')
    else:
        print(multiplier(given_str))


if __name__ == '__main__':
    main()