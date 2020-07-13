"""
场景: 

- 递归, 

- 四则运算表达式求值
解决括号的问题: 碰到 '(', 就将其 push, 碰到 ')' 就将 '(' pop, 期间进行数字运算
解决先乘除后加减的问题: (中缀表示法, 后缀表示法/Reverse Polish Notation) 



"""

class Stack(object):
    """Stack 顺序存储结构

    借助 list, python 自带 ArrayList , 拿来即用:)
    """

    def __init__(self, stack_size=10):
        super().__init__()
        self.stack_size = stack_size
        # self.data = []
        self.data = [None] * stack_size  # 强行当做数组用
        self.top = -1  # top = -1 if the stack is empty

    def push(self, value):
        """O(1)"""

        if (self.top == self.stack_size):
            raise Exception('Stack full, cannot push')
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        """O(1)"""

        if self.top == -1:
            raise Exception('Stack is empty, cannot pop')
        result = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return result

    def __str__(self):
        return str(self.data)


class TwoShareStack(object):
    """两栈共享一个数组

    适合于元素类型相同, 此消彼长的场景
    """

    def __init__(self, max_size=10):
        super().__init__()
        self.max_size = max_size
        self.data = [None] * max_size
        self.top1 = -1
        self.top2 = len(self.data)

    def push(self, value, stack_number):
        if self.top1 + 1 == self.top2:
            raise Exception('Stack full.')
        if stack_number == 1:
            self.top1 += 1
            self.data[self.top1] = value
        elif stack_number == 2:
            self.top2 -= 1
            self.data[self.top2] = value
        else:
            raise Exception('illegal stack Number')

    def pop(self, stack_number):
        if stack_number == 1:
            if self.top1 == -1:
                raise Exception('stack1 is empty')
            result = self.data[self.top1]
            self.top1 -= 1
            return result
        elif stack_number == 2:
            if self.top2 == self.max_size:
                raise Exception('stack2 is empty')
            result = self.data[self.top2]
            self.top2 += 1
            return result
        else:
            raise Exception('illegal stack number')

    def __str__(self):
        return str(self.data)


class StackNode(object):
    def __init__(self, value, next=None):
        super().__init__()
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    __repr__ = __str__


class LinkedStack(object):
    """Stack 链式存储结构

    头结点 和 top 指针合二为一

    时间复杂度同顺序存储, 每个元保存一个指针, 更占空间, 但是栈长度可无限增长
    """

    def __init__(self):
        super().__init__()
        self.top = None
        self.size = 0

    def push(self, value):
        node = StackNode(value, self.top)
        self.top = node
        self.size += 1

    def pop(self):
        result = self.top
        self.top = self.top.next
        self.size -= 1
        return result

    def __str__(self):
        result = '{'
        current = self.top
        if current == None:
            return result + '}'
        while current != None:
            result += current.value + ', '
            current = current.next
        return result[:-2] + '}'
    
    __repr__ = __str__

