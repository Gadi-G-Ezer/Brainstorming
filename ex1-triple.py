COEFFICIENT = 3  # value must be an integer


def triple(given_str: str):
    """
    function triple that receives a string, and returns another string where each character in the original
    string is multiply by the given constant COEFFICIENT.
    :param given_str:
    """
    return ''.join(char * int(COEFFICIENT) for char in str(given_str))


def main():
    assert triple(123) == '111222333'
    assert triple('abc') == 'aaabbbccc'
    assert triple([1, 2, 3]) == '[[[111,,,   222,,,   333]]]'
    assert triple((1, 2, 3)) == '(((111,,,   222,,,   333)))'
    assert triple({1, 2, 3}) == '{{{111,,,   222,,,   333}}}'
    assert triple({1: 'a', 2: 'b', 3: 'c'}) == "{{{111:::   '''aaa''',,,   222:::   '''bbb''',,,   333:::   '''ccc'''}}}"

    print(triple(input('insert a string:\n')))


if __name__ == '__main__':
    main()
