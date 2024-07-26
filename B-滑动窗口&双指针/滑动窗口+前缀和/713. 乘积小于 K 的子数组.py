"""
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
 

示例 1：

输入：nums = [10,5,2,6], k = 100
输出：8
解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
示例 2：

输入：nums = [1,2,3], k = 0
输出：0
 

提示: 

1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
"""

# todo 不定长滑窗 + 窗口计数问题

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        # 返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目
        ans = 0
        if k <= 1:
            return 0
        
        # todo [l..r]内元素乘积严格小于k, prod用来记录窗口内所有元素乘积
        # [l,r],[l+1,r]...[r,r] ==> 子数组以r结尾，窗口内符合条件的子数组个数为r-l+1
        l = 0
        prod = 1
        for r, x in enumerate(nums):
            # 入
            prod *= x
            
            # 出
            while prod >= k:
                prod //= nums[l]
                l += 1

            # 更新ans
            ans += r-l+1

        return ans
