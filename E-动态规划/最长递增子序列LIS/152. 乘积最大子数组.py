"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

子数组 是数组的连续子序列。



示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。


提示:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数
"""
from typing import List

"""
解题思路
标签：动态规划
1.遍历数组时计算当前最大值，不断更新
2.令imax为当前最大值，则当前最大值为 imax = max(imax * nums[i], nums[i])
3.由于存在负数，那么会导致最大的变最小的，最小的变最大的。因此还需要维护当前最小值imin，imin = min(imin * nums[i], nums[i])
4.当负数出现时则imax与imin进行交换再进行下一步计算

时间复杂度：O(n)
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = min_product = 1
        max_product_global = -float('inf')

        for num in nums:
            if num < 0:
                max_product, min_product = min_product, max_product
            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)
            # print(f'{num} -> {max_product} / {min_product}')

            max_product_global = max(max_product_global, max_product)
        return max_product_global


if __name__ == '__main__':
    nums = [2, 3, -2, 4, -2]
    print(Solution().maxProduct(nums))
