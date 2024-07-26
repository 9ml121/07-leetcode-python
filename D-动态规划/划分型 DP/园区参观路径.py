"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134635868?spm=1001.2014.3001.5502

OJ用例
题解 - 园区参观路径 - Hydro

题目描述
园区某部门举办了Family Day，邀请员工及其家属参加；

将公司园区视为一个矩形，起始园区设置在左上角，终点园区设置在右下角；

家属参观园区时，只能向右和向下园区前进，求从起始园区到终点园区会有多少条不同的参观路径。

image

输入描述
第一行为园区的长和宽；

后面每一行表示该园区是否可以参观，0表示可以参观，1表示不能参观

输出描述
输出为不同的路径数量

用例1
输入
3 3
0 0 0
0 1 0
0 0 0
输出
2
"""

# todo 动态规划
# 类似：D-动态规划\路径计数问题\63. 不同路径 II.py

# 输入
# 第一行为园区的长和宽；代表行和列
m, n = map(int, input().split())
# 后面每一行表示该园区是否可以参观，0表示可以参观，1表示不能参观
grid= [list(map(int, input().split())) for _ in range(m)]

# 求从起始园区到终点园区会有多少条不同的参观路径。
def main():
    # 1.如果起点或者终点坐标值为1，代表没有路径
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return 0

    # 2.dp[i][j]代表从起点(0,0)到(i,j)总共有多少参观路径
    dp = [[0]*(n+1) for _ in range(m+1)]
    dp[1][1] = 1
    grid[0][0] = -1  # start
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0: 
                # left | up
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1]

    # print(dp)
    return dp[-1][-1]

print(main())

