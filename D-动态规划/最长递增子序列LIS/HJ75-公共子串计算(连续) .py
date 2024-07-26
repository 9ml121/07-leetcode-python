"""
描述
给定两个只包含小写字母的字符串，计算两个字符串的最大公共子串的长度。

注：子串的定义指一个字符串删掉其部分前缀和后缀（也可以不删）后形成的字符串。
数据范围：字符串长度：1≤s≤150
进阶：时间复杂度：O(n^3) ，空间复杂度：O(n)
输入描述：
输入两个只包含小写字母的字符串

输出描述：
输出一个整数，代表最大公共子串的长度

示例1
输入：
asdfas
werasdfaswer

输出：
6
"""

# todo 注意此题跟 leetcode 1143. 最长公共子序列LCS 有区别
# 区别在于这里公共子串是连续的

"""
解法1：暴力枚举，列出所有的可能性
"""
# s1 = input()
# s2 = input()
# if len(s1) > len(s2):
#     s1, s2 = s2, s1  # 保证s1是长度较短的那个
#
# res = 0
# for i in range(len(s1)):
#     if s1[i] in s2:
#         for j in range(i, len(s1)):
#             if s1[i:j + 1] in s2 and j + 1 - i > res:
#                 res = j + 1 - i
# print(res)

"""
解法2：dp
"""


def getResult(s1: str, s2: str):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
    # dp[i][j]代表s1[i-1]结尾，s2[j-1]结尾出现的最长 连续 公共子串
    # base case:i=0或者j=0都代表没有匹配的上，值为0

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                # 动态转移函数：
                dp[i][j] = dp[i - 1][j - 1] + 1
            # 如果不想等，需要重新开始统计，也就是默认值0

    # print(dp)
    # 最后结果应该是dp里面的最大值
    return max(dp)
