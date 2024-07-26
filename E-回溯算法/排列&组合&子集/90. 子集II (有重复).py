"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：
1 <= nums.n <= 10
-10 <= nums[i] <= 10
"""
from typing import List

'''
1。需要先进行排序，让相同的元素靠在一起，如果发现 nums[i] == nums[i-1]，则跳过
- 这段代码和之前标准的子集问题的代码几乎相同，就是添加了排序和剪枝的逻辑。
- 至于为什么要这样剪枝，结合前面的图应该也很容易理解，这样带重复元素的子集问题也解决了
'''


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, start, track, res):
            # 前序位置，每个节点的值都是一个子集
            res.append(list(track))  # 注意：数组track要换成新的对象
            # 从start开始遍历nums数组
            for i in range(start, len(nums)):
                # 剪枝逻辑，值相同的相邻树枝，只遍历第一条
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # 把当前数值添加到走过的路径列表中
                track.append(nums[i])
                # 从下一个数字的位置继续回溯
                backtrack(nums, i + 1, track, res)
                # 回溯过程中要把当前数值从走过的路径中移除
                track.pop()

        res = []
        # 对给定的数组进行排序，这样相同的元素就会排在一起。
        nums.sort()
        # 对数组进行回溯
        backtrack(nums, 0, [], res)
        return res


cls = Solution()
nums = [1, 2, 2]
print(cls.subsetsWithDup(nums))
