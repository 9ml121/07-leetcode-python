"""
给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。
这条路径可以经过也可以不经过根节点。
两个节点之间的路径长度 由它们之间的边数表示。

示例 1:
      5
     / \
    4   5
   / \   \
  1   1   5

输入：root = [5,4,5,1,1,5]
输出：2

示例 2:
      1
     / \
    4   5
   / \   \
  4   4   5

输入：root = [1,4,5,4,4,5]
输出：2


提示:
树的节点数的范围是 [0, 104]
-1000 <= Node.val <= 1000
树的深度将不超过 1000
"""
from typing import Optional

import myTreeNode2
from myTreeNode2 import TreeNode

"""
    2
   / \
  2   3
 / \
2   4
注意：不是中序遍历！！！
  
"""


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxLen = 0

        def dfs(node):
            nonlocal maxLen
            if not node:
                return 0

            # 计算左子树和右子树的最长同值路径长度。
            leftLen = dfs(node.left)
            rightLen = dfs(node.right)

            # 计算从当前节点向左子树延伸的同值路径长度
            if node.left and node.left.val == node.val:
                leftLen += 1
            else:
                leftLen = 0
            # 从当前节点向右子树延伸的同值路径长度 right_arrow。
            if node.right and node.right.val == node.val:
                rightLen += 1
            else:
                rightLen = 0
            # 更新 max_length 的值，
            maxLen = max(maxLen, leftLen + rightLen)
            # 返回以当前节点为根节点的同值路径长度中较长的那个。
            return max(leftLen, rightLen)

        dfs(root)
        return maxLen


if __name__ == '__main__':
    nums = [1, 2, 2, 2, 2, 2, 2, 2]
    """
        1
       / \
      2   2
     / \ / \
    2  2 2  2
   /
  2
    """
    root = myTreeNode2.insert(nums)
    print(Solution().longestUnivaluePath(root))
