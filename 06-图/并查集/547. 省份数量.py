"""
题目描述形式1:
班上有 n 名学生。其中有些人是朋友，有些则不是。他们的友谊本质上是单向的。
例如，如果 A 是 B 的朋友，那么 B 不一定是 A 的朋友。我们用一个 n*n 的矩阵 M 表示这样的关系。
例如，M[i][j] = 1 表示 A 是 B 的朋友，而 M[i][j] = 0 则表示他们不是朋友。

你要统计有多少个朋友圈。你需要对这个矩阵进行操作，直到所有的朋友圈都被统计出来。

题目描述形式2：
有 n 个城市，其中一些彼此相连，另一些没有相连。
如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。

返回矩阵中 省份 的数量。


示例 1:
输入:
        [[1,1,0],
         [1,1,0],
         [0,0,1]]
输出: 2
说明：已经有两个朋友圈了，第三个人自己一个人，所以是自己一个朋友圈。

示例 2:
输入:
        [[1,1,0],
         [1,1,1],
         [0,1,1]]
输出: 1
说明：只有一个朋友圈，即使第二个人和第三个人互相认识。

提示：
1 <= n <= 200
M[i][i] == 1
M[i][j] == M[j][i]
"""
from typing import List


# 方法 1：并查集
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        # 获取矩阵的长度
        length = len(M)
        # 初始化并查集
        union_find = UnionFind2(length)
        # 遍历矩阵
        for i in range(length):
            # 只需要遍历下三角部分（不包括对角线）
            for j in range(i):
                # 如果两个人是朋友，就将他们合并到同一个集合中
                if M[i][j] == 1:
                    union_find.union(i, j)
        # 返回联通分量的个数
        return union_find.count


"""
1.quick-find 基于 id 的思想：
- 给每一个组一个编号，这个编号称为 id ， 如果两个元素的 id 一样，就认为它们同属于一个集合，时间复杂度为 O(1)。
- 要想合并两个组，就需要将它们的 id 设置成一样。在最差情况下，需要修改几乎整个数组元素的 id，时间复杂度为 O(N)。
所以这一版并查集「查询」快，但是「合并」慢。
"""


# todo 1.并查集的 quick-find 实现。
# 时间复杂度O(n^3), 这里 n 是输入数组的长度，双层循环 O(n^2), 合并操作 O(n)
class UnionFind:
    """UnionFind第一版：quick-find"""

    def __init__(self, n: int):
        """
        n:输入数组的长度，
        parent:输入数组的索引列表
        count:连通分量的个数,即题目要求的朋友圈个数，初始化为数组长度
        """
        self.n = n
        self.parent = list(range(n))
        self.count = n

    def find(self, x: int) -> int:
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        xid = self.find(x)
        yid = self.find(y)
        if xid == yid:
            return
        # 将索引列表中所有xid的值都替换为yid
        for i in range(self.n):
            if self.parent[i] == xid:
                self.parent[i] = yid
        self.count -= 1

    # 重写__repr__函数，返回索引列表的字符串形式
    def __repr__(self):
        return str(self.parent)


"""
2.quick-find 基于代表的思想：
- 为每一个集合选出一个代表元素，这个代表元素位于这棵树的 根结点，因此也叫 代表元法 。
- 只要有发生合并，不是修改标识，而是 把其中一个元素的根结点的链接指向另一个元素的根结点 ，这里「链接指向」是通过 parent 数组体现的

# 查：树的平均高度是log(n)，查询的平均时间复杂度就是数的高度O(log(n))。
# 并：在合并的时候，只需要将其中一个元素指向另一个元素即可,真正的合并操作时间复杂度为O(1)。
     合并之前需要做两次查询，因此时间复杂度依然是O(log(n))。
"""


# todo 2.并查集的 quick-union 实现
# 时间复杂度O(n^2 * log(n)), 这里 n 是数组的长度
class UnionFind2:
    """UnionFind第2版: quick-union => union的时候不考虑每个节点所在数的高度"""

    def __init__(self, n: int):
        # 在查找的过程中，总是从下到上查找，每个结点的父结点是我们关心的，因此把这个数组命名为 parent
        # parent[i] 代表以i为节点val的子树的根节点val为parent[i]
        # 初始化的时候，每个元素指向它自己，即：单独的一个结点是一棵树
        self.parent = list(range(n))
        # 初始化联通分量的数量为节点数
        self.count = n

    def find(self, x: int) -> int:
        """
        查找节点x所在的集合的根节点,时间复杂度为节点所在数的高度O(log(N))
        """
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        """
        1.有发生合并，把其中一个元素的根结点的链接指向另一个元素的根结点, 这里「链接指向」是通过 parent 数组体现的
        2.合并之前需要做两次查询，因此时间复杂度依然是O(log(N))。
        """
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        # 很随意地将其中一颗树的 根结点 指向另一棵树的 根结点,容易导致数的高度不断增加
        self.parent[rootX] = rootY
        self.count -= 1

    def __repr__(self):
        return str(self.parent)


# todo 3.并查集的 quick-union 优化1：按照size合并
class UnionFind3:
    """UnionFind第3版: 把 结点个数 较少的树的根结点指向结点个数较多的树的根结点"""

    def __init__(self, n: int):
        # parent[i] 代表以i为节点val的子树的根节点val为parent[i]
        self.parent = list(range(n))
        self.count = n
        # size[i]代表以i为节点的数的节点个数
        # 初始化的时候，每个结点都是一颗树，只有 1 个结点
        self.size = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        if self.size[rootX] == self.size[rootY]:
            # 将其中一棵树的跟节点指向另一棵树的根节点，两个根节点不分彼此
            self.parent[rootX] = rootY
            self.size[rootY] += 1
        elif self.size[rootX] < self.size[rootY]:
            self.parent[rootX] = rootY
            # 此时以rootY为根节点的子树多了size[rootX]这么多节点
            # 需要维护定义
            self.size[rootY] += self.size[rootX]
        else:
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]
        self.count -= 1

    def __repr__(self):
        return str(self.parent)


# todo 4.并查集的 quick-union 优化2：按照rank合并(推荐!!)
class UnionFind4:
    """UnionFind第4版: 将 高度 较低树的根结点指向 高度 较高的树的根结点"""

    def __init__(self, n: int):
        # parent[i] 代表以i为节点val的子树的根节点val为parent[i]
        self.parent = list(range(n))
        self.count = n
        # rank[i]代表以 i 为根结点的子树的高度，初始化高度都为1
        self.rank = [1] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        if self.rank[rootX] == self.rank[rootY]:
            self.parent[rootX] = rootY
            # 此时以 rootY 为根结点的树的高度仅加了 1
            self.rank[rootY] += 1
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            # 此时以 rootY 为根结点的树的高度不变
        else:
            # 同理，此时以 rootX 为根结点的树的高度不变
            self.parent[rootY] = rootX
        self.count -= 1


# todo 4.并查集的 quick-union 优化3：路径压缩的思路1：隔代压缩
class UnionFind5:
    """UnionFind第5版: 路径压缩的思路 1：隔代压缩 + 基于rank的合并
    让查询过程中经历的 部分结点 指向它的父亲结点的父亲结点。相对于「完全压缩」而言，压缩没有那么彻底。
    """

    def __init__(self, n: int):
        # parent[i] 代表以i为节点val的子树的根节点val为parent[i]
        self.parent = list(range(n))
        self.count = n
        # rank[i]代表以 i 为根结点的子树的高度，初始化高度都为1
        self.rank = [1] * n

    def find(self, x: int) -> int:
        """返回val为x的节点的根节点val
        """
        while x != self.parent[x]:
            # 路径压缩：隔代压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        if self.rank[rootX] == self.rank[rootY]:
            self.parent[rootX] = rootY
            # 此时以 rootY 为根结点的树的高度仅加了 1
            self.rank[rootY] += 1
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
            # 此时以 rootY 为根结点的树的高度不变
        else:
            # 同理，此时以 rootX 为根结点的树的高度不变
            self.parent[rootY] = rootX
        self.count -= 1


# todo 4.并查集的 quick-union 优化3：路径压缩的思路2：完全压缩(终极优化！！)
class UnionFind6:
    """UnionFind第6版: 路径压缩的思路 2：完全压缩 + 基于rank的合并
    让查询过程中经历的 部分结点 指向它的父亲结点的父亲结点。相对于「完全压缩」而言，压缩没有那么彻底。
    """

    def __init__(self, n: int):
        # parent[i] 代表以i为节点val的子树的根节点val为parent[i]
        self.parent = list(range(n))
        self.count = n
        # rank[i]代表以 i 为根结点的子树的高度，初始化高度都为1
        self.rank = [1] * n

    def find(self, x: int) -> int:
        """返回val为x的节点的根节点val
        路径压缩：完全压缩
        """
        if x != self.parent[x]:
            # find(parent[x]) 会返回树的根结点，
            # parent[x] = find(parent[x]) 会将沿途经过的结点的父亲结点都指向根结点
            self.parent[x] = self.find(self.parent[x])
        # 输入 x 没有发生变化，应返回 x 的父亲结点，才表示树根结点
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return

        if self.rank[rootX] == self.rank[rootY]:
            self.parent[rootX] = rootY
            self.rank[rootY] += 1
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
        self.count -= 1

    def __repr__(self):
        return str(self.parent)


if __name__ == '__main__':
    M = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    s = Solution()
    print(s.findCircleNum(M))
