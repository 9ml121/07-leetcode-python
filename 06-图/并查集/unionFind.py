from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UnionFind(n)

        # 只遍历矩阵斜对角下半部（不包括对角线）
        for i in range(n):
            for j in range(i):
                # 如果两个人是朋友，就将他们合并到同一个集合中
                if M[i][j] == 1:
                    uf.union(i, j)
        # 返回联通分量的个数
        return uf.count


# 2.并查集结构(完全路径压缩)
class UnionFind:
    def __init__(self, n: int):
        """
        构造函数接受一个整数 n 作为参数，表示元素的个数
        parent 数组来表示每个元素的根节点编号，初始时每个元素的根节点编号都是它自己的编号。
        count 表示连通分量的个数，初始值为元素总个数
        """
        self.parent = [i for i in range(n)]
        self.count = n

    def find(self, x: int) -> int:
        """返回val为x的节点的根节点val
        完全路径压缩：让查询根结点的过程中，沿途经过的 所有结点 指向都指向根结点。
        """
        if x != self.parent[x]:
            # find(parent[x]) 会返回树的根结点，
            # parent[x] = find(parent[x]) 会将沿途经过的结点的父亲结点都指向根结点
            self.parent[x] = self.find(self.parent[x])
        # 输入 x 没有发生变化，应返回 x 的父亲结点，才表示树根结点
        return self.parent[x]

    def union(self, x, y) -> None:
        """
        在合并两个元素时，先找到它们的根节点，
        然后将其中一个根节点的父节点指向另一个根节点，即将它们合并成一个集合。
        """
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX
            self.count -= 1

    def __repr__(self):
        return str(self.parent)


class Solution2:
    def findCircleNum(self, M: List[List[int]]) -> int:
        uf = UnionFind2()
        for i in range(len(M)):
            uf.add(i)
            for j in range(i):
                if M[i][j]:
                    uf.merge(i, j)

        return uf.num_of_sets


# 并查集结构写法 2
class UnionFind2:
    def __init__(self):
        self.father = {}
        # 额外记录集合的数量
        self.num_of_sets = 0

    def find(self, x):
        """完全路径压缩迭代写法：树高度为 2"""
        root = x

        while self.father[root]:
            root = self.father[root]

        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            # 集合的数量-1
            self.num_of_sets -= 1

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            # 集合的数量+1
            self.num_of_sets += 1


if __name__ == '__main__':
    ufs = UnionFind(5)
