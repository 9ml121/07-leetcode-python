"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134759904?spm=1001.2014.3001.5502

OJ用例
题解 - 两个字符串间的最短路径问题 - Hydro

题目描述
给定两个字符串，分别为字符串 A 与字符串 B。

例如 A字符串为 "ABCABBA"，B字符串为 "CBABAC" 可以得到下图 m * n 的二维数组，定义原点为(0,0)，终点为(m,n)，水平与垂直的每一条边距离为1，映射成坐标系如下图。

从原点 (0,0) 到 (0,A) 为水平边，距离为1，从 (0,A) 到 (A,C) 为垂直边，距离为1；

假设两个字符串同一位置的两个字符相同，则可以作一个斜边，如 (A,C) 到 (B,B) 最短距离为斜边，距离同样为1。

作出所有的斜边如下图，(0,0) 到 (B,B) 的距离为：1 个水平边 + 1 个垂直边 + 1 个斜边 = 3。

image

根据定义可知，原点到终点的最短距离路径如下图红线标记，最短距离为9：

image

输入描述
空格分割的两个字符串 A 与字符串 B
字符串不为"空串"
字符格式满足正则规则：[A-Z]
字符串长度 < 10000

输出描述
原点到终点的最短距离

用例1
输入
ABC ABC
输出
3
用例2
输入
ABCABBA CBABAC
输出
9
"""
# todo 考察动态规划
# 输入：空格分割的两个字符串 A 与字符串 B
str1, str2 = input().split()

# 输出：原点到终点的最短距离
# 从原点到终点，有向右，向下，向右下3种方向可以选择
# 方法1: 超内存解法
def main():
    n1 = len(str1)
    n2 = len(str2)
    dp = [[0] * (n2+1) for _ in range(n1+1)]

    for i in range(1, n1+1):
        dp[i][0] = dp[i-1][0] + 1
    for j in range(1, n2+1):
        dp[0][j] = dp[0][j-1] + 1
    # print(dp)

    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
    # print(dp)
    print(dp[-1][-1])

# 方法2:动态规划+压缩数组(没有内存超限)
# Python相较于其他语言，性能差了一些，其他语言压缩数组解法可以不超时的应对10000 * 10000的极限用例

def main():
    n1 = len(str1)
    n2 = len(str2)
    # 初始时preRow记录第一行上各点到(0,0)点的最短距离，即为(0,0) -> (0,j) 的直线路径
    pre_row = [i for i in range(n2+1)]
    # 初始时curRow记录第二行上各点到(0,0)点的最短距离
    cur_row = [0] * (n2+1)

    for i in range(1, n1+1):
        cur_row[0] = i
        for j in range(1, n2+1):
            if str1[i-1] == str2[j-1]:
                cur_row[j] = pre_row[j-1] + 1
            else:
                cur_row[j] = min(cur_row[j-1], pre_row[j]) + 1

        # 滚动数组，注意：不能直接复制！！
        # pre_row = cur_row
        for j in range(n2):
            pre_row[j] = cur_row[j]

    return cur_row[-1]


print(main())
