"""
给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。
每个人都可能不喜欢其他人，那么他们不应该属于同一组。

给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和  bi的人归入同一组。
当可以用这种方法将所有人分进两组时，返回 true；
否则返回 false。

示例 1：
输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
输出：true
解释：group1 [1,4], group2 [2,3]

示例 2：
输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
输出：false

示例 3：
输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
输出：false


提示：
1 <= n <= 2000
0 <= dislikes.length <= 104
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
dislikes 中每一组都 不同
"""
import collections
from typing import List


# 与leetcode 785. 判断二分图.py 类似
# 方法1：bfs
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        # visited[node] 记录节点颜色，初始值为 0 表示未被访问，赋值为 1 或者 -1 表示两种不同的颜色。
        visited = [0] * (n + 1)
        # graph[node] 记录编号为i的人不喜欢的人列表
        graph = [[] for _ in range(n + 1)]

        for p1, p2 in dislikes:
            graph[p1].append(p2)
            graph[p2].append(p1)

        # print(graph)
        for node in range(1, n + 1):
            # 已经着色的人不用重复遍历
            if visited[node] != 0:
                continue
            # 还没有着色的人标记为1，并加入一个新的dq
            visited[node] = 1
            dq = collections.deque([node])
            while dq:
                cur_node = dq.popleft()
                cur_color = visited[cur_node]
                for dislike_node in graph[cur_node]:
                    # 1.如果不喜欢的人还没有着色，将他标记为相反的颜色，并加入dq
                    if visited[dislike_node] == 0:
                        visited[dislike_node] = -visited[cur_node]
                        dq.append(dislike_node)
                    # 2.如果不喜欢的人的已经着色，并且与自己颜色一样，说明不能分为2组
                    if visited[dislike_node] == cur_color:
                        return False

        return True


# 方法2：dfs
class Solution2:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]  # 创建邻接表表示图

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        visited = [0] * (n + 1)  # 记录节点的颜色，0表示未着色

        def dfs(node: int, color: int) -> bool:
            visited[node] = color
            for neighbor in graph[node]:
                if visited[neighbor] == color:  # 邻居节点已被着色，并且颜色与当前节点相同
                    return False
                if visited[neighbor] == 0 and not dfs(neighbor, -color):  # 邻居节点未被着色，递归进行DFS遍历
                    return False
            return True

        for i in range(1, n + 1):
            if visited[i] == 0 and not dfs(i, 1):
                return False

        return True
