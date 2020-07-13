"""双指针"""


class Node(object):
    def __init__(self, v=None, next=None):
        super().__init__()
        self.v = v
        self.next = next
    def __str__(self):
        result = str(self.v)
        while self.next != None:
            result += "->" + self.next.v
        return result
    # def __eq__(self, node):
    #     if self.v == node.v:
    #         return True
    #     else: return False

def has_cycle(node: Node) -> bool:
    """是否成环"""
    fast = slow = node
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False


def cycle_start(node: Node) -> Node:
    """环起点"""
    fast = slow = node
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            break
    # 任意指针重新回到 head
    slow = node
    while slow != fast:
        # 速度变为一样
        slow = slow.next
        fast = fast.next
    # 再次相遇即为环起点    
    return slow


def link_middle(node: Node):
    """链表中点
    当快指针到达链表尽头时，慢指针就处于链表的中间位置。
    当链表的长度是奇数时，slow 恰巧停在中点位置；如果长度是偶数，slow 最终的位置是中间偏右：

    找到中点的重要作用是对链表进行归并排序。

    """
    fast = slow = node
    while fast != None and fast.next != Node:
        fast = fast.next.next
        slow = slow.next
    return slow


def reverse_k(node:Node, k: int):
    """
    寻找链表的倒数第 k 个元素
    """
    fast = slow = node
    for i in range(k):
        fast = fast.next
    while fast != None:
        fast = fast.next
        slow = slow.next
    return slow


def binary_search(nums: tuple, target: int) -> int:
    """二分查找
    也是双指针的应用
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left +  (right - left) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
    return -1




def reverse_arr(nums: tuple) -> tuple:
    """翻转数组"""
    result = tuple(nums)
    left = 0
    right = len(result) - 1

    while left < right:
        tmp = result[left]
        result[left] = result[right]
        result[right] = tmp

        left += 1
        right -= 1

    return result

def test_has_cycle():
    n1 = Node("1")
    n2 = Node("2")
    n3 = Node("3")
    n4 = Node("4")
    n5 = Node("5")
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    n5.next = n3

    cycle = has_cycle(n1)
    print(cycle)

    node = cycle_start(n1)
    print(node.v)


if __name__ == "__main__":
    test_has_cycle()