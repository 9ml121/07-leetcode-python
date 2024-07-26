"""
给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例 1:
         1
       /   \
      2     3
       \     \
        5     4
输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

示例 2:
输入: [1,null,3]
输出: [1,3]

示例 3:
输入: []
输出: []


提示:
二叉树的节点个数的范围是 [0,100]
-100 <= Node.val <= 100
"""
from myTreeNode import *


# bfs方法
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        dq = collections.deque([root])

        while dq:
            level_size = len(dq)
            res.append(dq[-1].val)  # 每次遍历只搜集队列最后一个节点的值

            for _ in range(level_size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res
