"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127418073

OJ用例
题解 - 求字符串中所有整数的最小和 - Hydro

题目描述
输入字符串s，输出s中包含所有整数的最小和。

说明：

字符串s，只包含 a-z A-Z ±

合法的整数包括

1）正整数：一个或者多个0-9组成，如 0 2 3 002 102

2）负整数：负号 – 开头，数字部分由一个或者多个0-9组成，如 -0 -012 -23 -00023

输入描述
包含数字的字符串

输出描述
所有整数的最小和

用例1
输入
bb1234aa
输出
10
用例2
输入
bb12-34aa
输出
-31
说明
1+2+（-34） = -31
"""
# s = 'bb1234aa'
# s = 'bb12-34aa'


s = input()
ans = 0

n = len(s)
i, j = 0, 0
while j < len(s):
    if s[j].isalpha():
        j += 1
    elif s[j] == '-':
        # 负整数按照最大位数计算
        j += 1
        i = j
        while j < len(s) and s[j].isdigit():
            j += 1
        if j > i:
            neg = int(s[i:j])
            ans -= neg
    else:
        # 正整数按照最小位数计算
        if s[j] == '+':
            j += 1
        while j < len(s) and s[j].isdigit():
            pos = int(s[j])
            ans += pos
            j += 1

print(ans)

""" 
bb12-a-34aa
bb1+2+a+-34aa
"""
