"""
给你一张 无向 图，图中有 n 个节点，节点编号从 0 到 n - 1 （都包括）。同时给你一个下标从 0 开始的整数数组 values ，其中 values[i] 是第 i 个节点的 价值 。同时给你一个下标从 0 开始的二维整数数组 edges ，其中 edges[j] = [uj, vj, timej] 表示节点 uj 和 vj 之间有一条需要 timej 秒才能通过的无向边。最后，给你一个整数 maxTime 。

合法路径 指的是图中任意一条从节点 0 开始，最终回到节点 0 ，且花费的总时间 不超过 maxTime 秒的一条路径。你可以访问一个节点任意次。一条合法路径的 价值 定义为路径中 不同节点 的价值 之和 （每个节点的价值 至多 算入价值总和中一次）。

请你返回一条合法路径的 最大 价值。

注意：每个节点 至多 有 四条 边与之相连。

 

示例 1：



输入：values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
输出：75
解释：
一条可能的路径为：0 -> 1 -> 0 -> 3 -> 0 。总花费时间为 10 + 10 + 10 + 10 = 40 <= 49 。
访问过的节点为 0 ，1 和 3 ，最大路径价值为 0 + 32 + 43 = 75 。
示例 2：



输入：values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30
输出：25
解释：
一条可能的路径为：0 -> 3 -> 0 。总花费时间为 10 + 10 = 20 <= 30 。
访问过的节点为 0 和 3 ，最大路径价值为 5 + 20 = 25 。
示例 3：



输入：values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50
输出：7
解释：
一条可能的路径为：0 -> 1 -> 3 -> 1 -> 0 。总花费时间为 10 + 13 + 13 + 10 = 46 <= 50 。
访问过的节点为 0 ，1 和 3 ，最大路径价值为 1 + 2 + 4 = 7 。
示例 4：



输入：values = [0,1,2], edges = [[1,2,10]], maxTime = 10
输出：0
解释：
唯一一条路径为 0 。总花费时间为 0 。
唯一访问过的节点为 0 ，最大路径价值为 0 。
 

提示：

n == values.length
1 <= n <= 1000
0 <= values[i] <= 108
0 <= edges.length <= 2000
edges[j].length == 3 
0 <= uj < vj <= n - 1
10 <= timej, maxTime <= 100
[uj, vj] 所有节点对 互不相同 。
每个节点 至多有四条 边。
图可能不连通。
"""


import heapq
from math import inf
from typing import List


# todo 暴力搜索 + 回溯 + 图
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        n = len(values)
        maps = [[] for _ in range(n)]
        for u, v, time in edges:
            maps[u].append((v, time))
            maps[v].append((u, time))

        used = [False] * n
        used[0] = True
        ans = 0

        def dfs(i: int = 0,  sum_time: int = 0, sum_val: int = values[0]):
            if i == 0:
                nonlocal ans
                ans = max(ans, sum_val)
                # 注意这里没有 return，还可以继续走

            for j, time in maps[i]:
                if sum_time + time > maxTime:
                    continue
                if used[j]:
                    dfs(j, sum_time + time, sum_val)
                else:
                    used[j] = True
                    # 每个节点的价值至多算入价值总和中一次
                    dfs(j, sum_time + time, sum_val + values[j])
                    used[j] = False

        dfs()
        return ans


# 方法二：爆搜+最短路剪枝
class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], max_time: int) -> int:
        n = len(values)
        g = [[] for _ in range(n)]
        for x, y, t in edges:
            g[x].append((y, t))
            g[y].append((x, t))

        # todo Dijkstra 算法, 预处理每个节点到 0 的最短路
        dis = [inf] * n
        dis[0] = 0
        h = [(0, 0)]  # 每个节点到 0 的最短路， 节点
        while h:
            dx, x = heapq.heappop(h)
            if dx > dis[x]:  # x 之前出堆过
                continue
            for y, d in g[x]:
                new_dis = dx + d
                if new_dis < dis[y]:
                    dis[y] = new_dis  # 更新 x 的邻居的最短路
                    heapq.heappush(h, (new_dis, y))

        def dfs(x: int, sum_time: int, sum_value: int) -> None:
            if x == 0:
                nonlocal ans
                ans = max(ans, sum_value)
                # 注意这里没有 return，还可以继续走
                
            for y, t in g[x]:
                # 相比方法一，这里多了 dis[y]
                if sum_time + t + dis[y] > max_time:
                    continue
                if vis[y]:
                    dfs(y, sum_time + t, sum_value)
                else:
                    vis[y] = True
                    # 每个节点的价值至多算入价值总和中一次
                    dfs(y, sum_time + t, sum_value + values[y])
                    vis[y] = False  # 恢复现场

        ans = 0
        vis = [False] * n
        vis[0] = True
        dfs(0, 0, values[0])
        return ans
