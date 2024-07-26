"""
树可以看成是一个连通且 无环 的 无向 图。

给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。
添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。
图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。
如果有多个答案，则返回数组 edges 中最后出现的那个。


示例 1：
        1---2
        |  /
        | /
        3
输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]

示例 2：
2---1---5
|   |
3---4
输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]


提示:
n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
edges 中无重复元素
给定的图是连通的
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        # cnt 代表连通分量的个数,初始化为输入数组长度
        self.cnt = n
        # 初始化分量 ids数组
        self.fa = list(range(n))

    def find(self, a: int) -> int:
        # 找到根节点
        while a != self.fa[a]:
            self.fa[a] = self.fa[self.fa[a]]
            a = self.fa[a]
        return a

    def union(self, a: int, b: int):
        # quick union
        aRoot = self.find(a)
        bRoot = self.find(b)

        if aRoot != bRoot:
            self.fa[aRoot] = bRoot
            # 每次 union 以后，连通分量减 1
            self.cnt -= 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n + 1)
        for a, b in edges:
            if uf.find(a) != uf.find(b):
                uf.union(a, b)
            else:
                return [a, b]
        return []
