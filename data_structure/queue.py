"""队列

本质还是 线性表, 只能在一端插入, 另一端删除

场景: 

- 键盘输入, 屏幕输出
- 排队
"""

class Queue(object):
    """顺序存储结构
    
    循环队列:
    为了提高空间利用率, 避免 "假溢出"(头部有位置, 尾巴空间不够), 使用 循环队列

    """

    def __init__(self, max_size=10):
        super().__init__()
        self.max_size = max_size
        self.data = [None] * max_size
        self.front = 0
        self.rear = 0 # 为什么要使用头尾双指针? 为了避免队头队尾重合使得处理变得麻烦

    def enQueue(self, value):
        # 判断是否满了, rear 加1 (如果超出末尾, 则转到开头) 是否等于 front
        if ((self.rear + 1) % self.max_size) == self.front:
            raise Exception('Queue fulled.')
        self.data[self.rear] = value
        # rear 向后移动一位, 如果超出则转到数组头部
        self.rear  = (self.rear + 1) % self.max_size

    def deQueue(self):
        if self.front == self.rear:
            raise Exception('Queue empty')
        result = self.data[self.front]
        self.front = (self.front + 1) % self.max_size
        return result

    def size(self):
        # 分为 1. front < rear 和 2. front>rear 两种情况
        # 对于1: rear -front
        # 对于2: front - rear + max_size
        # 综合下, 就是下面的这个公式
        return (self.rear - self.front + self.max_size) % self.max_size

class Node(object):
    """Queue node 链式存储"""

    def __init__(self, value, next=Node(None, None)):
        super().__init__()
        self.value = value
        self.next = next
    
    def __str__(self):
        return self.value

    __repr__ = __str__


class LinkedQueue(object):
    #todo
    pass