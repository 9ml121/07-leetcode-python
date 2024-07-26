"""
给定一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。



示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]


提示：

1 <= nums.n <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

"""
import itertools
from typing import List

# todo 回溯算法
# 遍历多叉树，在回溯的过程中记录路径变量（前序遍历/后续遍历都可以）。
'''
1。通过保证元素之间的相对顺序不变来防止出现重复的子集
2。如果想计算所有子集，那只要遍历这棵 多叉树 ，把所有节点的值收集起来
'''

# 写法1：回溯搜索 ==》遍历二叉树，前序位置收集结果
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 返回无重复元素的nums数组所有可能的子集
        ans = []
        n = len(nums)
        
        def dfs(i=0, path=[]):
            # todo 前序位置，每个节点的值都是一个子集, 直接收集结果
            # todo 注意：因为path是可变数据类型，这里要用值拷贝，不能用引用拷贝， 下面3种写法都可以
            # ans.append(path.copy())  
            # ans.append(list(path))
            ans.append(path[:])  
             
            # 枚举下一个数，只能选i后面的数，避免产生重复子集
            for j in range(i, n):
                path.append(nums[j]) # 做选择
                dfs(j + 1, path)  # 通过j+1变换树枝层数，避免产生重复的子集
                path.pop() # 撤销选择

        dfs()
        return ans


# 写法2：回溯搜索==》遍历二叉树，所有组合落在了叶子节点
class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 返回无重复元素的nums数组所有可能的子集
        ans = []
        n = len(nums)
        
        # 时间复杂度：O(n*2^n), 每次递归只有选与不选2个情况，所以总共递归2^n次，copy数组的复杂度是n
        def dfs(i=0, path=[]):
            if i == n:
                ans.append(path[:])
                return

            # 当前数可选，也可以不选
            # 1.不选当前数，直接进入下一层
            dfs(i + 1, path)

            # 2.选择当前数，再进入下一层
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop() # 撤销选择

        dfs()
        return ans


# 写法3：利用itertools组合函数 combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            for elem in itertools.combinations(nums, i):
                ans.append(list(elem))
        return ans
    
if __name__ == '__main__':
    cls = Solution()
    nums = [1, 2, 3]
    print(cls.subsets(nums))
