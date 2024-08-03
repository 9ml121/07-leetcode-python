"""
给你一个整数 k 和一个整数 x 。整数 num 的价值是它的二进制表示中在 x，2x，3x 等位置处 
设置位
 的数目（从最低有效位开始）。下面的表格包含了如何计算价值的例子。

x	num	Binary Representation	Price
1	13	000001101	3
2	13	000001101	1
2	233	011101001	3
3	13	000001101	1
3	362	101101010	2
 

num 的 累加价值 是从 1 到 num 的数字的 总 价值。如果 num 的累加价值小于或等于 k 则被认为是 廉价 的。

请你返回 最大 的廉价数字。

 

示例 1：

输入：k = 9, x = 1
输出：6
解释：由下表所示，6 是最大的廉价数字。
x	num	Binary Representation	Price	Accumulated Price
1	1	001	1	1
1	2	010	1	2
1	3	011	2	4
1	4	100	1	5
1	5	101	2	7
1	6	110	2	9
1	7	111	3	12
示例 2：

输入：k = 7, x = 2
输出：9
解释：由下表所示，9 是最大的廉价数字。
x	num	Binary Representation	Price	Accumulated Price
2	1	0001	0	0
2	2	0010	1	1
2	3	0011	1	2
2	4	0100	0	2
2	5	0101	0	2
2	6	0110	1	3
2	7	0111	1	4
2	8	1000	1	5
2	9	1001	1	6
2	10	1010	2	8
 

提示：

1 <= k <= 10^15
1 <= x <= 8
"""


from bisect import bisect_left
from functools import cache

# 方法一：二分答案 + 数位 DP
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        

        # 数位搜索num的累加价值
        def count(num: int) -> int:
            @cache
            def dfs(i: int, is_limit: bool = True, cnt1: int = 0) -> int:
                if i == 0:
                    return cnt1

                up = num >> (i-1) & 1 if is_limit else 1
                res = 0
                for d in range(up+1):
                    res += dfs(i-1, is_limit and d == up,
                               cnt1 + (d == 1 and i % x == 0))

                return res

            return dfs(num.bit_length())

        # num最大值和最小值
        lo = 1      # count(lo) <= k
        # 最差情况下，每 2^x个数才有一个有价值的数，那 2^x × (k+1) 个数的价值和肯定超过 k 了
        hi = (k+1) << x  # count(hi) > k
        while lo + 1 < hi:
            mid = (lo+hi) >> 1
            if count(mid) <= k:
                lo = mid
            else:
                hi = mid

        return lo


# 方法二：二分答案+数学公式（最优解）
class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count(num: int) -> int:
            res = 0
            shift = x - 1
            n = num >> shift
            while n:
                # 第一部分
                res += (n // 2) << shift
                # 第二部分
                if n % 2:
                    mask = (1 << shift) - 1
                    res += (num & mask) + 1
                shift += x
                n >>= x
            return res

        return bisect_left(range((k + 1) << x), k + 1, key=count) - 1
