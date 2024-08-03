"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/128816967

题目描述
有N条线段，长度分别为a[1]-a[n]。

现要求你计算这N条线段最多可以组合成几个直角三角形。

每条线段只能使用一次，每个三角形包含三条线段。

输入描述
第一行输入一个正整数T（1<＝T<＝100），表示有T组测试数据.

对于每组测试数据，接下来有T行，

每行第一个正整数N，表示线段个数（3<＝N<＝20），接着是N个正整数，表示每条线段长度，（0<a[i]<100）。

输出描述
对于每组测试数据输出一行，每行包括一个整数，表示最多能组合的直角三角形个数

用例1
输入
1
7 3 4 5 6 5 12 13
输出
2
说明
可以组成2个直角三角形（3，4，5）、（5，12，13）

"""

# todo 本题并不是简单的全组合求解，考察排列组合 + 回溯 + 去重

# 输入
# t组测试数据
# t = int(input())
# 每行第一个正整数N，表示线段个数（3<＝N<＝20），接着是N个正整数，表示每条线段长度，（0<a[i]<100）。
# cases = [list(map(int, input().split()))[1:] for _ in range(t)]
# print(cases)

# 测试数据
cases = [[3, 3, 4, 5, 12, 13, 84,85]]


# 输出：每组测试数据输出一行，表示最多能组合的直角三角形个数
def dfs(case, n, idx, used, cnt):
    ans = cnt

    for i in range(idx, n):
        if used[i]:
            continue
        for j in range(i+1, n):
            if used[j]:
                continue
            for k in range(j+1, n):
                if used[k]:
                    continue

                a = case[i]
                b = case[j]
                c = case[k]
                if a**2 + b**2 == c**2:
                    used[i] = True
                    used[j] = True
                    used[k] = True
                    # todo 注意这里更新结果，是取每次递归树中能组成的最多组合
                    res = dfs(case, n, idx+1, used, cnt+1)
                    ans = max(ans, res)

                    used[i] = False
                    used[j] = False
                    used[k] = False
    return ans


for case in cases:
    case.sort()
    n = len(case)
    ans = dfs(case, n, 0, [False]*n, 0)
    print(ans)

