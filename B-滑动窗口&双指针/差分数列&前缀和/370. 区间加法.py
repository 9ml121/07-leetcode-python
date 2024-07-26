"""
假设你有一个长度为 n 的数组，初始情况下所有的数字均为 0，你将会被给出 k​​​​​​​ 个更新的操作。
其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组 A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加 inc。
请你返回 k 次操作后的数组。

示例:
输入: n = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
输出: [-2,0,3,5,3]
解释:

初始状态:
[0,0,0,0,0]

进行了操作 [1,3,2] 后的状态:
[0,2,2,2,0]

进行了操作 [2,4,3] 后的状态:
[0,2,5,5,3]

进行了操作 [0,2,-2] 后的状态:
[-2,0,3,5,3]
"""
from typing import List

# todo 前缀和思想（差分数组）
# 类似：B-滑动窗口&双指针\差分数列&前缀和\1109. 航班预订统计.py

class DiffArr:
    # 构建差分数组
    def __init__(self, nums: list):
        self.n = len(nums)
        self.diffs = [0] * self.n
        # 根据初始数组构造差分数组
        self.diffs[0] = nums[0]
        for i in range(1, self.n):
            self.diffs[i] = nums[i] - nums[i - 1]

    #  给闭区间 [i, j] 增加 inc（可以是负数）
    def update(self, i, j, inc):
        self.diffs[i] += inc
        # 当 j+1 >= diff.n 时，说明是对 nums[i] 及以后的整个数组都进行修改，那么就不需要再给 diff 数组减 value 了。
        if j + 1 < self.n:
            self.diffs[j + 1] -= inc

    # 返回更新后的结果数组
    def result(self):
        # 根据差分数组构造结果数组
        res = [0] * self.n
        res[0] = self.diffs[0]
        for i in range(1, self.n):
            res[i] = res[i - 1] + self.diffs[i]
        return res


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # arr 初始化为全 0
        arr = [0] * length
        # 构造差分解法
        diffArr = DiffArr(arr)

        for i, j, inc in updates:
            diffArr.update(i, j, inc)

        return diffArr.result()


if __name__ == '__main__':
    cls = Solution()
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    # [-2,0,3,5,3]
    print(cls.getModifiedArray(length, updates))
