"""
现有一个记作二维矩阵 frame 的珠宝架，其中 frame[i][j] 为该位置珠宝的价值。拿取珠宝的规则为：

只能从架子的左上角开始拿珠宝
每次可以移动到右侧或下侧的相邻位置
到达珠宝架子的右下角时，停止拿取
注意：珠宝的价值都是大于 0 的。除非这个架子上没有任何珠宝，比如 frame = [[0]]。

 

示例 1:

输入: frame = [[1,3,1],[1,5,1],[4,2,1]]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最高价值的珠宝
 

提示：

0 < frame.length <= 200
0 < frame[0].length <= 200
"""


from functools import cache
from typing import List

# 方法 1：动态规划
class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        # 珠宝的价值都是>= 0, 每次可以移动到右侧或下侧的相邻位置, 计算可以拿到的最高价值
        m, n = len(frame), len(frame[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(frame):
            for j, x in enumerate(row):
                f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1]) + x
        return f[m][n]

# 方法 2：记忆化搜索
# 定义子问题为：从 (0,0) 到 (i,j) 可以得到的樱桃个数的最大值。
class Solution:
    def jewelleryValue(self, grid: List[List[int]]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            return max(dfs(i, j - 1), dfs(i - 1, j)) + grid[i][j]
        
        return dfs(len(grid) - 1, len(grid[0]) - 1)
