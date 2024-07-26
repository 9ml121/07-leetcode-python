"""
在由 2D 网格表示的校园里有 n 位工人（worker）和 m 辆自行车（bike），n <= m。所有工人和自行车的位置都用网格上的 2D 坐标表示。

我们为每一位工人分配一辆专属自行车，使每个工人与其分配到的自行车之间的 曼哈顿距离 最小化。

返回 每个工人与分配到的自行车之间的曼哈顿距离的最小可能总和 。

p1 和 p2 之间的 曼哈顿距离 为 Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|。

 

示例 1：



输入：workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]
输出：6
解释：
自行车 0 分配给工人 0，自行车 1 分配给工人 1 。分配得到的曼哈顿距离都是 3, 所以输出为 6 。
示例 2：



输入：workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]
输出：4
解释：
先将自行车 0 分配给工人 0，再将自行车 1 分配给工人 1（或工人 2），自行车 2 给工人 2（或工人 1）。如此分配使得曼哈顿距离的总和为 4。
示例 3:

输入：workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]
输出：4995
 

提示：

n == workers.length
m == bikes.length
1 <= n <= m <= 10
workers[i].length == 2
bikes[i].length == 2
0 <= workers[i][0], workers[i][1], bikes[i][0], bikes[i][1] < 1000
所有的工人和自行车的位置都是 不同 的。
"""


from collections import defaultdict
from functools import cache
from math import inf
from typing import List


# 状态压缩 + 记忆化搜索
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def dis(p1: list[int, int], p2: list[int, int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        m = len(workers)
        n = len(bikes)

        @cache
        def dfs(i: int, mask: int) -> int:
            # 尝试给第i个工人分配自行车
            # 用m位二进制数mask表达自行车的分配情况,1为可分配,0为已分配。
            # 对第 i 个人，搜索可分配位置的自行车，并更新距离
            if i == m:   # 如果没有人了，返回 0
                return 0

            res = inf
            for j in range(n):        # 遍历每个自行车
                if mask >> j & 1:     # 第 j 辆自行车可分配
                    # 把 bikes[j] 分配给 workers[i] 并计算距离
                    # 同时把人的已使用数量加 1、bike 的 mask 当前位置自行车状态置为 0
                    res = min(
                        res, dis(workers[i], bikes[j]) + dfs(i+1, mask ^ (1 << j)))

            return res

        return dfs(0, (1 << n)-1)


# 写法 2：状态压缩 + 记忆化搜索
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def Manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        m = len(workers)
        n = len(bikes)

        @cache
        def dfs(i: int, mask: int) -> int:    
            # 对第 i 个人，搜索剩余的自行车并尝试分配给他，同时计算距离
            if i == m:       # 如果没有人了，返回 0
                return 0

            res = inf
            for j in range(n):      # 遍历每个自行车
                if mask & (1 << j) == 0:     # 如果未使用过
                    # 把 bikes[j] 分配给 workers[i] 并计算距离 ，同时把人的已使用数量加 1、bike 的 mask 赋上值
                    res = min(res, Manhattan(
                        workers[i], bikes[j]) + dfs(i+1, mask | (1 << j)))
            return res

        return dfs(0, 0)


# 状态压缩 + 动态规划
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        n = len(workers)
        m = len(bikes)
        # 动态数组用一个key长度为 n的字典表示
        f = defaultdict(lambda: defaultdict(lambda: inf))
        f[0][0] = 0
        
        for i in range(n):
            for k in f[i].keys():
                for j in range(m):
                    if (k >> j) & 1 == 0:
                        f[i + 1][k | (1 << j)] = min(f[i + 1][k | (1 << j)], abs(
                            workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]) + f[i][k])
        return min(f[n].values())
