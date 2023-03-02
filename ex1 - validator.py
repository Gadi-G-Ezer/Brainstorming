ERROR_MESSAGE = 'Please provide a valid input'


def product(numbers_lst: list):
    """
    function receives a list of numbers and returns their product.
    """
    try:
        result = 1
        for num in numbers_lst:
            result *= num
        return result if result != int(result) else int(result)
    except BaseException as error:
        print('Error: ', error)


def validation(given_input: str):
    """
    function receive a string and convert it to list of float numbers.
    if the string is empty or does not consist with numbers delimited by space an empty list will be returned.
    the last will be followed by an error message printed to the screen.
    """
    numbers_list = []
    if not given_input:
        print('Error: nothing was provided')
        return numbers_list
    try:
        numbers_list = [float(num) for num in given_input.split()]
    except:
        print(ERROR_MESSAGE)
    return numbers_list


def provide_list():
    """
    function get input from user, i.e. list of numbers delimited by space, and return a list of float numbers.
    """
    numbers_list = []
    while not numbers_list:
        numbers_list = validation(input("provide a list of numbers delimited by space (‘ ‘):\n"))
    return numbers_list


def main():
    print('Assert testing:')
    assert validation('123 a b') == []
    assert validation('a 1 4 5') == []
    assert validation('[1] 2') == []
    assert validation('-1 5.5') == [-1, 5.5]
    assert product([1, 2, 3]) == 6
    assert product([1, 0, 3]) == 0
    assert product(['a', 'b', 3]) == None
    assert product({'a', 'b', 3}) == None

    print('\nMoving on ...all tests results were good!\n')
    print(f'the product is: {product(provide_list())}')


if __name__ == '__main__':
    main()
