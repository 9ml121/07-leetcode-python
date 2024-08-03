"""
厨房里总共有 n 个橘子，你决定每一天选择如下方式之一吃这些橘子：

吃掉一个橘子。
如果剩余橘子数 n 能被 2 整除，那么你可以吃掉 n/2 个橘子。
如果剩余橘子数 n 能被 3 整除，那么你可以吃掉 2*(n/3) 个橘子。
每天你只能从以上 3 种方案中选择一种方案。

请你返回吃掉所有 n 个橘子的最少天数。



示例 1：
输入：n = 10
输出：4
解释：你总共有 10 个橘子。
第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
你需要至少 4 天吃掉 10 个橘子。

示例 2：
输入：n = 6
输出：3
解释：你总共有 6 个橘子。
第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
你至少需要 3 天吃掉 6 个橘子。

示例 3：
输入：n = 1
输出：1

示例 4：
输入：n = 56
输出：6


提示：

1 <= n <= 2*10^9
"""
from collections import defaultdict
from functools import cache
from heapq import heappop, heappush
from math import inf


# todo 方法 1：专题1-把X变成Y
class Solution:
    @cache
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n

        return min(self.minDays(n // 2) + n % 2, self.minDays(n // 3) + n % 3) + 1


# todo 方法 2：Dijkstra 算法求最短路
"""
也可以这样建图：
x 到 ⌊x/2⌋ 连一条边权为 x%2 + 1 的边。
x 到 ⌊x/3⌋ 连一条边权为 x%3 + 1 的边。
1 到 0 连一条边权为 1 的边。
答案为 n 到 0 的最短路，用 Dijkstra 算法计算。
"""


class Solution2:
    def minDays(self, n: int) -> int:
        dis = defaultdict(lambda: inf)  # 当前数值的最短路径，默认为 inf
        h = [(0, n)]  # 最短路径，当前数值
        while True:
            dx, x = heappop(h)
            # 如果 x≤1，可以直接返回答案
            if x <= 1:
                return dx + x

            if dx > dis[x]:
                continue

            # 代码实现时，无需建图，根据出堆的数字 x 计算出对应的邻居和边权。
            for d in 2, 3:
                y = x // d
                dy = dx + x % d + 1
                if dy < dis[y]:
                    dis[y] = dy
                    heappush(h, (dy, y))
