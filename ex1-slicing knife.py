GIVEN_STR = "We were more than just a slice"


def slicing(begin: int(), end: int(), jump=1, input_str=GIVEN_STR):
    """
    function receives a string slice it and return the result.
    :param input_str: original string
    :param begin: start slicing from
    :param end: end slicing at
    :param jump: how many characters to jump
    :return result: sliced string
    """
    print(input_str[begin:end:jump])


def answers():
    """
    this function return answers 1 to 5 :
    1) 'We wer'
    2) 'ere more than just a sli'
    3) 'W eemr hnjs lc'
    4) 'wr oeta utasi'
    5) 'ecils a tsuj naht erom erew eW'
    """
    for question_number in range(1, 6):
        print(f"Answer {question_number}:\t")
        if question_number == 1:
            slicing(0, 6)
        elif question_number == 2:
            slicing(4, -2)
        elif question_number == 3:
            slicing(0, len(GIVEN_STR), 2)
        elif question_number == 4:
            slicing(3, -1, 2)
        else:
            print(GIVEN_STR[::-1])


if __name__ == '__main__':
    answers()
