"""
给定 m 个数组，每个数组都已经按照升序排好序了。现在你需要从两个不同的数组中选择两个整数（每个数组选一个）并且计算它们的距离。两个整数 a 和 b 之间的距离定义为它们差的绝对值 |a-b| 。你的任务就是去找到最大距离

示例 1：

输入：
[[1,2,3],
 [4,5],
 [1,2,3]]
输出： 4
解释：
一种得到答案 4 的方法是从第一个数组或者第三个数组中选择 1，同时从第二个数组中选择 5 。


注意：

每个给定数组至少会有 1 个数字。列表中至少有两个非空数组。
所有 m 个数组中的数字总数目在范围 [2, 10000] 内。
m 个数组中所有整数的范围在 [-10000, 10000] 内。
"""
from typing import List


# 考察点：贪心
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1 = min2 = float('inf')
        max1 = max2 = float('-inf')
        idx1 = idx2 = -1
        for i, arr in enumerate(arrays):
            if arr:
                small, big = arr[0], arr[-1]
                if small < min1:
                    min2 = min1
                    min1 = small
                    idx1 = i
                elif small < min2:
                    min2 = small

                if big > max1:
                    max2 = max1
                    max1 = big
                    idx2 = i
                elif big > max2:
                    max2 = big

        if idx1 != idx2:
            return abs(max1 - min1)
        else:
            return max(abs(max1 - min2), abs(max2 - min1))


if __name__ == '__main__':
    pass
