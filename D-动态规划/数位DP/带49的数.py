"""
题目来源
https://blog.csdn.net/qfc_128220/article/details/128139171?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22128139171%22%2C%22source%22%3A%22qfc_128220%22%7D

题目描述
求区间 [1,n] 范围内包含多少带 49 的数。

一个数是带 49 的数，当且仅当它的十进制表示中存在连续的两位，其中较高位为 4，较低位为 9。
比如：49, 149, 1234987 都是带 49 的数；
而 4, 12345, 94, 999444 都不是。

输入描述
输入一个整数 n (1 ≤ n < 2^63)。

输出描述
输出一个整数，表示区间 [1, n] 范围内存在多少带 49 的数。

用例
输入	500
输出	15
说明	无

"""

# 输入
from functools import cache
s = input()


# 输出：求区间 [1,n] 范围内包含多少带 49 的数
# todo 数位dp:统计不含49的数更优雅写法
@cache
def dfs(s:str, i=0, pre4=False, limit=True):
    # 找到1个不含49的数
    if i == len(s):
        return 1

    res = 0
    up = int(s[i]) if limit else 9
    for d in range(up+1):
        # 跳过含有49的数字
        if d == 9 and pre4:
            continue

        res += dfs(s, i+1, d == 4, limit and d == up)

    return res

# 算法调用: 总数 - 不含49数的个数 = 含49数的个数
print(int(s) + 1 - dfs(s))


