class LimitedList():
    """
    LimitedList object will be initialized with a maximum number of elements it can hold.
    After your object has reached its limit, whenever someone tries to append an additional value to the list – the new
    member will be appended, and the first member in the list will be erased.
    Your object should support append, as well as assignment and receiving items using []. In addition,
    it should implement the __str__ method.
        """

    def __init__(self, max_elements):
        if type(max_elements) != int or max_elements < 1:
            raise TypeError(f'Error: max_element parameter expecting integer value but received {type(max_elements)}!')
        self._max_elements = max_elements
        self._limited_list = []


    def __str__(self):
        return str(self._limited_list)
    
    def __setitem__(self, key, value):
        self._limited_list[key] = value

    def __getitem__(self, item):
        return self._limited_list[item]

    def append(self, value):
        self._limited_list.append(value)
        if len(self._limited_list) > self._max_elements:
            self._limited_list.pop(0)


def main():
    a = LimitedList(3)
    a.append('hello')
    a.append('Gadi')
    a.append('how')
    assert str(a) == "['hello', 'Gadi', 'how']"

    a.append('are')
    a.append('you?')
    assert str(a) == "['how', 'are', 'you?']"

    a[1] = 'Rrrrr.....'
    assert str(a) == "['how', 'Rrrrr.....', 'you?']"

    assert str(a[2]) == 'you?'


if __name__ == '__main__':
    main()





