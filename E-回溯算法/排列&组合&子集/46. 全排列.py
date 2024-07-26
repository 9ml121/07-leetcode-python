"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]

示例 3：
输入：nums = [1]
输出：[[1]]


提示：

1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
"""
import collections
import itertools
from typing import List


# 回溯写法1：使用标记数组vis
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nums不含重复元素，返回nums所有的全排列
        ans = []
        n = len(nums)

        def dfs(vis=[False]*n, path=[]):
            if len(path) == n:
                ans.append(path[:]) # 拷贝path
                return

            for i, x in enumerate(nums):
                if vis[i]:
                    continue

                vis[i] = True
                path.append(nums[i])
                dfs(vis, path)
                vis[i] = False
                path.pop()

        dfs()
        return ans

# 回溯写法2: 递归函数参数传入nums，每一次递归都是重构新的nums数组
class Solution2:
    def permute(self, nums):
        ans = []

        def dfs(nums, path=[]):
            if not nums:
                ans.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        dfs(nums)
        return ans
    
    
# 回溯写法3: 不用标记数组vis, 直接在原来数组nums上进行交换元素位置
# 注意：这个交换的方式会打乱输出结果的原来字典序
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nums不含重复元素，返回nums所有的全排列
        ans = []
        n = len(nums)
    
        def dfs(i=0):
            # 所有数都填完了
            if i == n:
                ans.append(nums[:]) # 拷贝nums
                return
                
            for j in range(i, n):
                # todo 动态维护数组
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i + 1) # todo 注意：这里是对i下一个数递归，不是j
                nums[i], nums[j] = nums[j], nums[i]

        dfs()
        return ans


    
# 写法4：调用 itertools.permutations()
class Solution3:
    def permute(self, nums: List[int]):
        return list(itertools.permutations(nums))


# 方法 5：bfs(不推荐)
# 广度优先算法在解决全排列问题时的时间复杂度较高，因为全排列问题的解空间非常大。因此，回溯算法通常更适合解决全排列问题。
class Solution5:
    def permute(self, nums):
        result = []
        queue = collections.deque()
        queue.append([])

        while queue:
            path = queue.popleft()

            if len(path) == len(nums):
                result.append(path)

            for num in nums:
                if num not in path:
                    # queue 在每一层会添加一个临时 path节点
                    queue.append(path + [num])

        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permute(nums))
    print(Solution2().permute(nums))
    print(Solution4().permute(nums))
    print(Solution5().permute(nums))
    print(list(itertools.permutations(nums)))
