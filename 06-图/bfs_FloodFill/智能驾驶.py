"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135049730?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22135049730%22%2C%22source%22%3A%22qfc_128220%22%7D

题目描述
有一辆汽车需要从 m * n 的地图左上角（起点）开往地图的右下角（终点），去往每一个地区都需要消耗一定的油量，加油站可进行加油。

请你计算汽车确保从从起点到达终点时所需的最少初始油量。

说明：

智能汽车可以上下左右四个方向移动
地图上的数字取值是 0 或 -1 或 正整数：
-1 ：表示加油站，可以加满油，汽车的油箱容量最大为100；
0 ：表示这个地区是障碍物，汽车不能通过
正整数：表示汽车走过这个地区的耗油量
如果汽车无论如何都无法到达终点，则返回 -1
输入描述
第一行为两个数字，M，N，表示地图的大小为 M * N

0 < M,N ≤ 200
后面一个 M * N 的矩阵，其中的值是 0 或 -1 或正整数，加油站的总数不超过 200 个

输出描述
如果汽车无论如何都无法到达终点，则返回 -1

如果汽车可以到达终点，则返回最少的初始油量

用例1
输入
2,2
10,20
30,40
输出
70
说明
行走的路线为：右→下

用例2
输入
4,4
10,30,30,20
30,30,-1,10
0,20,20,40
10,-1,30,40
输出
70
说明
行走的路线为：右→右→下→下→下→右

用例3
输入
4,5
10,0,30,-1,10
30,0,20,0,20
10,0,10,0,30
10,-1,30,0,10
输出
60
说明
行走的路线为：下→下→下→右→右→上→上→上→右→右→下→下→下

用例4
输入
4,4
10,30,30,20
30,30,20,10
10,20,10,40
10,20,30,40
输出
-1
说明
无论如何都无法到达终点
"""

import collections
import heapq
"""
测试用例：注意可以走回头路
3,3
10,-1,40
30,0,50
50,-1,40
"""

# 输入
rows, cols = map(int, input().split(','))
grid = [list(map(int, input().split(','))) for _ in range(rows)]

# 输出：计算汽车确保从从起点到达终点时所需的最少初始油量
offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
# todo dist[i][j]表示从起点到达grid[i][j]这个位置至少需要的初始油量, 剩余油量, 是否加过油
dist = [[[101, 0, False] for _ in range(cols)] for _ in range(rows)]


def solution():
    start = grid[0][0]
    # 0 ：表示这个地区是障碍物，汽车不能通过
    if start == 0 or grid[-1][-1] == 0:
        return -1

    # -1 ：表示加油站，可以加满油，汽车的油箱容量最大为100；
    if start == -1:
        dist[0][0] = [0, 100, True]
    else:
        # 正整数：表示汽车走过这个地区的耗油量
        dist[0][0] = [start, 0, False]

    # 改用优先队列实现(注意这里用普通双向队列有测试用例不能通过)
    # dq = collections.deque([(0, 0)])
    pq = [(dist[0][0], 0, 0)]
    while pq:
        _, x, y = heapq.heappop(pq)
        for ox, oy in offsets:
            nx, ny = x+ox, y+oy
            # 越界，障碍物
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] == 0:
                continue
            
            num = grid[nx][ny]
            init, remain, is_add = dist[x][y]
            if num == -1:
                # 加油站
                remain = 100
                is_add = True
            elif num > 0:
                # 经过这个地区的耗油量
                if not is_add:
                    # 之前没有加过油
                    init += num
                    if init > 100:
                        continue
                else:
                    # 已经加过油
                    remain -= num
                    if remain < 0:
                        continue
    
            # 注意：这里上面测试用例不能通过
            if init < dist[nx][ny][0] or remain > dist[nx][ny][1]:
                if (nx, ny) == (rows-1, cols-1):
                    return init
                dist[nx][ny][0] = init
                dist[nx][ny][1] = remain
                dist[nx][ny][2] = is_add
                heapq.heappush(pq, (init, nx, ny))

    return -1


print(solution())
