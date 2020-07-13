"""前缀和

主要用于处理数组区间的问题
"""

def sub_sum(nums: tuple, target: int) -> list:
    """
    对于数组 nums, 有多少个连续的子数组, 满足子数组各个元素和为 target

    利用前缀和数组 O(n^2)

    """
    pre_sum = []
    pre_sum[0] = 0
    for i in range(len(nums)):
        pre_sum[i + 1] = pre_sum[i] + nums[i]

    ans = 0
    for i in range(1, len(nums) + 1):
        for j in range(i):
            if pre_sum[i] - pre_sum[j] == target:
                ans += 1
    return ans


def sub_sum_optimized(nums: tuple, target: int) -> int:
    """
    优化:
    """

