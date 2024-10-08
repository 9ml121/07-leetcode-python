"""
题目解析和算法源码
华为OD机试 - 寻找最优的路测线路（Java & JS & Python & C）-CSDN博客

题目描述
评估一个网络的信号质量，其中一个做法是将网络划分为栅格，然后对每个栅格的信号质量计算。

路测的时候，希望选择一条信号最好的路线（彼此相连的栅格集合）进行演示。

现给出 R 行 C 列的整数数组 Cov，每个单元格的数值 S 即为该栅格的信号质量（已归一化，无单位，值越大信号越好）。

要求从 [0, 0] 到 [R-1, C-1]设计一条最优路测路线。返回该路线得分。

规则：

路测路线可以上下左右四个方向，不能对角
路线的评分是以路线上信号最差的栅格为准的，例如路径 8→4→5→9 的值为4，该线路评分为4。线路最优表示该条线路的评分最高。
输入描述
第一行表示栅格的行数 R

第二行表示栅格的列数 C

第三行开始，每一行表示栅格地图一行的信号值，如5 4 5

输出描述
最优路线的得分

备注
1 ≤ R，C ≤ 20
0 ≤ S ≤ 65535
用例1
输入
3
3
5 4 5
1 2 6
7 4 6
输出
4
说明
路线为：5→4→5→6→6

用例2
输入
6
5
3 4 6 3 4
0 2 1 1 7
8 8 3 2 7
3 2 4 9 8
4 1 2 0 0
4 6 5 4 3
输出
3
说明
路线为：3→4→6→3→4→7→7→8→9→4→3→8→8→3→4→4→6→5→4→3
"""

import heapq

# todo 单源最短路径问题（有向图） 贪心 + 堆
# Dijkstra算法变形

# 输入
r = int(input())
c = int(input())
# 每一行表示栅格地图一行的信号值，如5 4 5, 值越大信号越好
grid = [list(map(int, input().split())) for _ in range(r)]

# 输出：最优路线的得分（路线的评分是以路线上信号最差的栅格为准的）
# todo 1.构建dist权重数组 
# dist[i][j]代表从起点到grid[i][j]这个网格最差的信号分值
# dist初始值就是grid[i][j]
# 注意：这里也可以将二维数组转换为一维数组，降低空间复杂度
dist = grid.copy()
visited = [[False] * c for _ in range(r)]

# todo 2.优先队列实现bfs
maxHeap = [(-dist[0][0], 0, 0)]  # (最差信号，横坐标， 纵坐标)
visited[0][0] = True
offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]
while maxHeap:
    _, x, y = heapq.heappop(maxHeap) # bfs每次先弹出大顶堆中信号最差网格分值的最大值
    for ox, oy in offsets:
        nx = x + ox
        ny = y + oy

        # 越界，已经访问过
        if nx < 0 or nx >= r or ny < 0 or ny >= c or visited[nx][ny]:
            continue
        
        # 注意：这里是贪心思维，不用再判断其他路径
        dist[nx][ny] = min(dist[x][y], grid[nx][ny])  # 路线的评分是以路线上信号最差的栅格为准的
        heapq.heappush(maxHeap, (-dist[nx][ny], nx, ny))
        visited[nx][ny] = True

        # 一旦dist[r-1][c-1]确定了，即可停止Dijkstra算法，即不需要找到(0,0)到其余点的dist解
        if nx == r-1 and ny == c-1:
            break

print(dist[-1][-1])
