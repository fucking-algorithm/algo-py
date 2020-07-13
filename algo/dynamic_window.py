"""滑动窗口"""

def sub_str(source: str, target: str) -> str:
    """最小覆盖子串
    找出 source 中的包含 target 的最短子串
    如: adoegegbanc 中找 abc, 返回 banc
    """
    result = ""
    left = 0 # 区间 [left, right] 为窗口, 初始窗口大小为 right - left = 0
    right = 0
    while right <= len(source):
        # 若 right 符合要求, 转而增加 left ,缩小 window
        if contain_sub(source[left:right], target):
            # 开始移动 left, 直到 source[left:right]不符合要求
            while left < right:
                if not contain_sub(source[left:right], target):
                    tmp = source[left-1:right]
                    print("--- tmp = " + tmp)
                    if len(result) == 0 or len(tmp) < len(result):
                        result = tmp
                        break
                # left 不断右边移动
                left += 1

        # right 不断右边移动
        right += 1
    return result

def contain_sub(s: str, t: str) -> bool:
    """s 中是否包含 t 中的每个字符"""
    for c in t:
        if c not in s:
            return False
    return True


def test_sub_str():
    result = sub_str("adoegegbanc", "abc")
    print(result)


if __name__ == "__main__":
    test_sub_str()
