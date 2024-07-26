""" 
题目解析和算法源码
华为OD机试 - 螺旋数字矩阵（Java & JS & Python & C）-CSDN博客

题目描述
疫情期间，小明隔离在家，百无聊赖，在纸上写数字玩。他发明了一种写法：

给出数字个数 n （0 < n ≤ 999）和行数 m（0 < m ≤ 999），从左上角的 1 开始，按照顺时针螺旋向内写方式，依次写出2,3,....,n，最终形成一个 m 行矩阵。

小明对这个矩阵有些要求：

每行数字的个数一样多
列的数量尽可能少
填充数字时优先填充外部
数字不够时，使用单个 * 号占位
输入描述
两个整数，空格隔开，依次表示 n、m

输出描述
符合要求的唯一矩阵

用例1
输入
9 4
输出
1 2 3
* * 4
9 * 5
8 7 6
说明
9个数字写出4行，最少需要3列

用例2
输入
3 5
输出
1
2
3
*
*
说明
3个数字写5行，只有一列，数字不够用*号填充

用例3
输入
120 7
输出
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 19
45 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 63 20
44 83 114 115 116 117 118 119 120 * * * * * * 99 64 21
43 82 113 112 111 110 109 108 107 106 105 104 103 102 101 100 65 22
42 81 80 79 78 77 76 75 74 73 72 71 70 69 68 67 66 23
41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24
"""


import math

n, rows = map(int, input().split())
cols = math.ceil(n / rows)

grid = [['*'] * cols for _ in range(rows)]

# 方法1:


def solution1():
    i, j = 0, 0
    top, bottom = 0, rows-1
    left, right = 0, cols-1
    num = 1
    while num <= n:
        # 上
        while num <= n and left <= j <= right:
            grid[i][j] = num
            j += 1
            num += 1
        top += 1
        j -= 1
        i += 1
        # 右
        while num <= n and top <= i <= bottom:
            grid[i][j] = num
            i += 1
            num += 1
        right -= 1
        i -= 1
        j -= 1
        # 下
        while num <= n and left <= j <= right:
            grid[i][j] = num
            j -= 1
            num += 1
        bottom -= 1
        j += 1
        i -= 1
        # 左
        while num <= n and top <= i <= bottom:
            grid[i][j] = num
            i -= 1
            num += 1
        left += 1
        i += 1
        j += 1
    for i in range(rows):
        print(' '.join(map(str, grid[i])))


# 方法2:（推荐）

def solution2():
    top, bottom = 0, rows-1
    left, right = 0, cols-1
    num = 1
    while num <= n:
        # 上
        for j in range(left, right+1):
            grid[top][j] = num
            num += 1
            if num > n:
                return
        top += 1

        # 右
        for i in range(top, bottom + 1):
            grid[i][right] = num
            num += 1
            if num > n:
                return
        right -= 1

        # 下
        for j in range(right, left-1, -1):
            grid[bottom][j] = num
            num += 1
            if num > n:
                return
        bottom -= 1

        # 左
        for i in range(bottom, top-1, -1):
            grid[i][left] = num
            num += 1
            if num > n:
                return
        left += 1

    for i in range(rows):
        print(' '.join(map(str, grid[i])))
