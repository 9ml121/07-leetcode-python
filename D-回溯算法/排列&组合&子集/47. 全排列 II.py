"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
示例 2：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
import collections
import itertools
from typing import List


# 写法1：回溯算法 + 剪枝
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # nums有重复元素，返回所有不重复的全排列
        ans = []
        n = len(nums)
        nums.sort()  # 排序是为了后面dfs剪枝
        
        def dfs(used=[False]*n, path=[]):
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i, x in enumerate(nums):
                if used[i]:
                    continue
                
                # todo 剪枝：重复数组
                if i > 0 and x == nums[i - 1] and not used[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True
                dfs(used, path)
                used[i] = False
                path.pop()

        dfs()
        return ans


# 方法 2：使用itertools模块的permutations函数(可能会超时)
class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 对给定列表进行排序
        nums.sort()
        # 使用permutations函数生成所有排列
        permutations_list = list(itertools.permutations(nums))
        print(permutations_list)
        # [(1, 1, 2), (1, 2, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1), (2, 1, 1)]

        # 使用collections.Counter去除重复的排列
        unique_permutations = list(collections.Counter(permutations_list).keys())
        print(unique_permutations)
        # [(1, 1, 2), (1, 2, 1), (2, 1, 1)]

        # 将排列转换为列表形式
        result = [list(p) for p in unique_permutations]
        return result


if __name__ == '__main__':
    nums = [1, 1, 2]
    print(Solution2().permuteUnique(nums))
