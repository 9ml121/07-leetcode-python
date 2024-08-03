"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127711587

题目描述
有一个考古学家发现一个石碑，但是很可惜，发现时其已经断成多段，原地发现n个断口整齐的石碑碎片。为了破解石碑内容，考古学家希望有程序能帮忙计算复原后的石碑文字组合数，你能帮忙吗？

输入描述
第一行输入n，n表示石碑碎片的个数。

第二行依次输入石碑碎片上的文字内容s，共有n组。

输出描述
输出石碑文字的组合（按照升序排列），行末无多余空格。

备注
如果存在石碑碎片内容完全相同，则由于碎片间的顺序变换不影响复原后的碑文内容，即相同碎片间的位置变换不影响组合。

用例1
输入
3
a b c
输出
abc
acb
bac
bca
cab
cba
说明
当石碑碎片上的内容为“a”，“b”，“c”时，则组合有“abc”，“acb”，“bac”，“bca”，“cab”，“cba”

用例2
输入
3
a b a
输出
aab
aba
baa
说明
当石碑碎片上的内容为“a”，“b”，“a”时，则可能的组合有“aab”，“aba”，“baa”

用例3
输入
3
a b ab
输出
aabb
abab
abba
baab
baba
说明
当石碑碎片上的内容为“a”，“b”，“ab”时，则可能的组合有“aabb”，“abab”，“abba”，“baab”，“baba”


"""


# 获取输入
n = int(input())
stones = input().split()

# 有重复元素的全排列
stones.sort()
ans = set()


def dfs(path, vis):
    global ans
    if len(path) == n:
        ans.add(''.join(path))
        return

    for i in range(n):
        if vis[i]:
            continue

        if i > 0 and stones[i] == stones[i-1] and not vis[i-1]:
            continue

        path.append(stones[i])
        vis[i] = True
        dfs(path, vis)
        vis[i] = False
        path.pop()


path = []
vis = [False] * n
dfs(path, vis)
ans = sorted(ans)
for c in ans:
    print(c)
