"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：
输入：matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],
               [5,6,7,8],
               [9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]


提示：
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List


# 螺旋遍历矩阵的一种常见方法是按层遍历。
# 我们可以定义上下左右四个边界，然后逐层遍历矩阵。
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])

        # 初始化上下左右四个边界
        left, right = 0, cols - 1
        top, bottom = 0, rows - 1
        ans = []

        # 按照顺时针的顺序遍历矩阵的每一层
        while left <= right and top <= bottom:
            # 遍历上边界
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # 遍历右边界
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # 遍历下边界
            if top <= bottom:  # 只剩一行，就不用遍历下边界了
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # 遍历左边界
            if left <= right:  # 只剩一列，就不用遍历左边界了
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans
