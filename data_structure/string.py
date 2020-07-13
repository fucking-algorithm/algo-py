"""string
有限的字符序列, 类似线性表, 更关注匹配, 替换等操作

- 顺序存储 - 通过数组实现, 第一个元素存储串长度
- 链式存储 - 为了节省空间, 每个 node 可能存储多个字符, 若未被占满, 用 '#' 填充 (concat 操作十分方便, 但总体不如 顺序存储灵活)

string 的匹配算法:

- 朴素模式匹配算法 - 太低效
- kmp模式匹配算法

todo
"""


class String(object):
    def __init__(self, value):
        super().__init__()
        # 首位存储串长度
        self.data = list(str(len(value)) + value)

    def index(self, sub_str, pos=1):
        """朴素模式匹配算法"""

        i = pos  # 主串指针
        j = 1  # 子串指针
        while (i <= int(self.data[0])) and (j <= int(sub_str.data[0])):
            if self.data[i] == sub_str.data[j]:
                i += 1
                j += 1
            else:
                i = i - j + 2  # 主串到下一位
                j = 1  # 子串回到首位
        if j > int(sub_str.data[0]):
            return i - int(sub_str.data[0]) - 1
        else:
            return -1

    def __str__(self):
        # 字符数组转string
        return ''.join(self.data[1:])

    __repr__ = __str__
