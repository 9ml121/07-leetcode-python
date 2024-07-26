"""
有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，
其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

示例 1：
输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2

示例 2：
输入：times = [[1,2,1]], n = 2, k = 1
输出：1

示例 3：
输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
 

提示：
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）
"""


import heapq
import collections
from typing import List

# todo 最小堆实现单源最短路径(有向图) 后悔贪心思维
"""
参考：
https://blog.csdn.net/qfc_128220/article/details/127680161?spm=1001.2014.3001.5501

https://labuladong.online/algo/data-structure/dijkstra/#%E7%A7%92%E6%9D%80%E4%B8%89%E9%81%93%E9%A2%98%E7%9B%AE
"""

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1.构建连接图(可以用字典，也可以用二维列表)
        # 对比来看，邻接表模拟图结构在内存消耗上代价更小，因此我们一般选择邻接表来模拟图结构
        graph = collections.defaultdict(list)
        for u, v, w in times:
            # 注意这里是单向图,ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间
            graph[u].append((v, w))

        # 2.记录最短路径的权重，这道题是从节点k开始发出信号，到达节点i的最短传递时间为dist[i]
        # 初始化到达开始节点k传递时间为0, 到达其他节点为float('inf')
        dist = [float('inf')] * (n+1)
        dist[k] = 0  

        # 3.使用一个小根堆来寻找「未确定节点」中与起点距离最近的点。
        # Dijkstra 算法使用优先级队列，主要是为了效率上的优化，类似一种贪心算法的思路。
        minHeap = [(dist[k], k)]  # (传递时间，传递节点)

        # 4.最短路径问题，一般不用dfs
        # bfs可以结合后悔贪心算法思维，让最短路径的查找变为类似于二叉树的二分查找
        while minHeap:
            time, u = heapq.heappop(minHeap)
            for v, w in graph[u]:
                if time + w < dist[v]:
                    dist[v] = time + w
                    heapq.heappush(minHeap, (dist[v], v))

        # 有效节点从1到n,如果到某个节点的传递时间为float('inf')，证明没有传递到
        ans = max(dist[1:])
        # 本题是 “从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号”，即本题要求从K节点到剩余其他各店的单源最短路径，并返回这里最短路径中最大的那个。
        return -1 if ans == float('inf') else ans
