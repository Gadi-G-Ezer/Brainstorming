def numbers_multiplier(numbers_list: list):
    """
    assuming that the input is valid – that is, the user has only inserted integers delimited by a space,
    function receives list of inegers as strings and retuns their product.
    :param numbers_list: given list of integers
    :return product: product of all numbers in the given list
    """
    product = 1
    for number in numbers_list:
        product *= int(number)
    return product


def main():
    integers_list = input('insert a list of numbers delimited by space:\n').split()
    print(numbers_multiplier(integers_list))


if __name__ == '__main__':
    main()