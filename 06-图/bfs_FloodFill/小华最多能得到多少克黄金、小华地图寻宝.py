"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134674604

题目描述
小华按照地图去寻宝，地图上被划分成 m 行和 n 列的方格，横纵坐标范围分别是 [0, n-1] 和 [0, m-1]。

在横坐标和纵坐标的数位之和不大于 k 的方格中存在黄金（每个方格中仅存在一克黄金），但横坐标和纵坐标之和大于 k 的方格存在危险不可进入。小华从入口 (0,0) 进入，任何时候只能向左，右，上，下四个方向移动一格。

请问小华最多能获得多少克黄金？

输入描述
坐标取值范围如下：

0 ≤ m ≤ 50
0 ≤ n ≤ 50
k 的取值范围如下：

0 ≤ k ≤ 100
输入中包含3个字数，分别是m, n, k

输出描述
输出小华最多能获得多少克黄金

用例1
输入
40 40 18
输出
1484
用例2
输入
5 4 7
输出
20
"""
import collections

# 获取输入
cols, rows, k = map(int, input().split())


def cal(x: int, y: int):
    # 计算两个整数数位之和(或者用整数除10的方法)
    x, y = str(x), str(y)
    sz = max(len(x), len(y))
    x = x.rjust(sz, '0')
    y = y.rjust(sz, '0')
    ans = 0
    for i in range(sz):
        ans += (int(x[i]) + int(y[i]))
    return ans

# dfs和bfs都可以解决


def bfs():
    if rows == 0 or cols == 0:
        return 0

    dq = collections.deque([(0, 0)])
    offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    vis = [[False]*cols for _ in range(rows)]
    vis[0][0] = True
    ans = 0
    while dq:
        x, y = dq.popleft()
        ans += 1
        for ox, oy in offsets:
            new_x = x + ox
            new_y = y + oy
            if not (0 <= new_x < rows and 0 <= new_y < cols):
                continue

            if vis[new_x][new_y]:
                continue

            # 数位之和计算
            if cal(new_x, new_y) > k:
                continue

            dq.append((new_x, new_y))
            vis[new_x][new_y] = True
    return ans


print(bfs())
