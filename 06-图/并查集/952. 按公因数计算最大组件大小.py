"""
给定一个由不同正整数的组成的非空数组 nums ，考虑下面的图：

有 nums.length 个节点，按从 nums[0] 到 nums[nums.length - 1] 标记；
只有当 nums[i] 和 nums[j] 共用一个大于 1 的公因数时，nums[i] 和 nums[j]之间才有一条边。
返回 图中最大连通组件的大小 。


示例 1：
    4--6--15--35
输入：nums = [4,6,15,35]
输出：4

示例 2：
    20--50  9--63
输入：nums = [20,50,9,63]
输出：2

示例 3：
输入：nums = [2,3,6,7,4,12,21,39]
输出：8


提示：
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^5
nums 中所有值都 不同
"""

from typing import List


# 枚举点 + 求公约数: 肯定会超时
# 类似leetcode 1627. 带阈值的图连通性
# 枚举质因数 + 并查集运用题
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # 统计一个正整数的质因数（素因子）
        def getPrimeFactors(num):
            factors = set()
            i = 2
            while i * i <= num:  # num = 18
                if num % i == 0:
                    factors.add(i)
                    num //= i
                else:
                    i += 1
            if num > 1:
                factors.add(num)
            return factors

        # 维护连通块数量可以使用「并查集」来做
        n = len(nums)
        parent = list(range(n))  # parent[i]代表 nums数组下标为 i 与下标为 parent[i]的 数值有 直接 或者 间接 公因数
        sizes = [1] * n  # size[i]代表 与 nums数组下标为i 的数值有直接或者间接公因数的个数

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                sizes[root_y] += sizes[root_x]

        # 维护映射关系可以使用「哈希表」来做。
        valToIdx = {}
        for i, num in enumerate(nums):
            factors = getPrimeFactors(num)  # 对nums[i] 进行质因数分解
            for factor in factors:
                if factor not in valToIdx:
                    valToIdx[factor] = i
                else:
                    union(i, valToIdx[factor])

        # print(parent)
        # print(sizes)
        return max(sizes)


if __name__ == '__main__':
    # nums = [4, 6, 15, 35]  # 4
    # nums = [2, 3, 6, 7, 4, 12, 21, 39]  # 8
    nums = [83, 99, 39, 11, 19, 30, 31]  # 4
    print(Solution().largestComponentSize(nums))
