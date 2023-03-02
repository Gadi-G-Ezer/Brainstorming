def encode_title(given_str: str, pad_width: int):
    """
    This function receives a string, and a pad width, and encodes the string as a title.
    if pad width is not reached – then the title is padded with zeros to its left.

    :param given_str:
    :param pad_width:
    :return title:
    """
    return given_str.title().zfill(pad_width)


def main():
    while True:
        given_title = input('provide a string to encode:\n')
        if given_title != '':
            break
        print('Error: no string was provided! try again.')
    while True:
        try:
            min_string_length = int(input('provide minimum length of the string:\n'))
            break
        except:
            print('Error: input length is not valid! pls. input integer length.')
    print(encode_title(given_title, min_string_length))


if __name__ == '__main__':
    main()
