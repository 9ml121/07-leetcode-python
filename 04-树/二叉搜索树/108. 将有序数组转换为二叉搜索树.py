"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。



示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：

示例 2：
输入：nums = [1,3]
输出：[3,1]
解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。


提示：
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 按 严格递增 顺序排列
"""
from myTreeNode import *

# todo 关键点：取中点, 分治思想
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 将有序数组nums转换为一棵 高度平衡 二叉搜索树
        def dfs(i:int, j:int)->TreeNode:
            # 终止条件：
            if i > j:
                return None

            # 建立当前子树的根节点
            # todo 题目要求是高度平衡的二叉搜索树，因此我们必须要取中点
            # 由于是中点，因此左右两部分差不会大于 1，也就是说其形成的左右子树节点数最多相差 1，因此左右子树高度差的绝对值不超过 1
            mid = (i + j) // 2
            root = TreeNode(nums[mid])

            # 左右子树的下层递归
            root.left = dfs(i, mid - 1)
            root.right = dfs(mid + 1, j)

            return root

        return dfs(0, len(nums) - 1)
