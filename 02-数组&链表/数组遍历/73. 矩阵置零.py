"""
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。
请使用 原地 算法。

示例 1：
输入：matrix = [[1,1,1],
               [1,0,1],
               [1,1,1]]
输出：[[1,0,1],
      [0,0,0],
      [1,0,1]]

示例 2：
输入：matrix = [[0,1,2,0],
               [3,4,5,2],
               [1,3,1,5]]
输出：[[0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]]

提示：
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

进阶：
一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？
"""
from typing import List


# 方法一：用两个标记数组分别记录每一行和每一列是否有零出现。
# 使用  O(m+n) 的额外空间
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row, col = [False] * m, [False] * n

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True

        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        print(matrix)


# 方法二：使用两个集合（Set）来记录需要置零的行和列的索引
# 使用 O(m + n) 的额外空间
class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        rows_set = set()
        cols_set = set()

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    rows_set.add(i)
                    cols_set.add(j)

        for i in range(rows):
            for j in range(cols):
                if i in rows_set or j in cols_set:
                    matrix[i][j] = 0
        print(matrix)

