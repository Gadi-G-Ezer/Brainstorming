def samesame(given_lst: list):
    """
    the function sums the members of a list, but can work with different types as well–not only numbers, like so:
    the output for ['a', 'b', 'c'] will be 'abc', the output for [2, 4, 5] will be 11 and the output for [[1,2], [3,4]]
    will be [1, 2, 3, 4].
    :param given_lst:
    :return result:
    """
    if all([isinstance(item, (int, float)) for item in given_lst]):
        result = float()
        for num in given_lst:
            result += num
        return int(result) if result == int(result) else result
    if all([isinstance(item, (list, )) for item in given_lst]):
        result = []
        while given_lst:
            result.extend(given_lst.pop(0))
        return result
    return ''.join(str(item) for item in given_lst)


def validation(given_input: str):
    """
    function validate given string is not empty and can be split into a list and returns a list.
    note that an empy list is returned in case given string dors not meet the above criteria.
    """
    if not given_input:
        print('\nError: no input was provided! try again.')
        return []
    try:
        return [int(item) if int(item) == float(item) else float(item) for item in given_input.split()]
    except:
        return [validation(item[1:-1].replace(',', ' ')) if item[0]=='[' and item[-1] == ']' else item for item in given_input.split()]


def providing_list():
    """
    function receive and validate user input, i.e. string of list of elements, and return it as a list.
    """
    given_list = []
    while not given_list:
        given_list = validation(input('insert a list of elements delimited by space:\n'))
    return given_list


def main():
    print(samesame(providing_list()))


if __name__ == '__main__':
    print('\nsamesame() function is being tested ...')
    assert samesame(['a', 'b', 'c']) == 'abc'
    assert samesame([2, 4, 5]) == 11
    assert samesame([[1, 2], [3, 4]]) == [1, 2, 3, 4]
    assert samesame(['1', 'b']) == '1b'
    print('\nvalidation() function is being tested ...')
    assert validation('') == []
    assert validation('1 2') == [1, 2]
    assert validation('a b c') == ['a', 'b', 'c']
    assert validation('1 b') == ['1', 'b']
    assert validation('[1,2] [3,4]') == [[1,2], [3,4]]
    print("\n\n*** All tests results are ok. Let's move on !!! ***\n")

    main()





