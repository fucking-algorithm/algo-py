"""缓存淘汰算法 lru 
最近最少使用

为什么需要 哈希表? - 因为需要满足查找快的要求

为什么必须要用双向链表? - 因为我们需要删除操作。删除一个节点不光要得到该节点本身的指针，也需要操作其前驱节点的指针

为什么要在链表中同时存储 key 和 val，而不是只存储 val? - 往缓存添加, 需要 check cap, 如果达到 cap, 需要 找到 link 的 last item, 删除, 同时
根据 key 删除 map 中的 pair
"""

class Node(object):
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    # remove 指定 node 时会用到 (判断找到的 node 是否是 指定 node)
    def __eq__(self, n):
        if not isinstance(n, Node):
            return False
        if self.key == n.key:
            return True
        else: 
            return False

class DoubleList(object):
    def __init__(self):
        self.head = Node()
        self.count = 0

    def add_first(self, n: Node):
        n.next = self.head.next
        self.head.next = n
        self.count += 1
    
    def remove(self, n: Node):
        cur = self.head
        while cur != n:
            cur = cur.next
        
        p_node: Node = cur.prev
        s_node: Node = cur.next

        p_node.next = s_node
        s_node.prev = p_node

        self.count -= 1

    def remove_last(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.prev.next = None
        cur.prev = None
        return cur

    def size(self):
        return self.count
                

class LruCache(object):
    def __init__(self, cap: int):
        self.map = {}
        self.dl = DoubleList()
        self.cap = cap

    def get(self, key):
        v = self.map.get(key, None)
        if v:
            # 提升到 head
            self.dl.remove(v)
            self.dl.add_first(v)
        return v

    def put(self, key, value):
        to_save = Node(key, value)
        v = self.map.get(key, None)
        # if exist in map, then update
        if v:
            self.dl.remove(v)
            self.dl.add_first(to_save)

            self.map[key] = value
        # if not exist in map, then add
        else:
            # check
            if self.dl.size() == self.cap:
                last: Node = self.dl.remove_last()
                self.map.pop(last.key)

            x = Node(key, value)
            old_next: Node = self.dl.head.next

            self.dl.head.next = x
            x.prev = self.dl.head
            x.next = old_next
            if old_next:
                old_next.prev = x

            self.map[key] = value    

    def display(self):
        s = []
        cur = self.dl.head
        while cur.next != None:
            cur = cur.next
            s.append("({}, {}) -> ".format(cur.key, cur.value))
        print("".join(s)[:-3])


if __name__ == "__main__":
    lru = LruCache(3)
    lru.put("a", "aa")
    lru.put("b", "bb")
    lru.put("c", "CC")
    lru.display()
    a = lru.get("a")
    print(a)
    lru.display()
