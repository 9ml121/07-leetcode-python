"""
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。



示例 1：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

示例 2：
输入：nums = [0,0,0], target = 1
输出：0


提示：
3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""
from typing import List


# todo 排序 + 左右双指针
# 类似：A-滑动窗口&双指针\双指针\15. 三数之和.py

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 从 nums 中选出三个整数，使它们的和与 target 最接近,返回这三个数的和。
        ans = 0
        # min_diff 记录选出3数之和与target的最小绝对差值
        min_diff = float('inf')
        n = len(nums)
        # 预排序
        nums.sort()

        # 枚举第一个数字
        for i in range(n - 2):
            # 剪枝：相邻元素相同，直接跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 因为数组有序，可以通过同向双指针来求最接近target的三数之和
            l, r = i + 1, n - 1
            while l < r:
                total = nums[l] + nums[r] + nums[i]
                diff = total - target

                # 如果差值比之前的最小差值更小，则更新最小差值和结果
                if abs(diff) < min_diff:
                    min_diff = abs(diff)
                    ans = total

                if diff > 0:
                    r -= 1
                    # 剪枝：右边相邻元素相同，跳过
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif diff < 0:
                    l += 1
                    # 剪枝：左边相邻元素相同，跳过
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                else:
                    # diff == 0, 绝对差值肯定最小，题目保证只有1个解，因此可以直接返回
                    return total

        return ans


