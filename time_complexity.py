"""时间复杂度 demo

O	名称	举例

1	常量时间	一次赋值
logn	对数时间	折半查找(一个算法能在每个步骤去掉一半数据元素，如二分检索)
n	线性时间	线性查找(遍历, 单层循环)
nlogn	对数线性时间	快速排序
n2	平方	两重循环
n3	立方	三重循环
2n	指数	递归求斐波那契数列
n!	阶乘	旅行商问题
"""

def logn_test(n):
    """T(n) = logn"""

    sum = 0
    i = 1
    while i <= n:
        sum += i
        i *= 2
    return sum

def n_test(n):
    """T(n) = n"""

    sum = 0
    for i in range(1, n+1, 1):
        sum += i
    return sum


def zhishu_test(n):
    for i in range(0, n, 1):
        for j in range():
            pass

if __name__ == "__main__":
    print('sub = %s' % n_test(3))


