from a_list import LinkedList

"""线性表测试
"""

def test_list():
    """Python内建 线性表 顺序存储结构

    类比 jdk 的 ArrayList

    时间复杂度:

    list[index]	O(1)

    list.append	O(1)

    list.insert	O(n)

    list.pop()	O(1)

    list.pop(i) O(n)

    list.remove	O(n)
    """
    l = list()
    l.append('a')
    l.append('b')
    print('l[0] = ' + l[0])

    l.insert(0, 'zero')
    print('after insert(0, ...), l = ' + str(l))

    print('pop(2), return ' + l.pop(2))
    print('after pop(2), l = ' + str(l))

    print('remove(...), return ' + str(l.remove('a')))
    print('after remove, l = ' + str(l))


def test_linked_list():
    """线性表 链式存储 测试"""

    ll = LinkedList()
    ll.append('a')
    ll.append('b')
    ll.append('c')
    ll.append('d')

    print('length = %s' % ll.length)
    print('ll = {}'.format(ll))
    print('0 = ' + str(ll.get(0)))
    print('1 = %s' % ll.get(1))
    print('4 = %s' % ll.get(4))

    ll.insert(1, 'aa')
    print('ll = {}'.format(ll))

    pop = ll.pop(2)
    print('pop = {}'.format(pop))
    print('after pop , ll left {}'.format(ll))

    ll.remove('d')
    print('after remove, ll = {}'.format(ll))


if __name__ == "__main__":
    # test_list()
    test_linked_list()
