"""
题目来源
http://poj.org/problem?id=3311

题目描述
Pizazz披萨店以尽可能快地将披萨送到顾客手中而自豪。

不幸的是，由于削减开支，他们只能雇一个司机来送货。

司机将等待 1 个或更多 (最多10个) 订单被下达后再开始送餐。

不用说，他想要走最短的路线来运送这些食物并返回披萨店，即使这意味着在途中不止一次地经过同一地点或披萨店。

他委托你写一个程序来帮助他。

输入描述
输入将由多个测试用例组成。

第一行将包含单个整数 n，表示要送货的订单数量，其中 1 ≤ n ≤ 10。
在此之后，将有 n + 1 行，每一行包含 n + 1 个整数，表示从披萨店 (编号为0) 到 n 个位置 (编号为 1 到 n)  之间的送餐时间。

第 i 行上的第 j 个值表示直接从位置 i 到位置 j 而不经过沿途任何其他位置的时间。
请注意，由于不同的速度限制，交通信号灯等，经过其他位置的中转，可能实现更快地从 i 到 j。

此外，时间值可能不对称，即直接从位置 i 到 j 的时间可能与直接从位置 j 到 i 的时间不相同。

输入值 n = 0 将终止输入。

输出描述
对于每个测试用例，您应该输出单个数字，指示交付所有披萨并返回披萨店所需的最短时间。

用例
输入	3
0 1 10 10
1 0 1 2
10 1 0 10
10 2 10 0
0
输出	8
说明	无
"""


'''
题目解析
本题第二行~倒数第二行的输入其实就是一个 (n+1) * (n+1) 的邻接矩阵，我们定义其为dist矩阵。

dist[i][j] 表示客户位置 i 到 客户位置 j 的距离。

本题需要我们帮助司机找到一条最短路径，该最短路径需要满足：

从披萨店（位置0）出发，最终返回披萨店
经过所有客户位置，每个客户位置可以经过不止一次
首先，这题需要我们经过所有客户位置，因此我们对 1~n 客户位置求解全排列，每一个全排列即代表一种送餐策略路径，比如n=3，则有以下送餐策略路径：

1->2->3
1->3->2
2->1->3
2->3->1
3->1->2
3->2->1
我们在这些全排列首尾加上0，即可得所有送餐策略路径：

0->1->2->3->0
0->1->3->2->0
0->2->1->3->0
0->2->3->1->0
0->3->1->2->0
0->3->2->1->0
由于本题的 1 ≤ n ≤ 10 ，因此全排列求解不会超时。

得到所有的送餐策略路径后，我们需要求解每种策略路径对应的送餐距离，

如果想要每种策略的送餐距离尽可能小，则我们应该保证路径中相邻两点之间的距离尽可能的小。

而求解图中任意两点间的最短距离，最佳策略是使用floyd算法。

关于floyd算法可以看下：最短路径算法全套(floyed+dijstra+Bellman+SPFA)_哔哩哔哩_bilibili

最终，我们基于floyd算法，求得上面每个全排列路径的最短距离，在这些最短距离中最小的即为题解。
'''


# floyd算法求解图中任意两点之间的最短路径


import sys
def floyd():
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                # newDist是经过k后，i->j的距离
                newDist = dist[i][k] + dist[k][j]
                # 如果newDist是i->j的更短路径
                if newDist < dist[i][j]:
                    # 则更新i->j的最短距离
                    dist[i][j] = newDist
                    # 且此更短距离需要经过k, path[i][j]即记录 i->j 最短距离下需要经过点 k
                    path[i][j] = k


def dfs(pre, sumDis, used, level):
    """
    找一条经过所有点的最短路径，我们可以求解所有点形成的全排列，每一个全排列都对应一条经过所有点的路径，只是经过点的先后顺序不同 //
    求某个全排列过程中，可以通过dist数组，累计上一个点i到下一个点j的最短路径dist[i][j]
    :param pre: 上一个点, 初始为0，表示从披萨店出发
    :param sumDis: 当前全排列路径累计的路径权重
    :param used: 全排列used数组，用于标记哪些点已使用过
    :param level: 用于记录排列的长度
    """
    global ans

    if level == n:
        # 此时pre是最后一个客户所在点，送完最后一个客户后，司机需要回到披萨店，因此最终累计路径权重为 sum + dist[pre][0]
        # 我们保留最小权重路径
        ans = min(ans, sumDis + dist[pre][0])
        return

    for i in range(1, n + 1):
        if used[i]:
            continue

        used[i] = True
        dfs(i, sumDis + dist[pre][i], used, level + 1)
        used[i] = False


while True:
    n = int(input())

    if n == 0:
        break

    # floyd算法需要基于dist和path矩阵求解
    # dist[i][j] 用于记录点 i->j 的最短距离，初始时等价于邻接矩阵
    dist = [list(map(int, input().split())) for _ in range(n + 1)]
    # path[i][j] 用于记录点 i->j 最短距离情况下需要经过的中转点，初始时默认任意两点间无中转点，即默认path[i][j] = -1
    path = [[-1] * (n + 1) for _ in range(n + 1)]

    # floyd算法调用
    floyd()

    # ans记录经过所有点后回到出发点的最短距离
    ans = sys.maxsize
    # 全排列模拟经过所有点的路径
    dfs(0, 0, [False] * (n + 1), 0)

    print(ans)
