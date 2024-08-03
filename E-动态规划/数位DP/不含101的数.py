"""
https://fcqian.blog.csdn.net/article/details/128065744

题目描述
小明在学习二进制时，发现了一类不含 101的数，也就是：

将数字用二进制表示，不能出现 101 。
现在给定一个整数区间 [l,r] ，请问这个区间包含了多少个不含 101 的数？

输入描述
输入的唯一一行包含两个正整数 l， r（ 1 ≤ l ≤ r ≤ 10^9）。

输出描述
输出的唯一一行包含一个整数，表示在 [l,r] 区间内一共有几个不含 101 的数。

用例
输入	1 10
输出	8
说明	区间 [1,10] 内， 5 的二进制表示为 101 ，10的二进制表示为 1010 ，因此区间 [ 1 , 10 ] 内有 10−2=8 个不含 101的数。

输入	10 20
输出	7
说明	区间 [10,20] 内，满足条件的数字有 [12,14,15,16,17,18,19] 因此答案为 7。
"""

'''
题目解析
本题如果用暴力法求解，很简单
但是本题的1 ≤ l ≤ r ≤ 10^9，也就是说区间范围最大是 1 ~ 10^9，那么上面O(n)时间复杂度的算法会超时。
因此，我们需要找到一个性能更优的算法。

本题需要使用数位DP算法，具体逻辑原理请看
    E-动态规划\数位DP\带3的数.py
    E-动态规划\数位DP\带49的数.py
'''


# 输入
from functools import cache
l, r = map(int, input().split())

# todo 数位dp
@cache
def dfs(s: str, i=0, pre0:int=None, prepre1:int=None, limit=True):
    # pre0:前一位是否为 0，前二位是否为 1
    if i == len(s):
        return 1

    res = 0
    up = int(s[i]) if limit else 1
    for d in range(up+1):
        # 含有 101， 跳过
        if d == 1 and pre0==0 and prepre1==1:
            continue
        
        res += dfs(s, i+1, d, pre0, limit and d == up)

    return res


# 输出：整数区间 [l,r] 包含了多少个二进制不含 101 的数
l = bin(l-1)[2:]
r = bin(r)[2:]
ans = dfs(r) - dfs(l)
print(ans)



