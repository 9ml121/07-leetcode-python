"""
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 最短 子数组，并输出它的长度。

 

示例 1：

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：

输入：nums = [1,2,3,4]
输出：0
示例 3：

输入：nums = [1]
输出：0
 

提示：

1 <= nums.length <= 104
-105 <= nums[i] <= 105
 

进阶：你可以设计一个时间复杂度为 O(n) 的解决方案吗？
"""


from typing import List

# 方法1：排序(最好理解), 时间复杂度为排序的消耗 O(Nlog(N))
class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 找nums左右边界，边界内的元素要小于左边最大值，大于右边最小值
        n = len(nums)

        # 1.如果原数组本来就有序，直接返回0
        def isSorted() -> bool:
            for i in range(1, n):
                if nums[i - 1] > nums[i]:
                    return False
            return True

        if isSorted():
            return 0

        # 2.将数组排序得到一个有序数组，然后跟原数组比对，分别找到左端点l和右端点r刚好破换数组有序性
        numsSorted = sorted(nums)
        left = 0
        while nums[left] == numsSorted[left]:
            left += 1

        right = n - 1
        while nums[right] == numsSorted[right]:
            right -= 1

        # 3.无序部分长度就是r-l+1
        return right - left + 1


# todo 方法2：一次遍历(最优解)，需要画图分析，逻辑分析有点困难（单调栈的思想）
"""
假设把这个数组分成三段，
左段和右段是标准的升序数组，
中段数组虽是无序的，但满足最小值大于左段的最大值，最大值小于右段的最小值。
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # 找nums左右边界，边界内的元素要小于左边最大值，大于右边最小值
        n = len(nums)
        
        # todo 循环不变量：nums[l..r]内的所有元素要大于左边left最大值l_max, 并且小于右边right的最小值r_min
        left = 0     
        right = -1
        l_max = nums[0]
        r_min = nums[-1]

        for i, x in enumerate(nums):
            # todo 从左到右维持左边最大值l_max，寻找右边界right
            if x < l_max:
                right = i
            else:
                # x >= l_max
                l_max = x

            # todo 从右到左维持右边最小值l_min，寻找左边界begin
            if nums[n - i - 1] > r_min:
                left = n - i - 1
            else:
                # nums[n - i - 1] <= r_min
                r_min = nums[n - i - 1]

        return right - left + 1


# 方法2：分两次遍历
class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Initialize
        n = len(nums)
        l = 0
        r = -1
        l_max = nums[0]
        r_min = nums[-1]

        # Find the right boundary (end) by maintaining the maximum value from left to right
        for i, x in enumerate(nums):
            if x < l_max:
                r = i
            else:
                l_max = nums[i]

        # Find the left boundary (begin) by maintaining the minimum value from right to left
        for i in range(n - 1, -1, -1):
            x = nums[i]
            if x > r_min:
                l = i
            else:
                r_min = x

        return r - l + 1

if __name__ == '__main__':
    nums = 
    print(Solution().findUnsortedSubarray(nums))
