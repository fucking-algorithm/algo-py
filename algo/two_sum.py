"""两数之和"""

def two_sum_double_pointer(sorted_nums: tuple, target: int) -> tuple:
    """
    返回两个下标, 元素和为 target
    
    对于有序的数组, 首选双指针
    """
    left = 0
    right = len(sorted_nums) - 1
    while left < right:
        left_plus_right = sorted_nums[left] + sorted_nums[right]
        if left_plus_right == target:
            return (left, right)
        elif left_plus_right < target:
            left+=1
        elif left_plus_right > target:
            right -= 1
    return (-1, -1)


def hashtable_backup(nums: tuple, target: int) -> tuple:
    """
    如果是无序的数组, 就无法使用双指针了

    这时最简单的是双层循环暴力枚举, O(n^2)

    加上一个 hashmap做索引可以降低复杂度 O(n)
    """
    # put all of nums into map, 元素作为索引, 下标作为 值
    index_map = {}
    for k, v in enumerate(nums):
        index_map[v] = k

    for i in range(len(nums)):
        two = target - nums[i]
        if index_map.__contains__(two) and index_map.get(two) != i:
            return (i, index_map.get(two))
    return (-1, -1)

def test_two_sum_double_pointer():
    result = two_sum_double_pointer((1, 3,3,6), 6)
    print(result)


def test_hashtable_backup():
    result = hashtable_backup((1, 3,3,6), 6)
    print(result)


if __name__ == "__main__":
    test_two_sum_double_pointer()
    test_hashtable_backup()

