"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/127711317?ops_request_misc=&request_id=1b67f3f5f9dd4336a8d30b89eaca29bd&biz_id=&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~koosearch~default-1-127711317-null-null.268%5Ev1%5Econtrol&utm_term=%E8%AE%A1%E7%AE%97%E7%96%AB%E6%83%85&spm=1018.2226.3001.4450

题目描述
在一个地图中(地图由n*n个区域组成），有部分区域被感染病菌。 感染区域每天都会把周围（上下左右）的4个区域感染。 请根据给定的地图计算，多少天以后，全部区域都会被感染。 如果初始地图上所有区域全部都被感染，或者没有被感染区域，返回-1

输入描述
一行N*N个数字（只包含0,1，不会有其他数字）表示一个地图，数字间用,分割，0表示未感染区域，1表示已经感染区域 每N个数字表示地图中一行，输入数据共表示N行N列的区域地图。

例如输入1,0,1,0,0,0,1,0,1，表示地图

1,0,1
0,0,0
1,0,1
输出描述
一个整数，表示经过多少天以后，全部区域都被感染 1<=N<200

用例1
输入
1,0,1,0,0,0,1,0,1
输出
2
说明
1天以后，地图中仅剩余中心点未被感染；2天以后，全部被感染。

用例2
输入
0,0,0,0
输出
-1
说明
无感染区域

用例3
输入
1,1,1,1,1,1,1,1,1
输出
-1
说明
全部都感染
"""
import math

# 获取输入
arr = list(map(int, input().split(',')))


# 图的多源bfs(2种方式，一是改变值，一是用一个vis数组记录是否被污染，这里用改变矩阵值)
def solution():
    n = int(math.sqrt(len(arr)))
    grid = [[0] * n for _ in range(n)]
    # bfs队列
    q = []
    # 感染人数
    sick = 0
    # 字符串可转换为N*N的数组
    for i, num in enumerate(arr):
        x, y = divmod(i, n)
        grid[x][y] = num
        if num == 1:
            sick += 1
            q.append((x, y))

    # 如果初始地图上所有区域全部都被感染，或者没有被感染区域，返回-1
    if sick == 0 or sick == len(arr):
        return -1

    offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    days = 0
    # 注意这里循环条件有2个
    while q and sick < len(arr):
        new_q = []
        for x, y in q:
            for ox, oy in offsets:
                new_x = x + ox
                new_y = y + oy
                if not (0 <= new_x < n and 0 <= new_y < n) or grid[new_x][new_y] == 1:
                    continue
                
                # 添加新一轮被感染点
                grid[new_x][new_y] = 1
                sick += 1
                new_q.append((new_x, new_y))

        days += 1
        q = new_q

    return days


print(solution())
