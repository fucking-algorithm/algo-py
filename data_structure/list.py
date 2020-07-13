#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""线性表 链式存储结构"""

class Node(object):
    """
    单向链表节点
    """

    def __init__(self, value, next=None):
        super().__init__()
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    __repr__ = __str__



class LinkedList(object):
    """单向链表

    [root] -> [node0] -> [node1] -> [node2]

    静态链表: 借助数组实现, 每个 位置存放 data 和 cur, cur 是下一个元素的下标
    第一个元素和最后一个元素做为特殊元素, 不存 data, 只存放 cur
    - 第一个元素: cur 为数组的空闲位置起点下标
    - 最后一个元素: cur 为第一个有 data 的元素下标(头结点)

    循环链表: tail node 的next 指向 第一个 node; 使用尾指针(rear node) 而不使用头指针

    双向链表: 每个node有两个指针(prior, next), 空间换时间
    """

    def __init__(self, head=Node(None, None)):
        super().__init__()
        self.head = head
        self.length = 0

    def get(self, index):
        """get node by index
        
        index = 0, then return head node

        O(n)
        """
        result = self.head
        i = 1
        if index > self.length:
            raise Exception('Index cannot bigger than length, length = %s' % self.length)
        if index == 0:
            return result
        while(i <= index):
            result = result.next
            i += 1
        return result

    def append(self, value):
        """append to tail
        
        O(1)
        """
        tail = self.get(self.length)
        tail.next = Node(value)
        self.length += 1

    def insert(self, index, value):
        """O(n)"""

        if index == 0:
            raise Exception('When you insert, index have to bigger than 0.')
        p = self.get(index - 1)
        node = Node(value, p.next)
        node.next = p.next
        p.next = node  # 一定要在最后一步
        self.length += 1

    def pop(self, index):
        """O(n)"""

        p = self.get(index - 1)
        target = p.next
        p.next = target.next
        return target

    def remove(self, value):
        """O(2n)"""

        index = 0
        current = self.head
        while current != None:
            current = current.next
            index += 1
            if current.value == value:
                break
        if index == 0:
            raise Exception('value = %s doesn\'t exist in this list' % value)
        p = self.get(index - 1)
        p.next = p.next.next
    
    def __str__(self):
        result = '{'
        current = self.head
        while current.next != None:
            current = current.next
            result += str(current.value) + ', '
        return result[:-2] + '}'

    __repr__ = __str__


