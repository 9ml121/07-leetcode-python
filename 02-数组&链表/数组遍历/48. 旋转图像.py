"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。
请不要 使用另一个矩阵来旋转图像。

示例 1：
输入：matrix = [[1,2,3],
               [4,5,6],
               [7,8,9]]

输出：[[7,4,1],
      [8,5,2],
      [9,6,3]]


示例 2：
输入：matrix = [[5 , 1 , 9 , 11],
               [2 , 4 , 8 , 10],
               [13, 3 , 6 , 7 ],
               [15, 14, 12, 16]]

输出：[[15, 13, 2,  5],
      [14, 3,  4,  1],
      [12, 6,  8,  9],
      [16, 7,  10, 11]]


提示：
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List


# 方法1：先将 n x n 矩阵 matrix 按照左上到右下的对角线进行镜像对称，再对矩阵的每一行进行反转
# 参考：https://labuladong.github.io/algo/di-yi-zhan-da78c/shou-ba-sh-48c1d/er-wei-shu-150fb/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 先沿对角线镜像对称二维矩阵
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 然后反转二维矩阵的每一行
        for rows in matrix:
            # rows.reverse()  # 下面代码是自己实现列表的 reverse()函数
            left, right = 0, n - 1
            while left < right:
                rows[left], rows[right] =  rows[right], rows[left]
                left += 1
                right -= 1


# 方法2：使用辅助矩阵
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # 创建一个新的 n × n 辅助矩阵，用于存储旋转后的图像。
        rotate_matrix = [[0] * n for _ in range(n)]

        # 遍历原始图像矩阵，将每个元素旋转到辅助矩阵的对应位置。
        for i in range(n):
            for j in range(n):
                rotate_matrix[j][n - 1 - i] = matrix[i][j]

        # 不能写成 matrix = rotate_matrix
        matrix[:] = rotate_matrix


# 方法3：原地旋转
# 对于每个元素 matrix[i][j]，将其旋转到 matrix[j][n-1-i] 的位置，即原始矩阵中的第 i 行第 j 列元素旋转到第 j 行第 n-i-1 列。
class Solution3:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 通过循环遍历矩阵中的每个元素，完成原地旋转。
        # 注意循环的范围是 i < n // 2 和 j < (n + 1) // 2，以确保只旋转矩阵的一半
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                # 需要使用一个临时变量 temp 来保存旋转过程中的元素。
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = tmp


if __name__ == '__main__':
    matrix = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]

    # Solution().rotate(matrix)
    Solution2().rotate(matrix)
    print(matrix)

    # 输出：[[15, 13, 2, 5],
    #       [14, 3, 4, 1],
    #       [12, 6, 8, 9],
    #       [16, 7, 10, 11]]
