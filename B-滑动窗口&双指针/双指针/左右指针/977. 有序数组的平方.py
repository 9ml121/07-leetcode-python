"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

 

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]

示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
 

进阶：

请你设计时间复杂度为 O(n) 的算法解决本问题
"""
# todo 简单的左右双指针应用
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # nums升序，返回nums每个数字平方组成的新的升序数组，要求一次遍历
        # todo nums平方之后的最大值只有可能在最左端或者最右端
        n = len(nums)
        ans = [0] * n

        # l,r指向nums左右两端，比较平方之后的较大值，哪边大就移动哪边指针向内靠拢
        l = 0
        r = n-1
        # i指向ans最右端，依次填充比较得到的最大值
        i = n-1

        while l <= r:
            ls, rs = nums[l]**2, nums[r]**2
            if ls < rs:
                ans[i] = rs
                r -= 1
            else:
                ans[i] = ls
                l += 1

            i -= 1

        return ans
