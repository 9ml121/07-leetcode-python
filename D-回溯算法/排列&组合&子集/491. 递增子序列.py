"""
给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。
数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

示例 1：
输入：nums = [4,6,7,7]
输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

示例 2：
输入：nums = [4,4,3,2,1]
输出：[[4,4]]

提示：
1 <= nums.length <= 15
-100 <= nums[i] <= 100
"""
from typing import List


# 方法 1：标准回溯解法(遍历多叉树)==》类似 40-组合总和 II (元素有重复不可复选).py
# 不同点：利用排序的方式防止重复使用相同元素的，但这道题不能改变 nums 的原始顺序，所以不能用排序的方式，
# 而是用 used 集合来避免重复使用相同元素。
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        # 找出并返回nums数组中不同的递增子序列，递增子序列中 至少有两个元素
        # 数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况
        ans = []
        n = len(nums)
        
        def dfs(i=0, path=[]):
            if len(path) >= 2:
                ans.append(path[:])
    
            # todo：使用set来对本层元素进行去重，新的一层set都会重新定义（清空）
            used = set()
            for j in range(i, n):
                x = nums[j]
                # 需要搜集的是非严格单调递增数组
                if path and x < path[-1]:
                    continue

                if x in used:
                    continue

                used.add(x)  # 记录这个元素在本层用过了，本层后面不能再用了
                
                path.append(x)
                dfs(i+1, path)
                path.pop()

        dfs(0)
        return ans


if __name__ == '__main__':
    nums = [4, 6, 7, 7]
    print(Solution().findSubsequences(nums))
