"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。

示例 1:
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]

提示:
1 <= candidates.n <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List


# 组合问题和子集问题是等价的
# 找出 candidates 中所有可以使数字和为 target 的组合 ==》 计算 candidates 中所有和为 target 的子集。
# todo 回溯 + 排序剪枝
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # candidates有重复元素，不可复选，返回candidates 中所有和为 target 的子集
        ans = []
        candidates.sort()  # 排序的是为了后面dfs剪枝
        n = len(candidates)

        def dfs(target, i=0, path=[]):
            if target == 0:
                ans.append(path[:])
                return

            for j in range(i, n):
                x = candidates[j]
                # 大剪枝：因为数组有序，这里可以提前判断退出循环
                if target - x < 0:
                    break

                # 避免重复子集
                if j > i and x == candidates[j - 1]:
                    continue

                path.append(x)
                dfs(target - x, j + 1, path)
                path.pop()

        dfs(target)
        return ans


if __name__ == '__main__':
    cls = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5, 14]
    target = 8
    # candidates = [1, 1, 3, 4, 5, 6]
    # target = 4
    print(cls.combinationSum2(candidates, target))
