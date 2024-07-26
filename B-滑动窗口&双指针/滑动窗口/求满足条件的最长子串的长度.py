"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127341878

OJ用例
https://hydro.ac/d/HWOD2023/p/OD153/solution

题目描述
给定一个字符串，只包含字母和数字，按要求找出字符串中的最长（连续）子串的长度，字符串本身是其最长的子串，子串要求：

1、 只包含1个字母(a~z, A~Z)，其余必须是数字；

2、 字母可以在子串中的任意位置；

如果找不到满足要求的子串，如全是字母或全是数字，则返回-1。

输入描述
字符串(只包含字母和数字)

输出描述
子串的长度

用例1
输入
abC124ACb
输出
4
说明
满足条件的最长子串是C124或者124A，长度都是4

用例2
输入
a5
输出
2
说明
字符串自身就是满足条件的子串，长度为2

用例3
输入
aBB9
输出
2
说明
满足条件的子串为B9，长度为2

用例4
输入
abcdef
输出
-1
说明
没有满足要求的子串，返回-1
"""

# 写法1
s = input()
# s = 'abC124ACb'

n = len(s)
r = 0
ans = -1
while r < n:
    if s[r].isalpha():
        l = r
        # 123A
        while l - 1 >= 0 and s[l-1].isdigit():
            l -= 1
        # C123
        while r + 1 < n and s[r+1].isdigit():
            r += 1

        if r > l:
            ans = max(ans, r - l + 1)

    r += 1
print(ans)


# 写法2
# 输入获取
s = input()


# 算法入口
def getResult():
    maxLen = -1

    l = 0
    r = 0
    letterIdx = []
    hasLetter = False

    while r < len(s):
        # s = 'abC124ACb'
        if s[r].isalpha():
            hasLetter = True
            letterIdx.append(r)

            if len(letterIdx) > 1:
                l = letterIdx.pop(0) + 1

            if r == l:
                r += 1
                continue

        maxLen = max(maxLen, r - l + 1)
        r += 1

    if not hasLetter:
        return -1
    return maxLen


# 算法调用
print(getResult())
