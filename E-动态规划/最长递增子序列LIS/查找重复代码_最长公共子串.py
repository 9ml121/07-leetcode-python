"""
题目解析和算法源码
华为OD机试 - 查找重复代码（Java & JS & Python）_伏城之外的博客-CSDN博客

题目描述
小明负责维护项目下的代码，需要查找出重复代码，用以支撑后续的代码优化，请你帮助小明找出重复的代码。

重复代码查找方法：以字符串形式给定两行代码（字符串长度 1 < length <= 100，由英文字母、数字和空格组成），找出两行代码中的最长公共子串。

注：如果不存在公共子串，返回空字符串

输入描述
输入的参数text1, text2分别表示两行代码

输出描述
输出任一最长公共子串

用例1
输入
hello123world
hello123abc4
输出
hello123

用例2
输入
private_void_method
public_void_method
输出
_void_method

用例3
输入
hiworld
hiweb
输出
hiw
"""

# todo 注意此题和 E-动态规划\最长递增子序列LIS\HJ75-公共子串计算(连续) .py 区别
# 输入
text1 = input()
text2 = input()

# 输出：最长公共子串
n1 = len(text1)
n2 = len(text2)
# dp[i][j] 表示的是，str1的0~i范围  和  str2的0~j范围   的公共子串的长度
dp = [[0] * (n2+1) for _ in range(n1+1)]

max_len = 0  # 最长公共子串长度
end = 0      # 最长公共子串在text1中的结尾下标
for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        if text1[i-1] == text2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            
            if dp[i][j] > max_len:
                max_len = max(max_len, dp[i][j])
                end = i
        else:
            dp[i][j] = 0

# print(dp)
ans = text1[end - max_len: end]
print(ans)
