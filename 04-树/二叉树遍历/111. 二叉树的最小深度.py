"""
给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明：叶子节点是指没有子节点的节点。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：2

示例 2：
输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

提示：
树中节点数的范围在 [0, 105] 内
-1000 <= Node.value <= 1000
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # bfs层序遍历：
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 特判
        if not root:
            return 0

        depth = 1  # 根节点算第一层
        queues = [(root, depth)]
        while queues:
            cur, depth = queues.pop(0)
            # 最先到达叶子节点，就是最小深度
            if not cur.left and not cur.right:
                return depth
            if cur.left:
                queues.append((cur.left, depth + 1))
            if cur.right:
                queues.append((cur.right, depth + 1))

        return depth


if __name__ == '__main__':
    root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
    cls = Solution()
    print(cls.minDepth(root))
