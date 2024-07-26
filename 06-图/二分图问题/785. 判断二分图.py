"""
存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。
给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。
形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。
该无向图同时具有以下属性：
    1.不存在自环（graph[u] 不包含 u）。
    2.不存在平行边（graph[u] 不包含重复值）。
    3.如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
    4.这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。

二分图 定义：
如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，
并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。

如果图是二分图，返回 true ；否则，返回 false 。

示例 1：
0---- 1
| \   |
|   \ |
3 ---2
输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。

示例 2：
0------1
|      |
|      |
3------2
输入：graph = [[1,3],[0,2],[1,3],[0,2]]
输出：true
解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。


提示：
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] 不会包含 u
graph[u] 的所有值 互不相同
如果 graph[u] 包含 v，那么 graph[v] 也会包含 u
"""
import collections
from typing import List

"""
一、什么是二分图
二分图是指可以将图的节点分成两个不相交的集合，使得图中的每条边连接的两个节点都分属于不同的集合。

二、判断二分图
1、深度优先搜索 / 广度优先搜索
我们使用图搜索算法从各个连通域的任一顶点开始遍历整个连通域，遍历的过程中用两种不同的颜色对顶点进行染色，相邻顶点染成相反的颜色。
这个过程中倘若发现相邻的顶点被染成了相同的颜色，说明它不是二分图；
反之，如果所有的连通域都染色成功，说明它是二分图。

2、并查集
我们知道如果是二分图的话，那么图中每个顶点的所有邻接点都应该属于同一集合，且不与顶点处于同一集合。
因此我们可以使用并查集来解决这个问题，我们遍历图中每个顶点，将当前顶点的所有邻接点进行合并，
并判断这些邻接点中是否存在某一邻接点已经和当前顶点处于同一个集合中了，
若是，则说明不是二分图。
"""


# 方法1：BFS(推荐)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        num_nodes = len(graph)
        # visited[i] 记录节点颜色，初始值为 0 表示未被访问，赋值为 1 或者 -1 表示两种不同的颜色。
        visited = [0] * num_nodes  # 这里也可以换做一个字典

        for node in range(num_nodes):
            # 已经着色的节点不用重复访问
            if visited[node] != 0:
                continue

            # 如果节点未被着色, 将节点着色为 1,并将节点加入一个新的队列，进行bfs遍历
            dq = collections.deque([node])
            visited[node] = 1
            # 每出队一个顶点，将其所有邻接点染成相反的颜色并入队。
            while dq:
                cur_node = dq.popleft()
                cur_color = visited[cur_node]
                for neighbor in graph[cur_node]:
                    # 1.如果邻居节点未被着色,将邻居节点着色为与当前节点相反的颜色, 并加入dq
                    if visited[neighbor] == 0:
                        visited[neighbor] = -cur_color
                        dq.append(neighbor)
                    # 2.如果邻居节点已被着色，并且颜色相同，返回 false
                    if visited[neighbor] == cur_color:
                        return False

        return True


# 方法2：dfs
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        num_nodes = len(graph)
        # visited[i] 记录节点颜色，初始值为 0 表示未被访问，赋值为 1 或者 -1 表示两种不同的颜色。
        global visited
        visited = [0] * num_nodes

        for node in range(num_nodes):
            # 已经着色的节点不用遍历，还没有着色的节点将他着色为1，并进行dfs遍历
            if visited[node] == 0 and not self.dfs(graph, node, 1):
                return False
        return True

    def dfs(self, graph, node: int, color: int) -> bool:
        """判断节点node所有相邻节点是否可以分为2个集合"""
        global visited
        visited[node] = color
        for neighbor in graph[node]:
            # 1.如果相邻节点已经染色，且颜色与当前节点相同，说明不能二分，返回False
            if visited[neighbor] == color:
                return False
            # 2.如果相邻节点还没有染色，对相邻节点进行反向染色，并进行递归
            # 注意：一旦发现有相邻节点不能二分，要终止递归，返回False
            if visited[node] == 0 and not self.dfs(graph, neighbor, -color):
                return False
        # 3.如果所有相邻节点都能正确被染色，返回True
        return True


"""
如果要使用并查集来判断一个图是否是二分图，可以使用以下步骤：
1.初始化并查集，将每个节点初始化为一个独立的集合。
2.遍历图中的每条边，对于每条边的两个节点 u 和 v，判断它们是否属于同一个集合。如果属于同一个集合，则图不是二分图，返回 False。
3.如果节点 u 和节点 v 不属于同一个集合，则将它们合并到同一个集合中。
4.遍历完所有的边后，如果没有发现属于同一个集合的节点，则图是二分图，返回 True。
"""


# 方法3：并查集
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # 判断 x 和 y 是否在同一个集合中
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)

    # 合并 x 和 y 到一个集合中
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y


class Solution3:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # 初始化并查集
        num_nodes = len(graph)
        uf = UnionFind(num_nodes)

        # 遍历每个顶点，将当前顶点的所有邻接点进行合并
        for u in range(num_nodes):
            for v in graph[u]:
                if uf.isConnected(u, v):  # 如果节点 u 和节点 v 属于同一个集合，则图不是二分图
                    return False
                uf.union(graph[u][0], v)  # 将节点 u 和节点 v 合并到同一个集合中

        return True


if __name__ == '__main__':
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]  # False
    graph2 = [[1, 3], [0, 2], [1, 3], [0, 2]]  # True
    # print(Solution().isBipartite(graph))
    print(Solution().isBipartite(graph2))
    print(Solution2().isBipartite(graph2))
    print(Solution3().isBipartite(graph2))
