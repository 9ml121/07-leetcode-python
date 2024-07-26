"""
给你一个二叉树的根节点 root ，树中每个节点都存放有一个 0 到 9 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：

例如，从根节点到叶节点的路径 1 -> 2 -> 3 表示数字 123 。
计算从根节点到叶节点生成的 所有数字之和 。

叶节点 是指没有子节点的节点。

示例 1：
     1
   /   \
  2     3
输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25

示例 2：
        4
       / \
      9   0
     / \
    5   1
输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026

提示：
树中节点的数目在范围 [1, 1000] 内
0 <= Node.val <= 9
树的深度不超过 10
"""
from myTreeNode import *


# dfs方法1: 没有返回值
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root, val: int) -> None:
            nonlocal res
            next_val = val * 10 + root.val
            # 叶子节点将该条路径数字总和汇总到最后结果
            if not root.left and not root.right:
                res += next_val
                return

            # 这里用 if判断，可以保证 root一定不为空
            if root.left:
                dfs(root.left, next_val)
            if root.right:
                dfs(root.right, next_val)

        dfs(root, 0)  # 题目要求至少有 1 个节点
        return res


# dfs方法2: 有返回值
class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, val: int) -> int:
            if not root:
                return 0
            next_val = val * 10 + root.val
            if not root.left and not root.right:
                return next_val

            return dfs(root.left, next_val) + dfs(root.right, next_val)

        return dfs(root, 0)


# bfs方法
class Solution3:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        dq = collections.deque([(root, root.val)])
        res = 0

        while dq:
            node, path = dq.popleft()
            if node.left:
                dq.append((node.left, path * 10 + node.left.val))
            if node.right:
                dq.append((node.right, path * 10 + node.right.val))
            # 叶子节点汇总结果
            if not (node.left or node.right):
                res += path
        return res


if __name__ == '__main__':
    root = [4, 9, 0, 5, 1]  # 1026
    node = buildTree(root)
    print(Solution2().sumNumbers(node))
