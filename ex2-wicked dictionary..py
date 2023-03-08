class WickedDictionary():

    def __init__(self):
        self.element_dict = dict()

    def __str__(self):
        return str(self.element_dict)

    def __setitem__(self, key, value):
        if key in self.element_dict.keys():
            self.element_dict[key] = value
        else:
            self.element_dict[key*2] = value

    def __getitem__(self, item):
        return self.element_dict[item]


def main():
    a = WickedDictionary()
    assert a.element_dict == {}

    a[1] = 'a'
    assert a.element_dict == {2: 'a'}
    assert a[2] == 'a'

    a['ab'] = 2
    assert a.element_dict == {2: 'a', 'abab': 2}

    a['abab'] = 7
    assert a.element_dict == {2: 'a', 'abab': 7}

    assert str(a.element_dict) == "{2: 'a', 'abab': 7}"


if __name__ == '__main__':
    main()



