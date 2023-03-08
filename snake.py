import re

CIPHER_DICT = {'s': 'L', 'b': 's', 'w': 'O', 'z': 'G', 'c': 'o', 'J': 'y', 'V': 't', 'P': 'w', 'B': 'f', 'Z': 'q',
               'F': 'k', 'O': 'N', 'u': 'A', 'W': 'r', 'K': 'K', 'a': 'D', 'v': 'l', 'g': 'S', 'f': 'x', 'x': 'c',
               'N': 'e', 'p': 'b', 'U': 'a', 'j': 'P', 'o': 'Q', 'i': 'I', 'M': 'd', 't': 'U', 'H': 'V', 'X': 'i',
               'Y': 'T', 'R': 'H', 'h': 'X', 'L': 'z', 'G': 'F', 'A': 'W', 'm': 'n', 'T': 'u', 'l': 'B', 'C': 'Z',
               'q': 'p', 'D': 'v', 'I': 'g', 'n': 'h', 'y': 'C', 'S': 'j', 'k': 'M', 'd': 'J', 'Q': 'E', 'e': 'Y',
               'r': 'R', 'E': 'm'}


STRING = "YXu0hYq1xQ4,hQXUCw8Cs7nIu8BAxIUADYf\n\nLRYUYw5LI0RYUUYs6hDXU3UIoIBbcm\n.CBSA5LI7RYUUYs2hDXU8YBbnIj\n.UIoIBb" \
         "nI2LI8RYUUYs7hDXU2cYBbnQZ\n.cYBbnQo1LI9RYUUYs7hDXU4UDBk\n.JYUDoIBbnQo4LI3RYUUYs8hDXU6YLRDbj\n.JYULYh8LI3RYU" \
         "UYs8hDXU1CUIBIsDJDYH\n.YLhYJ7BDIoYbj\n.LUhAQo0LYLDo3U'hYRD2BDIoYbL2XSAQhY0QU0MDYRs0YXU4XSAQXUBW\n.LYBAR8CUI" \
         "BDoIUoDRb1LUDYs2LRQRRm\n.CUIRAb3JBAQXL6RYlYh9LLDb0LLYBha\n.CBUhYBIL0CBUIoIBbcY9hg\n.JYohYBIL1YXU5YoDx7xQ6,C" \
         "UIASIsnD8YLAxYR0YXU9hQIUDUbnYU4QU3YRYXu\n.LLYAS1JBAQXL7Ys3--YhQ2JhD2CBsDRYxYRb2CBhQ9YhQ6LAQIlsQ--9CDO7QU1" \
         "QJ0XSAQXUBW\n.UI4UDXU5CDO0CDn2UQh7Ys2LAQIlsQ0UD2ULRIx8LLYBhA2YR'AQC1OQe\n.XoUAv7LI3RYUUYs0hDXU8XSAQXUBW\n" \
         ".RYlYh0RYlYh5LI9hYUxQ0RYUUYs2hDXU8*UXSIR*9xg\n.OQh4YXU3hQIUDUhYnYBbnI9LI1JRDX0QU6,hIDBbcY5L'UI3D7JDs6xg\n." \
         "DYJI4YXU6hQIUDUhYnYBbnI9LI9CLDY4QU3,hIDBbcY2UI5CDn4Ys8D8JQQS1LYoDbLYnDe\n.DYJI0YRD9YhQ6ShIMhQX2UDYRS4DY" \
         "JI3--9L'UYB5QJ8YRQn9xQ0!YLQXU"


def decipher(text: str):
    """
    function creates a substitution cipher dictionary by replacing between keys and values of the given cipher
    dictionary. in the second step function replace numbers with space. using the created dictionary, if a character is
    in the created dictionary, it is replaced with its match. finally the order of the letter is changed to their
    original position.
    :param text:
    """
    original_text = ""
    active_cipher_dict = dict(zip(CIPHER_DICT.values(), CIPHER_DICT.keys()))
    # step 1
    switch_words_around_newline = re.sub(r'([a-zA-Z.]+)(\n+)([a-zA-Z.]+)', r'\3\2\1', text)
    # step 2
    getting_back_space = re.sub(r'\d+', ' ', switch_words_around_newline)
    # step 3
    for line in getting_back_space.split('\n'):
        original_text += " ".join(
            ["".join(map(lambda a: active_cipher_dict[a] if a in active_cipher_dict.keys() else a, word))[::-1]
             for word in line.split()]) + '\n'
    return original_text


def main():
    original_text = decipher(STRING)
    print(original_text)


if __name__ == "__main__":
    main()
