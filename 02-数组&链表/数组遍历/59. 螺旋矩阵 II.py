"""
给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
输入：n = 3
输出：[[1,2,3],
      [8,9,4],
      [7,6,5]]

示例 2：
输入：n = 1
输出：[[1]]


提示：
1 <= n <= 20
"""
from typing import List


# 在54题基础上稍微改动一下
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        # 初始化上下左右四个边界
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        # 需要填入矩阵的数字
        num = 1

        # 按照顺时针的顺序遍历矩阵的每一层
        # while left <= right and top <= bottom:
        while num <= n ** 2:
            # 遍历上边界
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # 遍历右边界
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # 遍历下边界
            if top <= bottom:  # 只剩一行，就不用遍历下边界了
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1

            # 遍历左边界
            if left <= right:  # 只剩一列，就不用遍历左边界了
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1

        return matrix
