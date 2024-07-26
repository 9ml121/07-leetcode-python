"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/135232122?spm=1001.2014.3001.5502

题目描述
给定 M（0 < M ≤ 30）个字符（a-z），从中取出任意字符（每个字符只能用一次）拼接成长度为 N（0 < N ≤ 5）的字符串，

要求相同的字符不能相邻，计算出给定的字符列表能拼接出多少种满足条件的字符串，

输入非法或者无法拼接出满足条件的字符串则返回0。

输入描述
给定的字符列表和结果字符串长度，中间使用空格(" ")拼接

输出描述
满足条件的字符串个数

用例1
输入
abc 1
输出
3
说明
给定的字符为a,b,c，结果字符串长度为1，可以拼接成a,b,c，共3种

用例2
输入
dde 2
输出
2
说明
给定的字符为dde，结果字符串长度为2，可以拼接成de,ed，共2种
"""

'''
题目解析
根据用例2的说明来看，本题是要求解的是：不重复的指定长度的排列。且本题还增加了一个条件，即排列中相邻元素不能相同。
本题的基础是求解排列。关于排列的求解可以看下：
C-回溯算法/排列&组合&子集/46. 全排列.py

了解的排列的求解后，我们就可以进一步了解不重复的排列求解，具体可以看下：
C-回溯算法/排列&组合&子集/47. 全排列 II.py

而本题只需要在这两题的基础增加：排列中相邻元素不能相同即可。
'''

# 获取输入
s, k = input().split()
k = int(k)

# 回溯算法
s = sorted(s)
ans = 0


def dfs(path, used):
    global ans
    if len(path) == k:
        ans += 1
        return

    for i in range(len(s)):
        if used[i]:
            continue

        # 重复组合剪枝
        if i > 0 and s[i] == s[i-1] and not used[i-1]:
            continue

        # 相同的字符不能相邻
        if path and s[i] == path[-1]:
            continue

        used[i] = True
        path.append(s[i])
        dfs(path, used)
        path.pop()
        used[i] = False


def solution(s: str, k: int):
    # 输入合法性校验
    if not (0 < len(s) <= 30) or not (0 < k <= 5):
        return 0
    for c in s:
        if not ('a' <= c <= 'z'):
            return 0

    # 调用算法
    path = []
    used = [False] * len(s)
    dfs(path, used)

    return ans


print(solution(s, k))
