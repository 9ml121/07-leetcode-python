"""
给你一个正整数数组 nums ，对 nums 所有元素求积之后，找出并返回乘积中 不同质因数 的数目。

注意：
质数 是指大于 1 且仅能被 1 及自身整除的数字。
如果 val2 / val1 是一个整数，则整数 val1 是另一个整数 val2 的一个因数。


示例 1：
输入：nums = [2,4,3,7,10,6]
输出：4
解释：
nums 中所有元素的乘积是：2 * 4 * 3 * 7 * 10 * 6 = 10080 = 25 * 32 * 5 * 7 。
共有 4 个不同的质因数，所以返回 4 。

示例 2：
输入：nums = [2,4,8,16]
输出：1
解释：
nums 中所有元素的乘积是：2 * 4 * 8 * 16 = 1024 = 210 。
共有 1 个不同的质因数，所以返回 1 。


提示：
1 <= nums.length <= 104
2 <= nums[i] <= 1000
"""
from typing import List


# 方法 1：分解质因数
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        # 统计一个正整数的质因数（素因子）
        def getPrimeFactors(n: int):
            factors = set()
            i = 2
            while i * i <= n:  # n=10
                if n % i == 0:
                    factors.add(i)
                    n //= i
                else:
                    i += 1

            if n > 1:
                factors.add(n)

            return factors

        # 多个集合取并集
        union_set = set()
        for num in nums:
            factors = getPrimeFactors(num)  # 分解质因数
            union_set = union_set.union(factors)

        return len(union_set)
