·····"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134863965

题目描述
给定一个正整数 n，如果能够分解为 m（m > 1）个连续正整数之和，请输出所有分解中，m最小的分解。

如果给定整数无法分解为连续正整数，则输出字符串"N"。

输入描述
输入数据为一整数，范围为 (1, 2^30]

输出描述
比如输入为：

21

输出：

21=10+11

用例1
输入
21
输出
21=10+11
说明
21可以分解的连续正整数组合的形式有多种：

21=1+2+3+4+5+6

21=6+7+8

21=10+11

其中 21=10+11，是最短的分解序列。
"""

# todo 注意：下面方法是用到数学方法，也可以用滑动窗口(性能要差一点)
# 滑动窗口解法参见：A-滑动窗口&双指针/滑动窗口/用连续自然数之和来表达整数.py


# 获取输入
import math


n = int(input())  # n > 1


def main(n):
    # 1.如果n为奇数，一定可以分解为2个连续正整数
    if n % 2 == 1:
        a = n//2
        b = n//2 + 1
        return f'{n}={a}+{b}'

    # 2.如果n为偶数，只有(奇数 * 偶数)才能有解  100=25*4=5*20
    # a.一种分解方式：分解n的最大奇因数max_odd, 连续总个数为偶数even * 2(奇数可以由 2 个连续的数组成)
    max_odd = get_max_odd(n)
    if max_odd == 1:
        # 说明n只能分解为：偶数*偶数， 比如2, 4，8，16，这样的数字无解
        return 'N'

    # b.另外一种分解方式：找max_odd的最小奇因数min_odd(从 3 开始)，连续总个数就位 min_odd(偶数是中间数)
    sz1, left1 = check_max_odd(n, max_odd)
    sz2, left2 = check_min_odd(n, max_odd)
    sz, left = None, None
    if sz1 and sz2:
        if sz1 <= sz2:
            sz = sz1
            left = left1
        else:
            sz = sz2
            left = left2
    elif sz1:
        sz = sz1
        left = left1
    elif sz2:
        sz = sz2
        left = left2
    else:
        return 'N'

    ans = []
    for i in range(sz):
        ans.append(left + i)
    return f"{n}={'+'.join(map(str, ans))}"


def get_max_odd(n: int):
    # 分解 n的最大奇因数
    while n % 2 == 0:
        n //= 2
    return n


def check_max_odd(n: int, max_odd: int):
    even = n // max_odd
    # print(f'check_max_odd: {n}={max_odd}*{even}')
    sz = even * 2
    left = max_odd//2 - even + 1
    if left >= 1:
        return sz, left

    return None, None


def check_min_odd(n: int, max_odd: int):  # 100=25*4=5*20
    min_odd = max_odd
    for x in range(3, int(math.sqrt(max_odd))+1, 2):
        if max_odd % x == 0:
            min_odd = x
            break
    # 如果 max_odd不能分解为更小的奇数，那么连续数长度为 max_odd, 中间数为 even
    even = n // min_odd
    # print(f'{n}={min_odd}*{even}')
    sz = min_odd
    left = even - min_odd//2
    if left >= 1:
        return sz, left
    else:
        return None, None


print(main(n))
"""
100=18+19+20+21+22
100 = 5 * 20
100 = 4 * 25
100=10+11+12+13+14+15+16+17

Wrong Answer 0读取到 2012=249+250+251...，应为 2012=248+249+250...。
"""
