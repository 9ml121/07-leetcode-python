"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/135062353?spm=1001.2014.3001.5502

题目描述
宝宝和妈妈参加亲子游戏，在一个二维矩阵（N*N）的格子地图上，宝宝和妈妈抽签决定各自的位置，地图上每个格子有不同的糖果数量，部分格子有障碍物。

游戏规则是妈妈必须在最短的时间（每个单位时间只能走一步）到达宝宝的位置，路上的所有糖果都可以拿走，不能走障碍物的格子，只能上下左右走。

请问妈妈在最短到达宝宝位置的时间内最多拿到多少糖果（优先考虑最短时间到达的情况下尽可能多拿糖果）。

输入描述
第一行输入为 N，N 表示二维矩阵的大小

之后 N 行，每行有 N 个值，表格矩阵每个位置的值，其中：

-3：妈妈
-2：宝宝
-1：障碍
≥0：糖果数（0表示没有糖果，但是可以走）
输出描述
输出妈妈在最短到达宝宝位置的时间内最多拿到多少糖果，行末无多余空格

备注
地图最大 50*50

用例1
输入
4
3 2 1 -3
1 -1 1 1
1 1 -1 2
-2 1 2 3
输出
9
说明
此地图有两条最短路径可到达宝宝位置，绿色线和黄色线都是最短路径6步，但黄色拿到的糖果更多，9个。

image

用例2
输入
4
3 2 1 -3
-1 -1 1 1
1 1 -1 2
-2 1 -1 3
输出
-1
说明
此地图妈妈无法到达宝宝位置

image
"""


# 输入
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# 输出：妈妈在最短到达宝宝位置的时间内最多拿到多少糖果
offsets = [(0, -1), (0, 1), (-1, 0), (1, 0)]
ans = 0

# todo dist[i][j]表示妈妈到达grid[i][j]这个位置可以获得的最大糖果数
# 初始化为-1代表妈妈没有到达过这个位置
dist = [[-1] * n for _ in range(n)]

def solution():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == -3: # 妈妈位置
                dist[i][j] = 0
                return bfs(i, j)


def bfs(i, j):
    global ans
    # todo 注意：这里dq不用记录step,因为最后结果是要找最快时间能否到达宝宝位置，可以获得的最大糖果数
    dq = [(i, j)]
    while dq:
        nxt_dq = []
        flag = False # flag用来标记是否已经到达宝宝位置
        for x, y in dq:
            for ox, oy in offsets:
                nx, ny = x+ox, y+oy
                # 越界, 障碍物
                if not (0 <= nx < n and 0 <= ny < n) or grid[nx][ny] = -1:
                    continue

                # 糖果/宝宝/重复路 3种可能
                # todo 需要判断从不同路径用相同步骤到达改点能获得的最大糖果数
                if dist[nx][ny] == -1:
                    # 第一次遍历，才需要加入队列
                    nxt_dq.append((nx, ny))

                # todo 更新dist路径值，因为每个位置可能从多个其他位置到达，所以要取能获得糖果最多的那个值
                # 注意：因为宝宝位置值为-2，到达这个位置新加的糖果数应该为0
                dist[nx][ny] = max(dist[nx][ny], dist[x][y] + max(0, dist[nx][ny]))

                # 宝宝
                if grid[nx][ny] == -2:
                    flag = True
                    ans = dist[nx][ny]

        # 注意：因为最后结果是要找最快时间能否到达宝宝位置，可以获得的最大糖果数，所以一旦flag为True,就需要返回结果
        if flag:
            return ans
        else:
            dq = nxt_dq
    # 不可能到达
    return -1


print(solution())
