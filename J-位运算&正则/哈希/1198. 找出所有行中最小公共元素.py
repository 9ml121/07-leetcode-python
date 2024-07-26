"""
给你一个 m x n 的矩阵 mat，其中每一行的元素均符合 严格递增 。请返回 所有行中的 最小公共元素 。

如果矩阵中没有这样的公共元素，就请返回 -1。



示例 1：

输入：mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
输出：5
示例 2:

输入：mat = [[1,2,3],[2,3,4],[2,3,5]]
输出： 2


提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 500
1 <= mat[i][j] <= 104
mat[i] 已按严格递增顺序排列。
"""
import collections
from typing import List


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])

        if rows == 1:
            return -1

        cnts = collections.defaultdict(int)

        for j in range(cols):
            for i in range(rows):
                cnts[mat[i][j]] += 1

                if cnts[mat[i][j]] == rows:
                    return mat[i][j]
        return -1
