class BSNode(object):
    def __init__(self, value, left=None, right=None):
        super().__init__()
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        def resolve_node(node):
            if node == None:
                return 'None'
            if node.value == None:
                return 'None'
            return node.value
        return 'BSNode(value = {}, left = {}, right = {})'.format(self.value, resolve_node(self.left), resolve_node(self.right))

    __repr__ = __str__


class BinarySearchTree(object):
    def __init__(self, root=BSNode(None)):
        super().__init__()
        self.root = root

    def insert(self, value):
        current = self.root
        while True:
            # 保存 parent
            current_temp = current

            if current.value == value:
                raise Exception('value already exist')
            elif value < current.value:
                current = current.left
            else:
                current = current.right

            if current == None:
                current = current_temp
                break
        if value < current.value:
            current.left = BSNode(value)
        elif value > current.value:
            current.right = BSNode(value)
        else:
            raise Exception('value already exist')

    def search(self, node, value):
        if node == None:
            raise Exception('cannot find with null node')
        if node.value == value:
            return node
        elif value < node.value:
            self.search(node.left, value)
        else:
            self.search(node.right, value)

    def delete(self, value):
        pass

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


def test_binary_search_tree():
    # node = BSNode('a')
    # node.left = BSNode('b', BSNode('d'))
    # node.right = BSNode('c')
    # bs_tree = BinarySearchTree(node)

    bs_tree = BinarySearchTree(BSNode('a'))
    bs_tree.insert('c')
    bs_tree.insert('d')
    bs_tree.insert('b')

    print('------ pre order --------')
    bs_tree.traverse_pre_order(bs_tree.root)
    print('------middle order---------')
    bs_tree.traverse_middle(bs_tree.root)
    print('--------post order---------')
    bs_tree.traverse_post_order(bs_tree.root)

    print('----------------------------')

    result_node = bs_tree.search(bs_tree.root, 'c')
    print(result_node)


def test_string_compare():
    a = 'ab'
    b = 'b'
    assert (a < b) == True


if __name__ == "__main__":
    test_binary_search_tree()
    # test_string_compare()
