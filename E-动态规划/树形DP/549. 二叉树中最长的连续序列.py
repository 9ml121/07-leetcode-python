"""
给定二叉树的根 root ，返回树中最长连续路径的长度。
连续路径是路径中相邻节点的值相差 1 的路径。此路径可以是增加或减少。

例如， [1,2,3,4] 和 [4,3,2,1] 都被认为有效，但路径 [1,2,4,3] 无效。
另一方面，路径可以是子-父-子顺序，不一定是父子顺序。



示例 1:



输入: root = [1,2,3]
输出: 2
解释: 最长的连续路径是 [1, 2] 或者 [2, 1]。


示例 2:



输入: root = [2,1,3]
输出: 3
解释: 最长的连续路径是 [1, 2, 3] 或者 [3, 2, 1]。


提示：

树上所有节点的值都在 [1, 3 * 104] 范围内。
-3 * 104 <= Node.val <= 3 * 104
"""

from myTreeNode2 import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # 返回树中最长连续路径的长度。
        # 连续路径是路径中相邻节点的值相差 1 的路径。此路径可以是增加或减少。
        maxLen = 0

        def dfs(node):
            # 返回子节点到当前根节点连续上升和连续下降的节点个数
            if not node:
                return [1, 1]

            left = dfs(node.left)
            right = dfs(node.right)

            if node.left:
                # 左上升
                if node.val == node.left.val + 1:
                    left[0] += 1
                else:
                    left[0] = 1
                # 左下降
                if node.val == node.left.val - 1:
                    left[1] += 1
                else:
                    left[1] = 1
            if node.right:
                # 右上升
                if node.val == node.right.val + 1:
                    right[0] += 1
                else:
                    right[0] = 1
                # 右下降
                if node.val == node.right.val - 1:
                    right[1] += 1
                else:
                    right[1] = 1
            nonlocal maxLen
            maxLen = max(maxLen, left[0] + right[1] - 1, left[1] + right[0] - 1)
            return [max(left[0], right[0]), max(left[1], right[1])]

        dfs(root)
        return maxLen


# 前序遍历
class Solution2:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        maxLen = 0

        def dfs(node, parent, inr, dcr) -> None:
            nonlocal maxLen
            if not node:
                return

            # 前序遍历
            if parent and node.val == parent.val + 1:
                inr += 1
            else:
                inc = 1

            if parent and node.val == parent.val - 1:
                dcr -= 1
            else:
                dcr = 1
            maxLen = max(maxLen, inc)

            dfs(node.left, node, curLen)
            dfs(node.right, node, curLen)

        dfs(root, None, 0)
        return maxLen


if __name__ == '__main__':
    nums = [3, 1, None, None, 2]  # 2
    root = insert(nums)
    print(Solution().longestConsecutive(root))
