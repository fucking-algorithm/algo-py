"""回溯算法"""


def permute(nums: tuple) -> list:
    """全排列
    给定 n 个不同的数字, 有几个全排列
    """
    res = []  # 记录所有路径

    def backtrace(nums: tuple, trace: list):
        """回溯函数
        trace - 代表一条可行的路径
        nums - 给定的数组
        """
        if len(trace) == len(nums):
            res.append(list(trace))
            return
        for num in nums:
            if num in trace:
                continue

            trace.append(num)

            # 进入下层决策树
            backtrace(nums, trace)

            trace.pop()  # 默认移除末尾

    backtrace(nums, [])

    return res


def sub_collection(nums: tuple) -> list:
    """子集
    输入一个数组，要求算法输出这些数字的所有子集 (数组不包含重复数字)
    """
    result = []

    def back_trace(nums: tuple, start: int, sub_set: list):  # start 参数用来排除已经选择过的数字
        # 一定要重新构造一个 list 让如 result, 否则公用同一个 引用最后都会被移除, 类似 [[], [], [], []]
        result.append(list(sub_set))
        for i in range(start, len(nums)):
            sub_set.append(nums[i])
            back_trace(nums, i+1, sub_set)
            sub_set.pop()

    back_trace(nums, 0, [])
    return result


def compbine(end: int, count: int) -> list:
    """组合
    输入两个数字 n, k，算法输出 [1..n] 中 k 个数字的所有组合
    """
    result = []
    if end <= 0 or count <= 0:
        return result

    def back_trace(end: int, count: int, start: int, track: list):
        if count == len(track):
            result.append(list(track))
            return
        for num in range(start, end + 1):
            track.append(num)
            back_trace(end, count, start+1, track)
            track.pop()
    back_trace(end, count, 1, [])
    return result


class Board(object):
    def __init__(self, n):
        self.n = n
        self.content = []
        for r in range(n):
            row_value = []
            for c in range(n):
                row_value.append("*")
            self.content.append(row_value)

    def display(self):
        for row in self.content:
            print("".join(row))


def n_queens(n: int) -> Board:
    """n 皇后问题
    一个 N×N 的棋盘，让你放置 N 个皇后，使得它们不能互相攻击 (即任何 Q都不能再同一条横线, 竖线, 斜线上)
    """
    result = Board(n)

    def back_trace(row: int, b: Board):
        if row == b.n:
            # TODO
            return

    back_trace(0, result)
    return result


def sudoku(n: int):
    """数独问题
    数字 1-9 在每一行/每一列/只能出现一次
    每一个以粗实线分隔的 3x3 宫内只能出现一次。
    """
    pass


def test_n_queens():
    n_queens(3)


def test_permute():
    result = permute((1, 2, 3))
    print(str(result))


def test_sub_collection():
    result = sub_collection((1, 2, 3))
    print(result)


if __name__ == "__main__":
    test_n_queens()
