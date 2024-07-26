"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

 

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
 

提示：

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""


from typing import List
# todo 排序 + 双指针
# 解法同 A-滑动窗口&双指针\双指针\15. 三数之和.py， 只不过多套一层循环

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 返回满足nums四数之和为target的不重复四元组
        ans = []
        nums.sort()
        n = len(nums)

        # 枚举第一个数字
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 枚举第二个数字
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                # 枚举第三，四个数字（从[j..n-1]向中间靠拢    
                l, r = j+1, n-1
                while l < r:
                    if l > j+1 and nums[l] == nums[l-1]:
                        l += 1
                        continue
                    if r < n-1 and nums[r] == nums[r + 1]:
                        r -= 1
                        continue
                    
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        
        return ans
