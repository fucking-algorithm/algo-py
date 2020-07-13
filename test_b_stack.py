from b_stack import Stack
from b_stack import LinkedStack


def test_stack():
    stack = Stack(5)
    print('empty stack = {}'.format(stack))
    stack.push('a')
    stack.push('b')
    stack.push('c')
    print('stack = {}'.format(stack))
    print('top = {}'.format(stack.top))

    p1 = stack.pop()
    p2 = stack.pop()
    print('p1 = {}'.format(p1))
    print('p2 = {}'.format(p2))
    print('stack = {}'.format(stack))
    print('top = {}'.format(stack.top))


def test_linked_stack():
    ls = LinkedStack()
    print('empty ls = {}'.format(ls))
    ls.push('a')
    ls.push('b')
    ls.push('c')
    print('ls = {}'.format(ls))

    p1 = ls.pop()
    print('p1 = {}'.format(p1))
    p2 = ls.pop()
    print('p2 = {}'.format(p2))
    print('ls = {}'.format(ls))


if __name__ == "__main__":
    # test_stack()
    test_linked_stack()
