"""
给定一个正整数 n ，请你统计在 [0, n] 范围的非负整数中，有多少个整数的二进制表示中不存在 连续的 1 。

示例 1:
输入: n = 5
输出: 5
解释: 
下面列出范围在 [0, 5] 的非负整数与其对应的二进制表示：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数 3 违反规则（有两个连续的 1 ），其他 5 个满足规则。

示例 2:
输入: n = 1
输出: 2

示例 3:
输入: n = 2
输出: 3
 

提示:
1 <= n <= 10^9
"""

from functools import cache

# todo 数位 DP
# 标准数位DP写法
class Solution:
    def findIntegers(self, n: int) -> int:
        # 返回[0..n]范围的整数的二进制表示中不存在连续的1的个数
        # 1.将n转换为二进制字符s
        s = bin(n)[2:]

        @cache
        def dfs(i=0, pre1=False, is_limit=True) -> int:
            '''
            @i: 二进制字符s的数位索引，初始值为0
            @pre1: 当前位置的前一位是否为1
            @is_limit: 当前位置是否为限制位，如果是限制位，当前位置上限只能取0~s[i], 否则可以取0-1
            return: 不存在连续1的个数
            '''
            if i == len(s):
                return 1

            up = int(s[i]) if is_limit else 1
            res = 0
            for d in range(up+1):
                # 有连续1，跳过
                if d == 1 and pre1:
                    continue 
                
                res += dfs(i+1, d==1, is_limit and d == up)

            return res

        return dfs()


# 写法 2
class Solution:
    def findIntegers(self, n: int) -> int:
        s = bin(n)[2:]

        @cache
        def f(i: int=0, pre1: bool=False, is_limit: bool=True) -> int:
            if i == len(s):
                return 1
            up = int(s[i]) if is_limit else 1
            res = f(i + 1, False, is_limit and up == 0)  # 填 0
            if not pre1 and up == 1:  # 可以填 1
                res += f(i + 1, True, is_limit)  # 填 1
            return res
        
        return f()
