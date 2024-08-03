"""
给你一个大小为 3 * 3 ，下标从 0 开始的二维整数矩阵 grid ，分别表示每一个格子里石头的数目。网格图中总共恰好有 9 个石头，一个格子里可能会有 多个 石头。

每一次操作中，你可以将一个石头从它当前所在格子移动到一个至少有一条公共边的相邻格子。

请你返回每个格子恰好有一个石头的 最少移动次数 。

 

示例 1：



输入：grid = [[1,1,0],[1,1,1],[1,2,1]]
输出：3
解释：让每个格子都有一个石头的一个操作序列为：
1 - 将一个石头从格子 (2,1) 移动到 (2,2) 。
2 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
3 - 将一个石头从格子 (1,2) 移动到 (0,2) 。
总共需要 3 次操作让每个格子都有一个石头。
让每个格子都有一个石头的最少操作次数为 3 。
示例 2：



输入：grid = [[1,3,0],[1,0,0],[1,0,3]]
输出：4
解释：让每个格子都有一个石头的一个操作序列为：
1 - 将一个石头从格子 (0,1) 移动到 (0,2) 。
2 - 将一个石头从格子 (0,1) 移动到 (1,1) 。
3 - 将一个石头从格子 (2,2) 移动到 (1,2) 。
4 - 将一个石头从格子 (2,2) 移动到 (2,1) 。
总共需要 4 次操作让每个格子都有一个石头。
让每个格子都有一个石头的最少操作次数为 4 。
 

提示：

grid.length == grid[i].length == 3
0 <= grid[i][j] <= 9
grid 中元素之和为 9 。
"""

from functools import cache
from itertools import permutations
from math import inf
from typing import List

# 方法 1：枚举全排列


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # 由于所有移走的石子个数等于所有移入的石子个数（即 0 的个数），我们可以把移走的石子的坐标记录到列表 from 中（可能有重复的坐标），
        # 移入的石子的坐标记录到列表 to 中。
        # 这两个列表的长度是一样的。
        from_ = []
        to = []
        for i, row in enumerate(grid):
            for j, cnt in enumerate(row):
                if cnt > 1:
                    from_.extend([(i, j)] * (cnt - 1))
                elif cnt == 0:
                    to.append((i, j))

        ans = inf
        # 枚举 from 的所有排列，与 to 匹配，即累加从 from[i] 到 to[i] 的曼哈顿距离。
        # 所有距离之和的最小值就是答案。
        for from2 in permutations(from_):
            total = 0
            for (x1, y1), (x2, y2) in zip(from2, to):
                total += abs(x1 - x2) + abs(y1 - y2)
            ans = min(ans, total)
        return ans

# todo 方法 2：状态压缩 + 动态规划
# E-动态规划/状态DP/526. 优美的排列.py
# E-动态规划/状态DP/1947. 最大兼容性评分和.py

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        # 计算两个坐标的曼哈顿距离
        def cal(a: tuple, b: tuple) -> int:
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        # 把所有值为 0 的单元格坐标 (i,j) 放入数组 left 中
        # 如果单元格的值 v 大于 1，那么我们把 v−1 个坐标 (i,j) 放入数组 right 中
        # 问题就转化为，每个 right 中的坐标 (i,j) 都要移动到 left 中的一个坐标 (x,y)，求最少的移动次数。
        left, right = [], []
        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    left.append((i, j))
                else:
                    for _ in range(grid[i][j] - 1):
                        right.append((i, j))

        # 使用 n 位二进制数来表示 left 中的每个坐标是否被 right 中的坐标填充
        # 其中 1 表示被填充，而 0 表示未被填充
        n = len(left)
        f = [inf] * (1 << n)
        f[0] = 0
        # 考虑 f[i]，记当前 i 的二进制表示中 1 的个数为 k，
        # 我们在 [0..n) 的范围内枚举 j，如果 i 的第 j 位为 1，那么 f[i] 可以由 f[i⊕(1<<j)] 转移而来，转移的代价为 cal(left[k−1],right[j])
        for i in range(1, 1 << n):
            k = i.bit_count()
            for j in range(n):
                if i >> j & 1:
                    f[i] = min(f[i], f[i ^ (1 << j)] +
                               cal(left[k - 1], right[j]))
        return f[-1]
