"""
给你一个整数数组 nums 和两个整数：left 及 right 。找出 nums 中连续、非空且其中最大元素在范围 [left, right] 内的子数组，并返回满足条件的子数组的个数。

生成的测试用例保证结果符合 32-bit 整数范围。

 

示例 1：

输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]
示例 2：

输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7
 

提示：
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= left <= right <= 10^9
"""

# todo 方法2：不定长滑窗 + 前缀和思想
# 最大元素在区间[L..R] 里的连续子数组的个数，可以看成是一个「区间」的问题，处理区间的问题可以按照「前缀和」的思路。
# 把原问题转化成为「最大元素小于等于R 的连续子数组的个数」减去「最大元素小于等于L−1 的连续子数组的个数」。

class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        # 找最大元素在范围 [left, right] 内的子数组，返回满足条件的子数组的个数。
        
        def notGreater(k: int):
            # 返回nums连续子数组的最大值小于等于k的子数组个数
            ans = 0
            cur = 0  # 以当前字符结尾，子串中最大值不大于k的子数组个数
            for x in nums:
                if x <= k:
                    cur += 1 
                else:
                    cur = 0
                    
                ans += cur
            return ans

        #todo  betweenK 可以直接利用 atMostK，即 atMostK(k1) - atMostK(k2 - 1)，其中 k1 > k2。
        return notGreater(right) - notGreater(left-1)


# todo 方法1：三指针解法
class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        # 找最大元素在范围 [left, right] 内的子数组，返回满足条件的子数组的个数。
        ans = 0

        # todo [l..r]最大元素在left~right范围之内，且r端点元素一定在范围之内
        l = 0
        r = -1
        for i, x in enumerate(nums):
            if x > right:
                l = i+1
                continue

            if left <= x <= right:
                r = i

            # 更新ans
            if r >= l:
                ans += r-l+1

        return ans



