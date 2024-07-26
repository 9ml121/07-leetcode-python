"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127711368

OJ用例
题解 - 找城市 - Hydro

题目描述
一张地图上有n个城市，城市和城市之间有且只有一条道路相连：要么直接相连，要么通过其它城市中转相连（可中转一次或多次）。城市与城市之间的道路​都不会成环​。

当切断通往某个城市 i 的所有道路后，地图上将分为多个连通的城市群，设该城市i的聚集度为DPi（Degree of Polymerization），DPi = max（城市群1的城市个数，城市群2的城市个数，…城市群m 的城市个数）。

请找出地图上DP值最小的城市（即找到城市j，使得DPj = min(DP1,DP2 … DPn))

提示：如果有多个城市都满足条件，这些城市都要找出来（​可能存在多个解​）

提示：DPi的计算，可以理解为已知一棵树，删除某个节点后；生成的多个子树，求解多个子数节点数的问题。

输入描述
每个样例：第一行有一个整数N，表示有N个节点。1 <= N <= 1000。

接下来的N-1行每行有两个整数x，y，表示城市x与城市y连接。1 <= x, y <= N

输出描述
输出城市的编号。如果有多个，按照编号升序输出。

用例1
输入
5
1 2
2 3
3 4
4 5
输出
3
说明
输入表示的是如下地图： image

对于城市3，切断通往3的所有道路后，形成2个城市群[（1，2），（4，5）]，其聚集度分别都是2。DP3 = 2。

对于城市4，切断通往城市4的所有道路后，形成2个城市群[（1，2，3），（5）]，DP4 = max（3，1）= 3。

依次类推，切断其它城市的所有道路后，得到的DP都会大于2，因为城市3就是满足条件的城市，输出是3。

用例1
输入
6
1 2
2 3
2 4
3 5
3 6
输出
2 3
说明
将通往2或者3的所有路径切断，最大城市群数量是3，其他任意城市切断后，最大城市群数量都比3大，所以输出2 3
"""


# 考察并查集

# 输入
# n个节点
n = int(input())
# n-1行，城市x与y连接，没有环
grid = [list(map(int, input().split())) for _ in range(n-1)]
# print(grid)

# 找出地图上DP值最小的城市
ans = []
min_dpi = n


class Ufs:
    def __init__(self, n):
        self.fa = list(range(n))

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        fa_x = self.find(x)
        fa_y = self.find(y)
        if fa_x != fa_y:
            self.fa[fa_y] = fa_x


# 城市数量不大。枚举删除其中任意一个节点
for i in range(1, n+1):
    # 删除i节点,更新ufs
    ufs = Ufs(n+1)  # 节点从1开始
    for x, y in grid:
        if x == i or y == i:
            continue

        ufs.union(x, y)

    # 统计每个连通图的节点个数
    cnts = [0] * (n+1)
    for j in range(1, n+1):
        fa = ufs.find(j)
        cnts[fa] += 1

    cur_dpi = max(cnts)
    if cur_dpi < min_dpi:
        min_dpi = cur_dpi
        ans = [i]
    elif cur_dpi == min_dpi:
        ans.append(i)

print(' '.join(map(str, ans)))
