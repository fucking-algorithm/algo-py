from d_string import String


def test_string():
    s = String('abcabcabd')
    print('s = {}'.format(s))

    index = s.index(String('abd'))
    print('index of abd = {}'.format(index))

    index2 = s.index(String('abc'))
    print('index of abc = {}'.format(index2))

    index3 = s.index(String('a'))
    print('index of a = {}'.format(index3))

    s1 = String('00000000000000000001')
    print('s1 = {}'.format(s1))
    print('>>> {}'.format(s1.data))
    index4 = s1.index(String('0000000001'))
    print('index of 0000000001 = {}'.format(index4))


if __name__ == "__main__":
    test_string()
