"""
给你一个大小为 m x n 的二元矩阵 grid ，矩阵中每个元素的值为 0 或 1 。

一次 移动 是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的 得分 就是这些数字的总和。

在执行任意次 移动 后（含 0 次），返回可能的最高分数。



示例 1：


输入：grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
示例 2：

输入：grid = [[0]]
输出：1


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] 为 0 或 1
"""
from typing import List


# 贪心：我们总可以先考虑所有的行翻转，再考虑所有的列翻转
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        # 1.为了得到最高的分数，矩阵的每一行的最左边的数都必须为 1
        # 2.将每一行的最左边的数都变为 1 之后，就只能进行列翻转了
        # 实际编写代码时，我们无需修改原矩阵，而是可以计算每一列对总分数的「贡献」
        ans = m * (1 << (n - 1))
        for j in range(1, n):
            cnt_1 = 0
            for i in range(m):
                if grid[i][0] == 1:
                    cnt_1 += grid[i][j]
                else:
                    cnt_1 += (1 - grid[i][j])  # 行需要翻转
            # 考虑列翻转
            k = max(cnt_1, m - cnt_1)
            ans += k * (1 << (n - j - 1))

        return ans
