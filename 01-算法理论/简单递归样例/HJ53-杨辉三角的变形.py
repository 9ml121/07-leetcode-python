"""
以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数、左上角数和右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。

求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。
例如输入3,则输出2，输入4则输出3，输入2则输出-1。

数据范围： 1≤n≤10^9

输入描述：
输入一个int整数

输出描述：
输出返回的int值

示例1
输入：
4

输出：
3
"""


# 解法1:递归，会内存超限
def method1():
    def fun(n):
        pre = [1] * n
        dp = [1] * n
        if n == 1:
            dp = [1]
            # [1]

        elif n == 2:
            pre = [1] * n
            dp = pre + pre[0: n - 1][::-1]
            # [1,1,1]

        if n >= 3:
            pre[0] = 1
            pre[1] = n - 1
            # 递归逻辑
            dp = fun(n - 1)
            for i in range(2, n):
                pre[i] = dp[i - 2] + dp[i - 1] + dp[i]
            dp = pre + pre[0: n - 1][::-1]

            # [1, 2, 3, 2, 1]
            # [1, 3, 6, 7, 6, 3, 1]
            # [1, 4, 10, 16, 19, 16, 10, 4, 1]
        return dp


    n = int(input())
    dp = fun(n)
    res = -1
    for elem in dp:
        index = dp.index(elem)
        if elem % 2 == 0:
            res = index + 1
            break

    print(res)

"""
解法2：动态规划(推荐)
"""
n = int(input())
# [1]
# [1,1,1]
# [1,2,3,2,1]
# [1,3,6,7,6,3,1]

dp = [[0] * (i + 1) for i in range(n)]
dp[0] = [1]
if n >= 2:
    dp[1] = [1, 1]
if n >= 3:
    for i in range(2, n):  # n = 3, i = 2
        for j in range(i + 1):  # 2:[0,1,2]
            if j == 0:
                dp[i][0] = 0 + 0 + dp[i - 1][j]
            elif j == 1:
                dp[i][1] = 0 + dp[i - 1][j - 1] + dp[i - 1][j]
            elif 2 <= j <= i-1:
                dp[i][j] = dp[i - 1][j - 2] + dp[i - 1][j-1] + dp[i - 1][j]
            elif j >= i:
                dp[i][j] = dp[i - 1][j - 2] + dp[i - 1][j - 1] + dp[i - 1][j-2]
        # dp[i] = dp[i][0:j + 1] + dp[i][0:j][::-1]
# print(dp)
lst = dp[n - 1]
res = -1
for elem in lst:
    index = lst.index(elem)
    if elem % 2 == 0:
        res = index + 1
        break
print(res)
