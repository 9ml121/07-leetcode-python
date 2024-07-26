"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/128169190

题目描述
输入一行字符串，字符串可转换为N*N的数组，数组可认为是一个水域，判断多少天后，水域被全部污染。 数组中只有0和1，0表示纯净，1表示污染，每天只可污染上下左右的水域，如果开始全部被污染，或永远无法污染，则返回-1。

用例1
输入
1,0,1,0,0,0,1,0,1
输出
2
说明
输入转化为数组为：

1 0 1

0 0 0

1 0 1

第一天后水域变为

1 1 1

1 0 1

1 1 1

第二天全部被污染

用例2
输入
0,0,0,0
输出
-1
"""

# 类似题：
# 计算疫情扩散时间.py
# 994. 腐烂的橘子.py
import math

# 获取输入
# 字符串可转换为N*N的数组
arr = list(map(int, input().split(',')))


# bfs算法(2种方式，一是改变值，一是用一个vis数组记录是否被污染，这里用vis数组)
def solution():
    n = int(math.sqrt(len(arr)))
    grid = [[0] * n for _ in range(n)]
    # bfs队列
    dq = []
    # vis数组记录grid[i][j]是否被污染
    vis = [[False] * n for _ in range(n)]
    dirty = 0
    for i, num in enumerate(arr):
        x, y = divmod(i, n)
        grid[x][y] = num
        if num == 1:
            # 污染数量
            dirty += 1
            dq.append((x, y))
            vis[x][y] = True
            
    # 如果开始全部被污染，或永远无法污染，则返回-1
    if dirty == 0 or dirty == len(arr):
        return -1

    # bfs
    offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    days = 0
    while dq:
        new_dq = []
        for x, y in dq:
            for ox, oy in offsets:
                new_x = x + ox
                new_y = y + oy
                if not (0 <= new_x < n and 0 <= new_y < n) or vis[new_x][new_y]:
                    continue

                dirty += 1
                vis[new_x][new_y] = True
                new_dq.append((new_x, new_y))

        days += 1
        if dirty == len(arr):
            # 注意：一发现所有都被污染，就直接返回days
            return days
        dq = new_dq

    return -1


print(solution())
