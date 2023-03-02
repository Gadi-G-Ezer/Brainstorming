COEFFICIENT = 3  # this should be an integer


def space_triple(given_str: str):
    """
    function receives a string, and returns another string where each word in the original string is tripled
    :param given_str:
    """
    return ' '.join([word * int(COEFFICIENT) for word in str(given_str).split()])


def main():
    assert space_triple('hello') == 'hellohellohello'
    assert  space_triple('hello world') == 'hellohellohello worldworldworld'
    assert  space_triple([1, 2, 3]) == '[1,[1,[1, 2,2,2, 3]3]3]'

    print(space_triple(input('insert a string:\n')))


if __name__ == '__main__':
    main()




