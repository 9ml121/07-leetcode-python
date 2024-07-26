""" 
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134633873?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522170342894216800186566798%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&request_id=170342894216800186566798&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~blog~first_rank_ecpm_v1~rank_v31_ecpm-1-134633873-null-null.nonecase&utm_term=%E5%9B%B4%E6%A3%8B%E7%9A%84&spm=1018.2226.3001.4450

题目描述
围棋棋盘由纵横各19条线垂直相交组成，棋盘上一共19 x 19 = 361 个交点，对弈双方一方执白棋，一方执黑棋，落子时只能将棋子置于交点上。

“气”是围棋中很重要的一个概念，某个棋子有几口气，是指其上下左右方向四个相邻的交叉点中，有几个交叉点没有棋子，由此可知：

在棋盘的边缘上的棋子最多有 3 口气（黑1），在棋盘角点的棋子最多有2口气（黑2），其他情况最多有4口气（白1）
所有同色棋子的气之和叫做该色棋子的气，需要注意的是，同色棋子重合的气点，对于该颜色棋子来说，只能计算一次气，比如下图中，黑棋一共4口气，而不是5口气，因为黑1和黑2中间红色三角标出来的气是两个黑棋共有的，对于黑棋整体来说只能算一个气。
本题目只计算气，对于眼也按气计算，如果您不清楚“眼”的概念，可忽略，按照前面描述的规则计算即可。
image

现在，请根据输入的黑棋和白棋得到坐标位置，计算黑棋和白棋一共各有多少气？

输入描述
输入包含两行数据，如：

0 5 8 9 9 10 5 0 9 9 9 8

每行数据以空格分隔，数据个数是2的整数倍，每两个数是一组，代表棋子在棋盘上的坐标；
坐标的原点在棋盘左上角点，第一个值是行号，范围从0到18；第二个值是列号，范围从0到18。
举例说明：第一行数据表示三个坐标（0, 5）、(8, 9)、(9, 10)
第一行表示黑棋的坐标，第二行表示白棋的坐标。
题目保证输入两行数据，无空行且每行按前文要求是偶数个，每个坐标不会超出棋盘范围。
输出描述
8 7

两个数字以空格分隔，第一个数代表黑棋的气数，第二个数代表白棋的气数。

用例1
输入
0 5 8 9 9 10
5 0 9 9 9 8
输出
8 7
说明
如果将输入数据放到棋盘上

image

数数黑棋一共8口气，数数白棋一共7口气。
"""

# 遍历方法1:
def solution1():
    blacks = list(map(int, input().split()))
    whites = list(map(int, input().split()))

    grid = [[0] * 19 for _ in range(19)]  # 0代表空格
    for i in range(0, len(blacks), 2):
        grid[blacks[i]][blacks[i+1]] = 1  # 1代表白棋

    for i in range(0, len(whites), 2):
        grid[whites[i]][whites[i+1]] = 2  # 2代表黑棋

    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]


    def inArea(x, y):
        return 0 <= x < 19 and 0 <= y < 19


    cnts_black, cnts_white = 0, 0
    visited_black = set()
    visited_white = set()
    for i in range(19):
        for j in range(19):
            if grid[i][j] == 1:  # 黑色
                for ox, oy in offsets:
                    x, y = i + ox, j + oy
                    if inArea(x, y) and grid[x][y] == 0 and (x, y) not in visited_black:
                        cnts_black += 1
                        visited_black.add((x, y))
            elif grid[i][j] == 2:  # 白色
                for ox, oy in offsets:
                    x, y = i + ox, j + oy
                    if inArea(x, y) and grid[x][y] == 0 and (x, y) not in visited_white:
                        cnts_white += 1
                        visited_white.add((x, y))

    print(cnts_black, cnts_white, sep=' ')
    # print(f'{cnts_black} {cnts_white}')


# 遍历方法2:
# 输入获取
black = list(map(int, input().split()))
white = list(map(int, input().split()))


# 算法入口
def getResult():
    # 定义棋盘，没有棋子用0表示
    board = [[0] * 19 for _ in range(19)]

    for i in range(0, len(black), 2):
        x = black[i]
        y = black[i + 1]
        board[x][y] = 1  # 棋盘中黑棋用1表示

    for i in range(0, len(white), 2):
        x = white[i]
        y = white[i + 1]
        board[x][y] = 2  # 棋盘中白棋用2表示

    # 黑棋的气数
    black_liberty_count = 0
    # 白棋的气数
    white_liberty_count = 0

    # 上下左右四个方向的偏移量
    offsets = ((-1, 0), (1, 0), (0, -1), (0, 1))

    for i in range(19):
        for j in range(19):
            # 如果当前位置没有棋子，则可能是黑棋或白棋的气
            if board[i][j] == 0:
                # 当前位置是否为黑棋的气
                isBlackLiberty = False
                # 当前位置是否白棋的气
                isWhiteLiberty = False

                # 若为黑棋或者白棋的气，则当前位置的上下左右的位置上必有黑棋或白棋
                for offsetX, offsetY in offsets:
                    newI = i + offsetX
                    newJ = j + offsetY

                    # 若当前位置的上下左右的位置越界，则不考虑
                    if newI < 0 or newI >= 19 or newJ < 0 or newJ >= 19:
                        continue

                    # 若当前位置的上下左右的位置存在黑棋，则当前位置为黑棋的气
                    isBlackLiberty = isBlackLiberty or (board[newI][newJ] == 1)
                    # 若当前位置的上下左右的位置存在白棋，则当前位置为白棋的气
                    isWhiteLiberty = isWhiteLiberty or (board[newI][newJ] == 2)

                if isBlackLiberty:
                    black_liberty_count += 1

                if isWhiteLiberty:
                    white_liberty_count += 1

    return f"{black_liberty_count} {white_liberty_count}"


# 算法调用
print(getResult())
