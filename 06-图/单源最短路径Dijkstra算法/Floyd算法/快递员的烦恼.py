"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134899999?spm=1001.2014.3001.5502

OJ用例
题解 - 快递员的烦恼 - Hydro

题目描述
快递公司每日早晨，给每位快递员推送需要送到客户手中的快递以及路线信息，快递员自己又查找了一些客户与客户之间的路线距离信息，请你依据这些信息，给快递员设计一条最短路径，告诉他最短路径的距离。

注意：
不限制快递包裹送到客户手中的顺序，但必须保证都送到客户手中
用例保证一定存在投递站到每位客户之间的路线，但不保证客户与客户之间有路线，客户位置及投递站均允许多次经过
所有快递送完后，快递员需回到投递站

输入描述
首行输入两个正整数n、m

接下来 n 行，输入快递公司发布的客户快递信息，格式为：
    客户id 投递站到客户之间的距离distance

再接下俩的 m 行，是快递员自行查找的客户与客户之间的距离信息，格式为
    客户id1 客户id2 distance

在每行数据中，数据与数据之间均以单个空格分隔

规格：

0 < n ≤ 10
0 ≤ m ≤ 10
0 < 客户id ≤ 1000
0 < distance ≤ 10000

输出描述
最短路径距离，如无法找到，请输出-1

用例1
输入
2 1
1 1000
2 1200
1 2 300
输出
2500
说明
路径1：快递员先把快递送到客户1中，接下来直接走客户1到客户2之间的直通路线，最后走投递站和客户2之间的路，回到投递站，距离为 1000 + 300 + 1200 = 2500

路径2：快递员先把快递送到客户1手中，接下来回到快递站，再出发把客户2的快递送过去，再回到快递站，距离为 1000 + 1000 + 1200 + 1200 = 4400

路径3：快递员先把快递送到客户2手中，接下来直接走客户2到客户1之间的直通线路，最后走投递站和客户1之间的路，回到投递站，距离为 1200 + 300 + 1000 = 2500

其他路径......

所有路径中，最短路径距离为 2500

用例2
输入
5 1
5 1000
9 1200
17 300
132 700
500 2300
5 9 400
输出
9200
说明
在所有可行的路径中，最短路径长度为 1000 + 400 + 1200 + 300 + 300 + 700 + 700 + 2300 + 2300 = 9200
"""


# 输入
n, m = map(int, input().split())
# n行，快递公司发布的客户信息：客户id + 投递站到客户的距离dist
info1 = [list(map(int, input().split())) for _ in range(n)]
# m行，客户与客户之间的距离信息：客户id1 + 客户id2 + dist
info2 = [list(map(int, input().split())) for _ in range(m)]

# 输出：快递员最短路径距离，无法找到，输出-1
ans = float('inf')
# dist[i][j]代表两个地点之间的最短路径, 初始化为最大值
dist = [[float('inf')] * (n+1) for _ in range(n+1)]
# path[i][j]代表两个地点之间最短路径需要经过的中转点, 初始值设为-1，代表没有中转点
path = [[-1] * (n+1) for _ in range(n+1)]


def main():
    # 快递公司编号设为0， 客户id需要离散化为[1..n]
    # dist数组初始化设置为两个地点查询到的距离信息
    dic = {}
    for i in range(1, n+1):
        idx, val = info1[i-1]
        dic[idx] = i
        # 快递点到客户的距离
        dist[0][i] = val
        dist[i][0] = val

    # 客户与客户之间的距离
    for i in range(m):
        idx1, idx2, val = info2[i]
        i1 = dic[idx1]
        i2 = dic[idx2]
        dist[i1][i2] = val
        dist[i2][i1] = val

    # 调用floyd算法, 更新dist和path数组
    floyd()

    # 调用全排列算法，更新要求的最短路径
    dfs(0, [False] * (n+1), 0, 0)

    return ans


def floyd():
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                # 求客户i和客户j经过中转点k的路径
                cur_dist = dist[i][k] + dist[k][j]
                if cur_dist < dist[i][j]:
                    dist[i][j] = cur_dist
                    path[i][j] = k


def dfs(pre, vis, level, sumDist):
    """
    找一条经过所有点的最短路径，我们可以求解所有点形成的全排列，每一个全排列都对应一条经过所有点的路径，只是经过点的先后顺序不同 //
    求某个全排列过程中，可以通过dist数组，累计上一个点i到下一个点j的最短路径dist[i][j]

    @pre: 路径前一个客户id，初始值为快递站点0
    @vis: 标记全排列当前路径哪些客户id送过，初始化为[False] * (n+1)
    @level: 已经送达的客户数量，初始化为0，当到达n,就需要return
    @sumDist: 当前全排列路径已送达客户的总距离
    """
    global ans
    if level == n:
        # 最后一个客户，必然要返回快递站点0
        ans = min(ans, sumDist + dist[pre][0])
        return

    for i in range(1, n+1):
        if vis[i]:
            continue

        vis[i] = True
        dfs(i, vis, level+1, sumDist + dist[pre][i])
        vis[i] = False


print(main())
