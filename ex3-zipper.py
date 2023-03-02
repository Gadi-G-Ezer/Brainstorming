def iterable_validation(iterable):
    """
    function validates given iterable is either a list or a tuple and returns True or False accordingly.
    """
    if isinstance(iterable, (list, tuple)) and iterable:
        return True
    print('Error: not a valid iterable! iterable should be non empty list or tuple.')
    return False


def zipper(iterable1, iterable2):
    """
    function receives two iterables, each of them is either a list or a tuple.
    it returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or
    iterables. The returned list’s length is equal to the length of the shorter argument the function receives.
    """
    if iterable_validation(iterable1) and iterable_validation(iterable2):
        print(f'zipper({iterable1}, {iterable2}) result is: ')
        i = 0
        result = []
        while i < min(len(iterable1), len(iterable2)):
            result.append((iterable1[i], iterable2[i]))
            i += 1
        print(result,'\n')
        return result


def str_validation(given_input: str):
    """
    function receive a string and validate it's not empty and that it contains either  a tuple or a list.
    function returns the variable if it meets the above criteria and return an empty list otherwise.
    """
    if given_input:
        try:
            return given_input.split()
        except:
            print('Error: not a valid input!')
    else:
        print('Error: no input was provided!')
    return []


def provide_iterables():
    """
    function receives user input and validates it contains two iterables where each of them is either a tuple or a list.
    lastly the function returns a list of the given two iterables.
    """
    iterables_list = []
    while len(iterables_list) < 2:
        temp = str_validation(input(f'insert {len(iterables_list)+1} out of 2 iterables,\nprovide list of characters delimited by space (‘ ‘):\n'))
        if temp:
            iterables_list.append(temp)
    return iterables_list


def main():
    iterables_list = provide_iterables()
    result = zipper(iterables_list[0], iterables_list[1])


if __name__ == '__main__':
    print('tests are being processed . . .')
    assert zipper([1,2,3], [4,5,6]) == [(1, 4), (2, 5), (3, 6)]
    assert zipper([1,"hello world"], (4,5,6,7,8,9)) == [(1, 4), ('hello world', 5)]
    assert zipper(5, (1, 2)) is None
    assert zipper([], ()) is None
    print('\ntests are ok. lets move on ...\n')

    main()
