"""
给你两个正整数 left 和 right ，请你找到两个整数 num1 和 num2 ，它们满足：

left <= nums1 < nums2 <= right  。
nums1 和 nums2 都是 质数 。
nums2 - nums1 是满足上述条件的质数对中的 最小值 。
请你返回正整数数组 ans = [nums1, nums2] 。如果有多个整数对满足上述条件，请你返回 nums1 最小的质数对。如果不存在符合题意的质数对，请你返回 [-1, -1] 。

如果一个整数大于 1 ，且只能被 1 和它自己整除，那么它是一个质数。



示例 1：

输入：left = 10, right = 19
输出：[11,13]
解释：10 到 19 之间的质数为 11 ，13 ，17 和 19 。
质数对的最小差值是 2 ，[11,13] 和 [17,19] 都可以得到最小差值。
由于 11 比 17 小，我们返回第一个质数对。
示例 2：

输入：left = 4, right = 6
输出：[-1,-1]
解释：给定范围内只有一个质数，所以题目条件无法被满足。


提示：
1 <= left <= right <= 10^6
"""
import bisect
from typing import List


# 方法 1： 艾式筛
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [1] * (right + 1)
        primes = []
        minDiff = float('inf')
        res = [-1, -1]
        for i in range(2, right + 1):
            if is_prime[i]:
                if i >= left:
                    primes.append(i)
                if len(primes) >= 2 and primes[-1] - primes[-2] < minDiff:
                    minDiff = primes[-1] - primes[-2]
                    res = [primes[-2], primes[-1]]

                for j in range(i * i, right + 1, i):
                    is_prime[j] = 0

        # print(primes)
        return res


# 方法 2：线性筛
class Solution2:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [1] * (right + 1)
        primes = []

        for i in range(2, right + 1):
            if is_prime[i]:
                primes.append(i)

            for p in primes:
                if p * i > right:
                    break
                is_prime[p * i] = 0
                if i % p == 0:
                    break
        p, q = -1, -1
        MX = float('inf')
        primes.extend((MX, MX))  # 保证下面下标不会越界
        i = bisect.bisect_left(primes, left)  # primes[0..i) < left
        while primes[i + 1] <= right:
            if p < 0 or primes[i + 1] - primes[i] < q - p:
                p, q = primes[i], primes[i + 1]
            i += 1
        return [p, q]
