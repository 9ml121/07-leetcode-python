"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134844501?spm=1001.2014.3001.5501

OJ用例
题解 - 5G网络建设 - Hydro

题目描述
现需要在某城市进行5G网络建设，已经选取N个地点设置5G基站，编号固定为1到N，接下来需要各个基站之间使用光纤进行连接以确保基站能互联互通，不同基站之间假设光纤的成本各不相同，且有些节点之间已经存在光纤相连。

请你设计算法，计算出能联通这些基站的最小成本是多少。

注意：基站的联通具有传递性，比如基站A与基站B架设了光纤，基站B与基站C也架设了光纤，则基站A与基站C视为可以互相联通。

输入描述
第一行输入表示基站的个数N，其中：

0 < N ≤ 20
第二行输入表示具备光纤直连条件的基站对的数目M，其中：

0 < M < N * (N - 1) / 2
从第三行开始连续输入M行数据，格式为

X Y Z P

其中：

X，Y 表示基站的编号

0 < X ≤ N
0 < Y ≤ N
X ≠ Y
Z 表示在 X、Y之间架设光纤的成本

0 < Z < 100
P 表示是否已存在光纤连接，0 表示未连接，1表示已连接

输出描述
如果给定条件，可以建设成功互联互通的5G网络，则输出最小的建设成本

如果给定条件，无法建设成功互联互通的5G网络，则输出 -1

用例1
输入
3
3
1 2 3 0
1 3 1 0
2 3 5 0
输出
4
说明
只需要在1，2以及1，3基站之间铺设光纤，其成本为3+1=4

用例2
输入
3
1
1 2 5 0
输出
-1
说明
3基站无法与其他基站连接，输出-1

用例3
输入
3
3
1 2 3 0
1 3 1 0
2 3 5 1
输出
1
说明
2，3基站已有光纤相连，只要在1，3基站之间铺设光纤，其成本为1
"""

import heapq
import collections
# 1.获取输入
# 第一行输入表示基站的个数N,0 < N ≤ 20
n = int(input())
# 第二行输入表示具备光纤直连条件的基站对的数目M
m = int(input())
# 从第三行开始连续输入M行数据
items = [list(map(int, input().split())) for _ in range(m)]
# print(items)

# todo 最小生成树问题
# 方法1:Prim算法是基于顶点找最小生成树。用到数据结构是堆


def prim(n: int, items: list):
    # 1) 构建无向邻接图graph, 可以用字典，也可以用二维矩阵实现
    graph = collections.defaultdict(list)
    for u, v, cost, p in items:
        # 0 表示未连接，1表示已连接
        if p == 0:
            graph[u].append((v, cost))
            graph[v].append((u, cost))
        else:
            graph[u].append((v, 0))
            graph[v].append((u, 0))
    # print(graph)

    # 2) 建立一个最小堆pq，存储还未加入生成树的节点和连接成本，
    # 优先级是连接成本最低，初始化随便加入一个站点到pq
    pq = [(0, 1)]
    # 输出最小的建设成本
    min_cost = 0
    # used记录已经加入生成树的节点集合
    used = set()
    while n > 0 and pq:
        # pq每次弹出建设成本最低的节点u，如果u不在生成树used中，则加入到生成树, 剩余节点个数n-=1
        cost, u = heapq.heappop(pq)
        if u not in used:
            min_cost += cost
            used.add(u)
            n -= 1

        # 遍历u的所有连接点，如果还没有加入生成树used，就加入到pq
        for v, cost in graph[u]:
            if v not in used:
                heapq.heappush(pq, (cost, v))
        # print(f'used={used},pq={pq}, min_cost={min_cost}')

    if n == 0:  # 证明所有节点都加入到生成树
        return min_cost
    else:  # 如果给定条件，无法建设成功互联互通的5G网络，则输出 -1
        return -1


# print(prim(n, items))

# 方法2: Kruskal是基于边找最小生成树，用到数据结构是并查集
class Ufs:
    def __init__(self, n) -> None:
        self.fa = list(range(n))
        self.cnt = n  # cnt代表无向连通图个数

    def find(self, x):
        if self.fa[x] != x:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]

    def union(self, x, y):
        fa_x = self.find(x)
        fa_y = self.find(y)

        if fa_y != fa_x:
            self.fa[fa_y] = fa_x
            self.cnt -= 1


def kruskal(n, items):
    # 1) 根据连接矩阵items，构建带权重的连接边图edges
    edges = []
    for u, v, cost, p in items:
        if p == 1:  # 1代表已连接
            cost = 0
        edges.append((u, v, cost))
    
    # 2) 构建并查集，注意节点是从1开始
    ufs = Ufs(n+1)  
    
    # 3) 根据边权升序, 保证先遍历到的是边权最小的节点
    edges.sort(key=lambda x: x[2])
    # print(edges)
    min_cost = 0
    for u, v, cost in edges:
        # 如果x节点 和 y节点 是同一个连通分量（即都在最小生成树中），则此时会产生环
        # 因此只有当x节点 和 y节点不在同一个连通分量时，才能合并（纳入最小生成树）
        if ufs.find(u) != ufs.find(v):
            ufs.union(u, v)
            min_cost += cost

            # print(f'fa ={ufs.fa}, cnt={ufs.cnt}')
            
            # 需要注意的是，上面初始化并查集的节点数为n+1个，因此并查集底层fa数组的长度就是n+1，即索引范围是[0, n]，左闭右闭，
            # 其中0索引是无用的，1~n索引对应最小生成树中各个节点，如果者n个节点可以变为最小生成树，那么1~n节点会被合并为一个连通分量
            # 而0索引虽然无用，但是也会自己形成一个连通分量，因此最终如果能形成最小生成树，则并查集中会有两个连通分量
            if ufs.cnt == 2:
                return min_cost

    # 如果最后连通图的个数大于2，证明不是所有节点都连上
    return -1


print(kruskal(n, items))
