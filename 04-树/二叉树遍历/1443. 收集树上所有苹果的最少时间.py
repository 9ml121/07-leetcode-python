"""
给你一棵有 n 个节点的无向树，节点编号为 0 到 n-1 ，它们中有一些节点有苹果。
通过树上的一条边，需要花费 1 秒钟。

你从 节点 0 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。

无向树的边由 edges 给出，其中 edges[i] = [fromi, toi] ，表示有一条边连接 from 和 toi 。
除此以外，还有一个布尔数组 hasApple ，其中 hasApple[i] = true 代表节点 i 有一个苹果，否则，节点 i 没有苹果。


示例 1：
         0
       /  \
      1    2
     / \  / \
    4  5 3  6
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
    hasApple = [false,false,true,false,true,true,false]
输出：8
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。

示例 2：
         0
       /  \
      1    2
     / \  / \
    4  5 3  6
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
    hasApple = [false,false,true,false,false,true,false]
输出：6
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。

示例 3：
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]],
    hasApple = [false,false,false,false,false,false,false]
输出：0

示例 4：   
    1   0
     \ / \
      2   3  
输入：n = 4, edges = [[0,2],[0,3],[1,2]]
    hasApple = [false,true,false,false]
输出：4


提示：
1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai < bi <= n - 1
hasApple.length == n
"""
import collections
from typing import List


# 注意：
# 1.edges是一个无向树，不一定是二叉树，但是一定没有环
# 2.edge[0] 和 edge[1]只是说明互相有连接，并不代表父子节点关系！！

# 错误解答：
class Solution1:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # todo 错误点：误认为edge[0] 是 edge[1]的父节点！！
        nodes_dic = collections.defaultdict(list)
        for u, v in edges:
            nodes_dic[u].append(v)

        def dfs(node):
            # 叶子节点返回 0
            if node not in nodes_dic:
                return 0

            total_time = 0
            for child in nodes_dic[node]:
                sub_time = dfs(child)
                # 如果子节点有苹果或者子节点到叶子节点路径上有苹果，则路径上需要的时间为2
                if sub_time > 0 or hasApple[child]:
                    total_time += sub_time + 2
            return total_time

        return dfs(0)


# 错误解答2：误认为edge[0] 是 edge[1]的父节点！！
class Solution2:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        for u, v in reversed(edges):
            if hasApple[v]:
                hasApple[u] = True

        res = 0
        for u, v in edges:
            if hasApple[v]:
                res += 2
        return res


# 正确解答
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        # todo 构建树的邻接表表示
        graph = [set() for _ in range(n)]
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        def dfs(node):
            # 叶子节点返回 0
            if not graph[node]:
                return 0

            total_time = 0
            for child in graph[node]:
                # 删除子节点到当前节点的边，避免重复遍历
                graph[child].remove(node)

                # 递归遍历子节点
                sub_time = dfs(child)

                # todo 如果子节点有苹果或者子节点到叶子节点路径上有苹果，则路径上需要的时间为2
                if sub_time > 0 or hasApple[child]:
                    total_time += sub_time + 2
            return total_time

        return dfs(0)


if __name__ == '__main__':
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    hasApple = [False, False, True, False, True, True, False]
    print(Solution().minTime(n, edges, hasApple))
