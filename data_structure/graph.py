"""图
存储结构:

- 顺序存储显然不可能
- 链式存储不方便(比如如果各个顶点的 degree 相差巨大, 那么以 degree最大的顶点的degree 为准设计结构会造成空间浪费)
- 最终选用: 一个一维数组保存 vertex(顶点), 一个二维数组 arc[i][j](矩阵)保存边/弧

邻接矩阵:

- 主对角线都为 0 (因为没有自己到自己的边)
- 对于无向图, 有边, 则为 1, 没边则为 0
- 无向图的 arc[i][j] 是一个对称矩阵
- 对于有向图, 没弧为 正无穷(为了和权值为0区别开), 有弧为1或权值

对于稀疏图(边/弧 相对于顶点来说极少的图), 邻接矩阵有巨大的空间浪费

邻接表: 数组和链表结合, 一个数组依次存入所有顶点, 每个元素延伸出一个链表, 链表元素是该顶点所有邻接点
(就是 树结构中的 child 表示法)

但是对于有向图, 邻接表只能反映每个顶点的出度, 了解入度则要遍历整个图; 
反之, 逆邻接表只能反映入度, 没法了解出度

十字链表:
todo

"""

class EdgeNode(object):
    def __init__(self, index, weight=1, next=EdgeNode(None)):
        super().__init__()
        self.index = index
        self.weight = weight
        self.next = next


class VertexNode(object):
    def __init__(self, data, first_edge=EdgeNode(None)):
        super().__init__()
        self.data = data
        self.first_edge = first_edge


class Graph(object):
    def __init__(self, num_vertex, num_edge, max_size=10):
        super().__init__()
        self.num_vertex = num_vertex
        self.num_edge = num_edge
        self.max_size = max_size
        self.vertex_node_list = [None] * max_size

####################
