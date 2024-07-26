"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。
（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]


提示：
树中节点数目在范围 [0, 2000] 内
-100 <= Node.val <= 100
"""

from myTreeNode import *


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS写法 1
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = collections.deque([root])
        res = []
        level = 0  # 当前层数

        while dq:
            level_size = len(dq)
            level_vals = []
            level += 1
            for _ in range(level_size):
                cur_node = dq.popleft()
                level_vals.append(cur_node.val)

                if cur_node.left:
                    dq.append(cur_node.left)
                if cur_node.right:
                    dq.append(cur_node.right)

            if level % 2 == 1:
                res.append(level_vals)
            else:
                res.append(level_vals[::-1])

        return res


# BFS写法 2：
class Solution2:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = collections.deque([root])
        res = []
        level = 1  # 当前层数

        while dq:
            level_size = len(dq)
            # 与写法 1 不同点，就是这里用 dq来搜集节点值，奇数层从尾部添加，偶数层从头部添加
            level_vals = collections.deque()

            for _ in range(level_size):
                cur_node = dq.popleft()
                if level % 2 == 0:
                    level_vals.appendleft(cur_node.val)
                else:
                    level_vals.append(cur_node.val)

                if cur_node.left:
                    dq.append(cur_node.left)
                if cur_node.right:
                    dq.append(cur_node.right)

            res.append(list(level_vals))
            level += 1

        return res


if __name__ == '__main__':
    root = [3, 9, 20, None, None, 15, 7]
    node = buildTree(root)
    print(Solution().zigzagLevelOrder(node))
