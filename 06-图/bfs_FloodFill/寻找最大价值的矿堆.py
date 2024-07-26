"""
题目描述
给你一个由 '0' (空地)、'1' (银矿)、'2'(金矿) 组成的的地图，矿堆只能由上下左右相邻的金矿或银矿连接形成。
超出地图范围可以认为是空地。

假设银矿价值1，金矿价值2 ，请你找出地图中最大价值的矿堆并输出该矿堆的价值。

输入描述
地图元素信息如：
22220
00000
00000
11111

地图范围最大 300*300
0 ≤ 地图元素 ≤ 2

输出描述
矿堆的最大价值

用例
输入
22220
00000
00000
01111
输出	8
说明	无

输入
22220
00020
00010
01111
输出	15
说明	无

输入
20000
00020
00000
00111
输出	3
说明	无
"""


# todo F-图论\bfs_FloodFill\200.岛屿数量.py 变种题
import collections


def getResult(grid: list):
    rows, cols = len(grid), len(grid[0])
    # 找出地图中最大价值的矿堆并输出该矿堆的价值。
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    ans = 0  # 最大价值矿堆

    for i in range(rows):
        for j in range(cols):
            val = grid[i][j]
            res = 0  # 记录每块金银矿的总价值
            dq = collections.deque()  # 记录每块矿地有价值点的坐标
            if val != '0':
                res += int(val)
                # 统计过的坐标值，更改为'0'，避免重复遍历, 也可以用used数组或者集合标记
                grid[i][j] = '0'  
                dq.append((i, j))

            # dfs:搜索坐标4个方向，有发现金银坐标，就加进结果
            while dq:
                x, y = dq.popleft()  
                for ox, oy in offsets:
                    nx = x + ox
                    ny = y + oy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '0':
                        res += int(grid[nx][ny])
                        grid[nx][ny] = '0'
                        dq.append((nx, ny))
            # 找不到新价值坐标，更新res
            ans = max(ans, res)
    # 返回结果
    return ans


if __name__ == '__main__':
    # 获取输入
    # grid = []
    # while True:
    #     line = input()
    #     if line == '':
    #         print(getResult(grid))
    #         break
    #     else:
    #         grid.append(list(line))
    #
    # grid = [['2', '2', '2', '2', '0'],
    #         ['0', '0', '0', '2', '0'],
    #         ['0', '0', '0', '1', '0'],
    #         ['0', '1', '1', '1', '1']]

    grid = [['2', '0', '0', '0', '0'],
            ['0', '0', '0', '2', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '1', '1', '1']]

    # 调用算法
    print(getResult(grid))
