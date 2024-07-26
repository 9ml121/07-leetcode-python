"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127711451

题目描述
在一个机房中，服务器的位置标识在 n*m 的整数矩阵网格中，1 表示单元格上有服务器，0 表示没有。如果两台服务器位于同一行或者同一列中紧邻的位置，则认为它们之间可以组成一个局域网。

请你统计机房中最大的局域网包含的服务器个数。

输入描述
第一行输入两个正整数，n和m，0<n,m<=100

之后为n*m的二维数组，代表服务器信息

输出描述
最大局域网包含的服务器个数。

用例1
输入
2 2
1 0
1 1
输出
3
说明
[0][0]、[1][0]、[1][1]三台服务器相互连接，可以组成局域网


"""
# todo F-图论\bfs_FloodFill\200.岛屿数量.py 变种题
import collections

# 获取输入
rows, cols = map(int, input().split())
grid = []
for i in range(rows):
    grid.append(list(map(int, input().split())))

# bfs解法
max_cnt = 0
def bfs():
    global max_cnt
    vis = [[False] * cols for _ in range(rows)]
    offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 or vis[i][j]:
                continue

            vis[i][j] = True
            cnt = 0
            dq = collections.deque([(i, j)])
            while dq:
                x, y = dq.popleft()
                cnt += 1
                for ox, oy in offsets:
                    new_x = x + ox
                    new_y = y + oy

                    if not (0 <= new_x < rows and 0 <= new_y < cols):
                        continue

                    if grid[new_x][new_y] == 0 or vis[new_x][new_y]:
                        continue

                    dq.append((new_x, new_y))
                    vis[new_x][new_y] = True
            max_cnt = max(max_cnt, cnt)

    return max_cnt


bfs()
print(max_cnt)
