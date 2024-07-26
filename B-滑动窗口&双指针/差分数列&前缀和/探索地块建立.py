"""
题目描述
给一块n*m的地块，相当于n*m的二维数组，每个元素的值表示这个小地块的发电量；
求在这块地上建立正方形的边长为c的发电站，发电量满足目标电量k的地块数量。

输入描述
第一行为四个按空格分隔的正整数，分别表示n, m , c k
后面n行整数，表示每个地块的发电量

输出描述
输出满足条件的地块数量

用例
输入	2 5 2 6
    1 3 4 5 8
    2 3 6 7 1
输出	4
说明	无
"""

'''
题目解析
本题最优解题思路是使用：二维矩阵前缀
此题用浮沉之外的思路: 前缀数组的长度比原始数组长度大1
'''

# 1.处理输入
# row, col, c, k = map(int, input().split())
# print(row, col, c, k)
row, col, c, k = 2, 5, 2, 6

# matrix = [list(map(int, input().split())) for _ in range(row)]
# print(matrix)
matrix = [[1, 3, 4, 5, 8],
          [2, 3, 6, 7, 1]]

# 2.todo 构建二维矩阵前缀和:  闭合区间 + 前缀数组的长度比原始数组长度大1
preSum = [[0] * (col + 1) for _ in range(row + 1)]
for i in range(1, row + 1):
    for j in range(1, col + 1):
        preSum[i][j] = preSum[i][j-1] + preSum[i-1][j] - preSum[i-1][j-1] + matrix[i-1][j-1]
print(preSum)
# [[0, 0, 0, 0, 0, 0],
#  [0, 1, 4, 8, 13, 21],
#  [0, 3, 9, 19, 31, 40]]

# 3.利用前缀和矩阵,计算满足正方形的边长为c，发电量满足目标电量k的地块数量
ans = 0
# todo:注意，这里最好是从正方形右下角坐标开始遍历，避免计算边界
for i in range(c, row + 1):
    for j in range(c, col + 1):
        res = preSum[i][j] - (preSum[i][j - c] + preSum[i - c][j]) + preSum[i - c][j - c]
        # print(res)
        if res >= k:
            ans += 1  

print(ans)
