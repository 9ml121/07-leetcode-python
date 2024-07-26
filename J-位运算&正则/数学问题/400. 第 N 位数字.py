"""
给你一个整数 n ，请你在无限的整数序列 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...] 中找出并返回第 n 位上的数字。

 

示例 1：

输入：n = 3
输出：3
示例 2：

输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
 

提示：

1 <= n <= 2^31 - 1
"""

# todo 考察数学

"""
https://leetcode.cn/problems/nth-digit/solutions/2362054/400-di-n-wei-shu-zi-qing-xi-tu-jie-by-jy-sz5y

本文名词规定如下：
1.将 101112⋯ 中的每一位称为 数位 ，记为 n。
2.将 10,11,12,⋯ 称为 数字 ，记为 num 。
3.数字 10 是一个两位数，称此数字的 位数 为 2 ，记为 digit 。
4.每 digit 位数的起始数字（即：1,10,100,⋯），记为 start 。

数字范围    位数    数字数量    数位范围
1~9         1       9           9
10~99       2       90          180
100~999     3       900         2700
...
start~end   digit   9*start     9*start*digit

观察上表，可推出各 digit 下的数位数量 count 的计算公式：
count = 9 × start × digit

根据以上分析，可将求解分为三步：
1.确定 n 所在 数字 的 位数digit。
>>> digit, start, count = 1, 1, 9
>>> while n > count:
>>>     n -= count
>>>     start *= 10 # 1, 10, 100, ...
>>>     digit += 1  # 1,  2,  3, ...
>>>     count = 9 * start * digit # 9, 180, 2700, ...
# 循环执行 n 减去 一位数、两位数、... 的数位数量 count，直至 n≤count 时跳出。
# 由于 n 已经减去了一位数、两位数、...、(digit−1) 位数的 数位数量 count ，因而此时的 n 是从起始数字 start 开始计数的
# 结论：1.所求数位在某个 digit 位数中；2.所求数位为从数字 start 开始的第 n 个数位。

2.第二步：确定所求数位所在的数字num。
以digit=2, start=10为例：
            1 0 1 1 1 2 1 3 ...
n           1 2 3 4 5 6 7 8 ...
(n-1)//2    0 0 1 1 2 3 3 4 ...    

如上图所示，所求数位 在从数字 start 开始的第 [(n−1)//digit] 个 数字 中（ start 为第 0 个数字）。
结论： 所求数位在数字 num 中。
>>> num = start + (n - 1) // digit

3.第三步：确定所求数位在 num 的哪一数位
以digit=2, start=10为例：
            1 0 1 1 1 2 1 3 ...
n           1 2 3 4 5 6 7 8 ...
(n-1)%2     0 1 0 1 0 1 0 1 ...   

如上图所示，所求数位为数字 num 的第 (n−1)%digit 位（ 数字的首个数位为第 0 位）
结论： 所求数位是 res 。
>>> s = str(num) # 转化为 string
>>> res = int(s[(n - 1) % digit]) # 获得 num 的 第 (n - 1) % digit 个数位，并转化为 int
"""

# 写法1


class Solution:
    def findNthDigit(self, n: int) -> int:
        # 找到无限连续的整数列表，第n位上的数字

        # todo 1.确定 n 所在 数字 的 位数 ，记为 digit。
        digit = 1   # 几位数
        start = 1   # 该位数的开始数字
        count = 9   # d位数的数位数量

        while n > count:
            n -= count
            start *= 10  # 1, 10, 100, ..
            digit += 1   # 1,  2,  3, ...
            count = 9 * start * digit  # 9, 180, 2700, ...

        # 1.所求数位在某个 digit 位数中；2.所求数位为从数字 start 开始的第 n 个数位。

        # todo 2.确定 所求数位 所在的 数字 ，记为 num
        # 假设 start = 10，那么 n 是 10~99 中的某个两位数的哪一个？
        # 所求数位 在从数字 start 开始的第 [(n−1)//digit] 个 数字 中（start 为第 0 个数字）
        num = start + (n - 1) // digit
        
        # todo 3：确定所求数位在 num 的哪一数位
        # 假设num = 65, n是65中的拿个数字 ？
        # 怎么把 num 的第 idx 这一位数字抠出来呢？可以转化成字符串来算
        # 所求数位为数字 num 的第 (n−1)%digit 位（ 数字的首个数位为第 0 位）
        s = int(num)
        idx = (n - 1) % digit
        return int(s[idx])  

# 写法2
class Solution:
    def findNthDigit(self, n: int) -> int:
        # 找到无限连续的整数列表，第n位上的数字

        # 位数（一位数，两位数...）
        digit = 1
        # 1,10,100, 1000 这样的后缀
        base = 1

        while n > 9 * base * digit:
            n -= 9 * base * digit
            base *= 10
            digit += 1

        # 此时假设 base = 1000，那么说明 n 是 100~999 中的某个三位数的某一位
        # 哪个三位数呢？这样算：
        val = base + (n - 1) // digit
        # 是这个三位数的第几位呢？这样算：
        index = (n - 1) % digit

        # 怎么把 val 的第 index 这一位数字抠出来呢？可以转化成字符串来算：
        return int(str(val)[index])
