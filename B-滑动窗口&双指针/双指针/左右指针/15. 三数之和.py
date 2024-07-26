"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。

请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。

示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。


提示：
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
from typing import List


# todo 方法1：排序 + 左右双指针(推荐), 注意解法中去重的技巧 O(N^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 返回所有和为 0 且不重复的三元组
        n = len(nums)
        if n < 3:  # 特判
            return []
        
        ans = []
        # 1.预处理：排序
        nums.sort()

        # 2.先枚举第一个数
        for i in range(n - 2):
            # 剪枝1：nums是升序排序，nums[i]>0时，就不用再遍历了
            if nums[i] > 0:
                break
            
            # 剪枝2：需要和上一次枚举的数不相同 [-4,-1,-1,0,1,2]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 3.在枚举第二个数和第三个数：因为有序，可以将 l 和 r 分别从[i..n]区间的两端向中间靠拢，查找和为target的数组
            l, r = i + 1, n - 1
            while l < r:
                # 剪枝3：需要和上一次枚举的数不相同
                if l > i+1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                if r < n-1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue
                    
                total = nums[l] + nums[r] + nums[i]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                            
        return ans


# 方法2：哈希集合，空间换时间 O(n^2)
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        vis = set()

        for i in range(n):
            seen = set()
            for j in range(i + 1, n):
                target = -nums[i] - nums[j]
                if (target in seen) and tuple(sorted([nums[i], nums[j], target])) not in vis:
                    ans.append([nums[i], nums[j], target])
                    vis.add(tuple(sorted([nums[i], nums[j], target])))
                seen.add(nums[j])
        return ans

# 暴力解法：O(n^3)时间超限
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0 \
                            and tuple(sorted([nums[i], nums[j], nums[k]])) not in visited:
                        ans.append([nums[i], nums[j], nums[k]])
                        visited.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return ans

if __name__ == '__main__':
    sol = Solution3()
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0, 0]
    nums = [-2, 0, 0, 2, 2]
    print(sol.threeSum(nums))
