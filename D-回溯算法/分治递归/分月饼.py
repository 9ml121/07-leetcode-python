"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134629018?spm=1001.2014.3001.5502

题目描述
中秋节，公司分月饼，m 个员工，买了 n 个月饼，m ≤ n，每个员工至少分 1 个月饼，但可以分多个，

单人分到最多月饼的个数是 Max1 ，单人分到第二多月饼个数是 Max2 ，Max1 - Max2 ≤ 3 ，
单人分到第 n - 1 多月饼个数是 Max(n-1)，单人分到第n多月饼个数是 Max(n) ，Max(n-1) – Max(n) ≤ 3,
问有多少种分月饼的方法？

输入描述
每一行输入m n，表示m个员工，n个月饼，m ≤ n

输出描述
输出有多少种月饼分法

用例1
输入
2 4
输出
2
说明
分法有2种:

4 = 1 + 3
4 = 2 + 2
注意：1+3和3+1算一种分法

用例2
输入
3 5
输出
2
说明
5 = 1 + 1 + 3

5 = 1 + 2 + 2

用例3
输入
3 12
输出
6
说明
满足要求的有6种分法：

12 = 1 + 1 + 10（Max1 = 10, Max2 = 1，不满足Max1 - Max2 ≤ 3要求）
12 = 1 + 2 + 9（Max1 = 9, Max2 = 2，不满足Max1 - Max2 ≤ 3要求）
12 = 1 + 3 + 8（Max1 = 8, Max2 = 3，不满足Max1 - Max2 ≤ 3要求）
12 = 1 + 4 + 7（Max1 = 7, Max2 = 4，Max3 = 1，满足要求）
12 = 1 + 5 + 6（Max1 = 6, Max2 = 5，Max3 = 1，不满足要求）
12 = 2 + 2 + 8（Max1 = 8, Max2 = 2，不满足要求）
12 = 2 + 3 + 7（Max1 = 7, Max2 = 3，不满足要求）
12 = 2 + 4 + 6（Max1 = 6, Max2 = 4，Max3 = 2，满足要求）
12 = 2 + 5 + 5（Max1 = 5, Max2 = 2，满足要求）
12 = 3 + 3 + 6（Max1 = 6, Max2 = 3，满足要求）
12 = 3 + 4 + 5（Max1 = 5, Max2 = 4，Max3 = 3，满足要求）
12 = 4 + 4 + 4（Max1 = 4，满足要求）

"""

from functools import cache
# 获取输入

man_sz, cake_sz = map(int, input().split())

"""
3 5

1 1 3
1 2 2
1 3 1 => False

2 2 1 =>False
3 3   =>False
"""

# 分治算法
@cache
def dfs(level, lo, hi, remain):
    """
    level:分到第几个人  
    lo:可以分的最小月饼数
    hi:可以分的最大月饼数
    remain:剩余的月饼数
    """
    #  分到最后一个员工时，我们应该将剩余月饼都给他
    if level == man_sz - 1:
        if remain - lo <= 3:
            return 1
        return 0

    ans = 0
    for i in range(lo,  hi + 1):
        remain -= i
        ans += dfs(level+1, i, min(i+3, remain//(man_sz - level - 1)), remain)
        remain += i
    return ans


def solution():
    if man_sz == 1:
        return 1

    # 第一个人可以分的最小月饼数是1， 最大数是cake_sz // man_sz
    lo = 1
    hi = cake_sz//man_sz
    return dfs(0, lo, hi, cake_sz)

# print(solution())


# 参考写法2:
# 找到符合条件的所有分法
def dfs(path, level, lo, hi, remain, ans):
    """
    @path:局部变量，每个人已分到的月饼数列表
    @level:已经分了几个人，实际上就是len(path)
    @lo:当前能分的最少月饼数
    @hi:当前能分的最大月饼数
    @remain:还剩余的月饼数
    @ans:全局变量，所有符合条件分法的列表组合
    """
    # 递归结束条件为：已经分完倒数第二个人
    if level == man_sz - 1:
        if remain - lo <= 3:
            # 如果符合分配分案，就把方案path添加到最终结果列表ans
            # path.append(remain)
            ans.append(path[:] + [remain])  # 注意path是可变列表，不能直接添加
        return

    for i in range(lo, hi+1):
        remain -= i
        path.append(i)
        level += 1
        dfs(path, level, i, min(i+3, remain//(man_sz-level)), ans)
        path.pop()
        remain += i
        level -= 1


def solution():
    if man_sz == 1:
        return [cake_sz]

    lo = 1
    hi = cake_sz//man_sz
    ans = []
    dfs([], 0, lo, hi, ans)
    return ans


print(solution())

"""
3 12

[[1, 4, 7], 
[2, 4, 6], 
[2, 5, 5], 
[3, 3, 6], 
[3, 4, 5], 
[4, 4, 4]]
"""
