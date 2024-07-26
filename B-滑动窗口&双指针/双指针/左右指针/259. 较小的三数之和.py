"""
给定一个长度为 n 的整数数组和一个目标值 target ，寻找能够使条件 nums[i] + nums[j] + nums[k] < target 成立的三元组  i, j, k 个数（0 <= i < j < k < n）。

 

示例 1：

输入: nums = [-2,0,1,3], target = 2
输出: 2 
解释: 因为一共有两个三元组满足累加和小于 2:
     [-2,0,1]
     [-2,0,3]
示例 2：

输入: nums = [], target = 0
输出: 0 
示例 3：

输入: nums = [0], target = 0
输出: 0 
 

提示:

n == nums.length
0 <= n <= 3500
-100 <= nums[i] <= 100
-100 <= target <= 100
"""

# todo 排序 + 左右双指针
# 类似：B-滑动窗口&双指针\双指针\左右指针\1099. 小于 K 的两数之和.py

class Solution:
    def threeSumSmaller(self, nums: list[int], target: int) -> int:
        # 查找nums中三元子数组之和小于target的个数
        nums.sort()  # 预排序
        ans = 0
        n = len(nums)
        
        # 枚举第一个数
        for i in range(n):
            # 左右双指针枚举另外2个数
            l = i+1
            r = n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < target:
                    # 因为数组有序，[l..r)所有的数作为第二个数，和r组成的三数之和都满足条件
                    # 扩大左指针
                    ans += r-l
                    l += 1
                else:
                    # 如果三数之和s>=t, 缩小右指针；
                    r -= 1

        return ans
