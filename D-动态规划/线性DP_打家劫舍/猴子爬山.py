"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127418090

题目描述
一天一只顽猴想去从山脚爬到山顶，途中经过一个有个N个台阶的阶梯，但是这猴子有一个习惯：

每一次只能跳1步或跳3步，试问猴子通过这个阶梯有多少种不同的跳跃方式？

输入描述
输入只有一个整数N（0<N<=50）此阶梯有多少个台阶。

输出描述
输出有多少种跳跃方式（解决方案数）。

用例1
输入
50
输出
122106097
用例2
输入
3
输出
2
"""



# 输入
from functools import cache


n = int(input())

# 输出：有多少种跳跃方式

# 方法1：动态规划
def main1():
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i < 3:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + dp[i-3]
            
    # print(dp)
    print(dp[-1])


# 方法2：递归
@cache
def dfs(i=0):
    if i == n:
        return 1
    if i > n:
        return 0

    return dfs(i+1) + dfs(i+3)


ans = dfs()
print(ans)
