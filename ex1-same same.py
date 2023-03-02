def samesame(input_list):
    """
    the function sums the members of a list, but can work with different types as well.
    that is, not only numbers, like so:
    samesame(['a', 'b', 'c']) --> 'abc' ; samesame([2, 4, 5]) --> 11 ; samesame([[1,2], [3,4]]) --> [1, 2, 3, 4] .

    :param input_list:
    :return:
    """

    try:
        return sum(input_list)
    except:
        try:
            for i in range(1, len(input_list)):
                input_list[0] += input_list[i]
            return input_list[0]
        except:
            print('not a valid input. try again')


def main():
    assert samesame(['a', 'b', 'c']) == 'abc'
    assert samesame([2, 4, 5]) == 11
    assert samesame([[1, 2], [3, 4]]) == [1, 2, 3, 4]


if __name__ == '__main__':
    main()
