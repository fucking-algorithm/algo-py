"""树
存储结构:

- 顺序存储 
    - 单独使用没办法表示一棵树, 需要和 链式存储合作使用
    - 例外: 二叉树可以通过数组存储, 依次存入即可; 如果不是完全二叉树(自顶向下, 从左到右, 没有空位), 空的位置在数组中存为空即可, 所以一般只用于完全二叉树
- 链式存储

表示法:

- parent 表示法 - 每个节点包含value 和它的parent节点指针, Node1, Tree1
- child 表示法 - 每个节点依次存入一个数组, 每个数组元素延伸出一个 child 链表, 链表中的元素都是数组元素的 child (不是 grandchild)
- child  sibling 表示法 - 每个 node 包含2 个指针 (first_child, right_sibling), 将一颗复杂树转变为 二叉树
"""

########## parent 表示法 ###############


class Node1(object):
    def __init__(self, value, parent):
        super().__init__()
        self.value = value
        self.parent = parent

    def __str__(self):
        return self.value

    __repr__ = __str__


class Tree1(object):
    def __init__(self, root_index, node_count, max_size=10):
        super().__init__()
        self.root_index = root_index  # 根节点位置
        self.node_count = node_count  # 节点数
        self.data = [None] * max_size  # 节点数组

###################### child 表示法 ###################


class ChildLinkedNode(object):
    def __init__(self, index, next=None):
        super().__init__()
        self.index = index  # 数组中的下标
        self.next = next


class HeadArrayNode(object):
    def __init__(self, value, first_child=ChildLinkedNode(None)):
        super().__init__()
        self.value = value  # 存储每个node 的数据
        self.first_child = first_child  # child 链表的头指针


class Tree2(object):
    def __init__(self, max_size):
        super().__init__()
        self.data = [HeadArrayNode] * max_size
        self.root_index = 0  # 树的根节点在数组中的下标
        self.node_count = 3  # 节点数


####################

class Node3(object):
    def __init__(self, value, first_child=None, right_sibling=None):
        super().__init__()


class Tree3(object):
    pass


###################### 二叉树的遍历 ################

class BSNode(object):
    def __init__(self, value, left=None, right=None):
        super().__init__()
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
    def __init__(self, root=BSNode(None)):
        super().__init__()
        self.root = root

    def traverse_pre_order(self, node=BSNode(None)):
        """前序遍历"""
        if node == None:
            return
        if node.value == None:
            return
        print(node.value)
        self.traverse_pre_order(node.left)
        self.traverse_pre_order(node.right)

    def traverse_middle(self, node):
        if node == None or node.value == None:
            return
        self.traverse_middle(node.left)
        print(node.value)
        self.traverse_middle(node.right)

    def traverse_post_order(self, node):
        if node == None or node.value == None:
            return
        self.traverse_post_order(node.left)
        self.traverse_post_order(node.right)
        print(node.value)


def test_binary_search():
    node = BSNode('a')
    node.left = BSNode('b', BSNode('d'))
    node.right = BSNode('c')
    bs_tree = BinarySearchTree(node)
    print('------ pre order --------')
    bs_tree.traverse_pre_order(bs_tree.root)
    print('------middle order---------')
    bs_tree.traverse_middle(bs_tree.root)
    print('--------post order---------')
    bs_tree.traverse_post_order(bs_tree.root)


if __name__ == "__main__":
    test_binary_search()
