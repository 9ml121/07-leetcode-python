"""
题目描述
幻方（Magic Square）是一个由1~n²，共N²个整数构成的N*N矩阵，满足每行、列和对角线上的数字和相等。

上回你已经帮助小明将写错一个数字的幻方进行了修复，小明在感谢之余也想进一步试试你的水平，于是他准备了有两个数字发生了位置交换的幻方。

你可以把这两个交换的数字找出来并且改正吗？

输入描述
第一行输入一个整数N，代表带校验幻方的阶数（3 ≤ n ＜ 50）

接下来的N行，每行N个整数，空格隔开（1 ≤ 每个整数 ≤ n²）

输出描述
输出两行，代表两条纠正信息，注意先输出行号小的，若行号相同则先输出列好小的

每行输出空格隔开的三个整数，分别是：出错行号、出错列号、应填入的数字（末尾无空格）

用例
输入	3
    8 1 9
    3 5 7
    4 6 2

输出	1 3 6
    3 2 9
说明	无
"""

'''
https://fcqian.blog.csdn.net/article/details/129858011
本题是有最佳解题策略的，这个策略和幻方的一个特性有关：
    幻方中每一条直线上的数的和叫作幻和。
    幻和 = 所有数的和 ÷ 阶数

当我们知道幻和后，就可以很轻易找出发生交换的两个点所在的行列，比如用例1中，我们遍历所有行、所有列后，可以得出不正确的行、列（即行和或列和不等于幻和的行、列）
'''

# 输入获取
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


# 求对角线的和（右上，到左下）
def getDiagonalSum2():
    total = 0
    for i in range(n):
        total += matrix[i][n - 1 - i]
    return total


# 求对角线的和（左上，到右下）
def getDiagonalSum1():
    total = 0
    for i in range(n):
        total += matrix[i][i]
    return total


# 求对应列的和
def getColSum(c):
    total = 0
    for r in range(n):
        total += matrix[r][c]
    return total


# 求对应行的和
def getRowSum(r):
    return sum(matrix[r])


# 将一维坐标解析为二维坐标
def getPos(pos):
    x = pos // n
    y = pos % n
    return [x, y]


def isValid(pos1, pos2, magic_sum):
    # 获取可能出错的两个点的坐标
    x1, y1 = pos1
    x2, y2 = pos2

    # 交换可能出错的两个点的值
    matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]

    # 首先判断两个对角线和是否等于幻和
    ans = magic_sum == getDiagonalSum1() and magic_sum == getDiagonalSum2()

    # 判断每一行的和是否相等
    if ans:
        for r in range(n):
            if getRowSum(r) != magic_sum:
                ans = False
                break

    # 判断每一列的和是否相等
    if ans:
        for c in range(n):
            if getColSum(c) != magic_sum:
                ans = False
                break

    # 如果所有行、列、对角线都相等，则返回对应交换位置
    if ans:
        if pos1 < pos2:
            print(f"{x1 + 1} {y1 + 1} {matrix[x1][y1]}")
            print(f"{x2 + 1} {y2 + 1} {matrix[x2][y2]}")
        else:
            print(f"{x2 + 1} {y2 + 1} {matrix[x2][y2]}")
            print(f"{x1 + 1} {y1 + 1} {matrix[x1][y1]}")
    else:
        # 否则复原交换位置
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]

    return ans


# 算法入口
def getResult():
    # 计算幻和
    magic_sum = 0
    for i in range(n):
        for j in range(n):
            magic_sum += matrix[i][j]
    magic_sum /= n

    # 记录 和不正确的行
    rows = []
    # 记录 和不正确的列
    cols = []

    for row in range(n):
        if getRowSum(row) != magic_sum:
            rows.append(row)  # 记录行号

    for col in range(n):
        if getColSum(col) != magic_sum:
            cols.append(col)  # 记录列号

    # 两点处于同一行，不同列
    if len(rows) == 0:
        # 则两点的行坐标可能是任意一行
        rows = [i for i in range(n)]

    # 两点处于同一列，不同行
    if len(cols) == 0:
        # 则两点的列坐标可能是任意一列
        cols = [i for i in range(n)]

    # 行号 x 列号，就可以组合出坐标
    positions = []
    for r in rows:
        for c in cols:
            positions.append((r, c))

    # 组合两点，尝试交换
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            if isValid(positions[i], positions[j], magic_sum):
                return


# 算法调用
getResult()
