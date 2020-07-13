"""动态规划
动态规划问题的一般形式就是把所有可行的答案穷举出来，然后在其中找最值

存在「重叠子问题」，如果暴力穷举的话效率会极其低下，所以需要「备忘录」或者「DP table」来优化穷举过程，避免不必要的计算


"""


import datetime
import time


def fib_raw(n: int) -> int:
    """斐波那契数列

    原始的暴力递归写法, 

    画出递归树, 发现有很多重复的子问题

    时间复杂度: 子问题个数乘以解决一个子问题需要的时间, 解决一个子问题的时间，在本算法中，没有循环，只有 f(n - 1) + f(n - 2) 一
    个加法操作，时间为 O(1), 子问题个数，即递归树中节点的总数。显然二叉树节点总数为指数级别，所以子问题个数为 O(2^n)
    总体复杂度:  O(2^n)
    """
    assert n >= 0, ">>> params illigal: n >= 0"
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_raw(n - 1) + fib_raw(n - 2)


def fib_memo(n: int) -> int:
    """
    带备忘录的递归写法

    复杂度: 子问题个数为 O(n) * 一个子问题时间为 O(1) = O(n)
    """
    memo = [0] * (n + 1)  # 初始化为 0
    if memo[n] != 0:  # 不为零, 表示已经计算过了, 可以直接返回
        return memo[n]

    fib = fib_raw(n)

    memo.insert(n, fib)

    return fib


def test_list():
    a = ["1"] * 3
    b = ["1" * 3]
    print(a)
    print(b)

    # ['1', '1', '1']
    # ['111']


def fib_dp_table(n: int) -> int:
    """
    dp table 的写法, O(n)
    """
    dp = [0] * (n + 1)
    dp.insert(1, 1)
    dp.insert(2, 1)
    for i in range(3, len(dp)):
        dp.insert(i, dp[i - 1] + dp[i - 2])
    return dp[n]


def egg_dp(egg_count: int, floor_height: int) -> int:
    """扔鸡蛋问题
    有一栋从 1 到 N 共 N 层的楼，然后给你 K 个鸡蛋（K 至少为 1）。现在确定这栋楼存在楼层 0 <= F <= N，
    在这层楼将鸡蛋扔下去，鸡蛋恰好没摔碎. 最坏情况下，你至少要扔几次鸡蛋，才能确定这个楼层 F 
    """
    pass


def coin_change(coins: list, amount: int):
    """凑硬币问题
    给你 k 种面值的硬币，面值分别为 c1, c2 ... ck，每种硬币的数量无限，再给
    一个总金额 amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1

    比如说 k = 3，面值分别为 1，2，5，总金额 amount = 11。那么最少需要 3 枚硬币凑出，即 11 = 5 + 5 + 1。


    """
    def dp(n):
        # base case
        if n == 0:
            return 0
        if n < 0:
            return -1
        # 求最小值，所以初始化为正无穷
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1:
                continue
            res = min(res, 1 + subproblem)
        return res if res != float('INF') else -1
    return dp(amount)


###########################
#        test
###########################

def test_fib():
    n = 30

    t1 = datetime.datetime.now()
    fib = fib_raw(n)
    t2 = datetime.datetime.now()
    print(">>> fib = {}, time: {} ms".format(
        fib, (t2 - t1).microseconds / 1000))

    t3 = datetime.datetime.now()
    fibmemo = fib_memo(n)
    t4 = datetime.datetime.now()
    print(">>> fibmemo = {}, time: {} ms".format(
        fibmemo, (t4 - t3).microseconds / 1000))

    t5 = datetime.datetime.now()
    fib_dp = fib_dp_table(n)
    t6 = datetime.datetime.now()
    print(">>> fib_dp = {}, time: {} ms".format(
        fib_dp, (t6 - t5).microseconds / 1000))


def test_coinChange():
    result = coin_change((1, 2, 5), 11)
    print(">>> " + str(result))


if __name__ == "__main__":
    test_fib()
