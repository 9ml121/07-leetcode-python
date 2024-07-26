"""
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。
图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}


测试用例格式：
  简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。
  邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。



示例 1：
输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
输出：[[2,4],[1,3],[2,4],[1,3]]
解释：
图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。

示例 2：
输入：adjList = [[]]
输出：[[]]
解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。

示例 3：
输入：adjList = []
输出：[]
解释：这个图是空的，它不含任何节点。

示例 4：
输入：adjList = [[2],[1]]
输出：[[2],[1]]


提示：
节点数不超过 100 。
每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
图是连通图，你可以从给定节点访问到所有节点。
"""
import collections


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional

"""
题目描述：
给定一个无向连通图中的一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值 val（Int）和其邻居的列表（list[Node]）。

解题思路：
克隆图的问题可以使用深度优先搜索（DFS）或广度优先搜索（BFS）来解决。我们可以从给定的节点开始进行遍历，然后递归地克隆每个节点和其邻居节点。

具体步骤如下：
1.创建一个字典 visited，用于存储已经访问过的节点，键为原始节点，值为克隆节点。
2.创建一个辅助函数 cloneNode，接收一个节点 node 作为参数，用于克隆节点和其邻居节点。
3.在 cloneNode 中，首先创建一个新节点 clone，将其值设置为原始节点的值。
4.将 clone 加入 visited 字典中，键为 node，值为 clone。
5.遍历原始节点的邻居节点，如果邻居节点已经在 visited 中，则将其对应的克隆节点加入 clone 的邻居列表中；
  否则，递归调用 cloneNode 函数克隆邻居节点，并将克隆节点加入 clone 的邻居列表中。
6.返回 clone 节点作为结果。
"""


# dfs思路
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 字典 visited用于存储已经访问过的节点，键为原始节点，值为克隆节点。
        visited = {}

        def dfs(node):
            if not node:
                return None

            if node in visited:
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)


# bfs思路
class Solution2:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # 1.字典 visited，用于存储已经访问过的节点，键为原始节点，值为克隆节点。
        visited = {}
        # 2.将给定的节点加入队列 queue 中，并创建一个克隆节点 clone，将其值设置为原始节点的值。
        queue = collections.deque([node])
        clone = Node(node.val)
        # 3.将 clone 加入 visited 字典中，键为原始节点，值为 clone。
        visited[node] = clone

        # 4.在循环中，从队列 queue 中弹出一个节点 curr，遍历其邻居节点。
        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                # 1)对于每个邻居节点，如果该节点已经在 visited 中，则将其对应的克隆节点加入 curr 的克隆节点的邻居列表中
                if neighbor in visited:
                    visited[curr].neighbors.append(visited[neighbor])
                # 2)否则，创建一个新的克隆节点 neighbor_clone，将其值设置为邻居节点的值，
                # 将其加入 visited 字典中，并将其加入 curr 的克隆节点的邻居列表中。
                else:
                    neighbor_clone = Node(neighbor.val)
                    visited[neighbor] = neighbor_clone
                    visited[curr].neighbors.append(neighbor_clone)
                    queue.append(neighbor)  # 将邻居节点加入队列 queue 中，以便继续遍历其邻居节点。
        # 5.返回初始节点的克隆节点作为结果。
        return clone
