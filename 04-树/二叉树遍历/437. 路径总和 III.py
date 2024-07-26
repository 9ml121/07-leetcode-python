"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3


提示:
二叉树的节点个数的范围是 [0,1000]
-10^9 <= Node.value <= 10^9
-1000 <= targetSum <= 1000
"""
from typing import Optional
from myTreeNode import TreeNode
import myTreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 方法 1：双层递归 ==> 空间复杂度O(n) 时间复杂度介于O(nlogn) 和 O(n^2)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 求解出任何一个节点出发到子孙节点的路径中和为指定值。 注意这里，不一定是从根节点出发，也不一定在叶子节点结束。
        def dfs(root: TreeNode, targetSum) -> int:
            # 统计以root节点开始，到叶子节点结束, 和为 targetSum的路径个数
            if not root:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += dfs(root.left, targetSum-root.val)
            ret += dfs(root.right, targetSum-root.val)

            return ret

        if not root:
            return 0

        # 先统计以当前节点开始，到叶子节点结束，和为 targetSum的路径个数
        ret = dfs(root, targetSum)
        # 再递归统计以左右子节点开始，到叶子节点结束，和为 targetSum的路径个数
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)

        # 最后返回以当前节点出发到子孙节点的路径中和为targetSum的所有路径个数
        return ret


# todo 方法 2：回溯 + 前缀和 + 哈希表 ==> 空间复杂度O(n), 时间复杂度O(n)
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # 求解出任何一个节点出发到子孙节点的路径中和为指定值。 注意这里，不一定是从根节点出发，也不一定在叶子节点结束。
        import collections
        
        def dfs(prefix = collections.Counter({0:1}), root: TreeNode = root, path: int = 0) -> int:
            # 遍历二叉树每个节点，统计每个节点前缀和(包含当前节点)
            # prefix字典: key表示当前节点前缀和, val代表对应路径数量
            if not root:
                return 0

            ret = 0
            
            path += root.val
            ret += prefix[path - targetSum]

            prefix[path] += 1
            ret += dfs(prefix, root.left, path)
            ret += dfs(prefix, root.right, path)
            prefix[path] -= 1

            return ret

        return dfs()


if __name__ == '__main__':
    root = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    targetSum = 8
    node = myTreeNode.insert(root)
    print(Solution().pathSum(node, targetSum))
