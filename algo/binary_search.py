"""二分查找"""

def binary_search(nums: tuple, target: int) -> int:
    start = 0
    end = len(nums) - 1

    # 为什么循环的条件中是 <=，而不是 <
    # 因为 搜索区间是 [left, right], 而不是 [left, right), left 和 right 是可能相等的
    while start <= end:
        # 防止 start + end 直接相加太大造成溢出
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            end = mid - 1
        elif target > nums[mid]:
            start = mid + 1

    return -1


def left_bound(nums: tuple, target: int) -> int:
    """寻找左侧边界的二分搜索"""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if target == nums[mid]:
            right = mid - 1
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
    # 检查出界情况
    if left >= len(nums) or nums[left] != target:
        return -1    
    # 此时, left == right
    return left

def test_arr_sub():
    arr = (0, 1, 2, 3, 4)
    # 包头不包尾
    sub = arr[2:]
    print(sub)

def test_binary_search():
    result = binary_search((-50, -1, 0, 3, 4, 9, 33, 99), -1)
    print(result)


if __name__ == "__main__":
    test_binary_search()
    


