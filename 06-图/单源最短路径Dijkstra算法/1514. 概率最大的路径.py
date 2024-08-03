"""
给你一个由 n 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 edges[i] = [a, b] 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 succProb[i] 。

指定两个节点分别作为起点 start 和终点 end ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。

如果不存在从 start 到 end 的路径，请 返回 0 。只要答案与标准答案的误差不超过 1e-5 ，就会被视作正确答案。

 

示例 1：
输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
输出：0.25000
解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25
示例 2：



输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
输出：0.30000
示例 3：



输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
输出：0.00000
解释：节点 0 和 节点 2 之间不存在路径
 

提示：

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
每两个节点之间最多有一条边
"""

import collections
import heapq
from typing import List

# 无向图本质上可以认为是「双向图」，从而转化成有向图。
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)
        for i in range(len(edges)):
            from_node, to_node = edges[i]
            weight = succProb[i]
            # 注意：这里是双向图
            graph[from_node].append((to_node, weight))
            graph[to_node].append((from_node, weight))

        # 记录最短路径的权重，你可以理解为 dp table
        # 定义：distTo[i] 的值就是节点 start 到达节点 i 的最短路径权重
        distances = [0] * (n+1)
        distances[start_node] = 1  # 开始起点权重定为1
        maxHeap = [(-1, start_node)]
        ans = 0
        while maxHeap:
            from_weight, from_node = heapq.heappop(maxHeap)
            for to_node, to_weight in graph[from_node]:
                cur_weight = (-from_weight) * to_weight
                if to_node == end_node:
                    # 注意：这里更新结果，不能直接返回。目的节点就不需要再加入最大堆了
                    ans = max(ans, cur_weight)
                else:
                    if cur_weight > distances[to_node]:
                        distances[to_node] = cur_weight
                        heapq.heappush(maxHeap, (-distances[to_node], to_node))

        return ans
