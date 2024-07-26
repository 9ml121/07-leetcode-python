"""
题目描述
某长方形停车场，每个车位上方都有对应监控器，当且仅当在当前车位或者前后左右四个方向任意一个车位范围停车时，监控器才需要打开；
给出某一时刻停车场的停车分布，请统计最少需要打开多少个监控器；

输入描述
第一行输入m，n表示长宽，满足1 < m,n <= 20；
后面输入m行，每行有n个0或1的整数，整数间使用一个空格隔开，表示该行已停车情况，其中0表示空位，1表示已停；

输出描述
最少需要打开监控器的数量；

用例
输入	3 3
    0 0 0
    0 1 0
    0 0 0
输出	5
说明	无
"""


# todo 二维矩阵每个坐标4个方向遍历模板

def getResult(grid):
    row, col = len(grid), len(grid[0])
    # 四个方向偏移坐标
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    cnt = 0
    for x in range(row):
        for y in range(col):
            # 0表示空位，1表示已停
            # 当且仅当在当前车位或者前后左右四个方向任意一个车位范围停车时，监控器才需要打开；
            # 如果只遍历坐标值为1的，需要更改四个方向为0的值为一个其他数，比较麻烦
            # 如果每个坐标都遍历，需要判断4个方向是否有1
            if grid[x][y] == '1':
                cnt += 1
            elif grid[x][y] == '0':
                for offsetX, offsetY in offsets:
                    newX = x + offsetX
                    newY = y + offsetY
                    if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == '1':
                        cnt += 1
    return cnt


if __name__ == '__main__':
    # 获取输入
    # 第一行输入m，n表示长宽, 长对应二维矩阵col长度，宽对应二维矩阵row长度
    # col, row = map(int, input().split())
    # grid = [input().split() for _ in range(row)]
    col, row = 3, 3
    grid = [['0', '0', '0'], ['0', '1', '0'], ['0', '0', '0']]
    print(getResult(grid))
