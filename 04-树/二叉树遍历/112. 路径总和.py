"""
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。

判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
如果存在，返回 true ；否则，返回 false 。

叶子节点 是指没有子节点的节点。

示例 1：
        5
       / \
      4   8
     /   / \
    11  13  4
   /  \      \
  7    2      1
输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。(5+4+11+2)

示例 2：
     1
   /   \
  2     3
输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。

示例 3：
输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。

提示：
树中节点的数目在范围 [0, 5000] 内
-1000 <= Node.value <= 1000
-1000 <= targetSum <= 1000
"""

from myTreeNode import *


# 方法 1：dfs => FloodFill(推荐)
# 一直向下找到 叶子节点，如果到 叶子节点 时 sum == 0，说明找到了一条符合要求的路径。
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        return self.hasPathSum(root.left, targetSum - root.val) \
               or self.hasPathSum(root.right, targetSum - root.val)


# 方法 2：bfs
# BFS 使用 队列(或者栈) 保存遍历到每个节点时的路径和，如果该节点恰好是叶子节点，并且 路径和 正好等于 sum，说明找到了解
class Solution2():
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]

        while stack:
            node, pathSum = stack.pop()
            if not node.left and not node.right and pathSum == targetSum:
                return True
            if node.left:
                stack.append((node.left, pathSum + node.left.value))
            if node.right:
                stack.append((node.right, pathSum + node.right.value))
        return False


class Solution3:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        dq = collections.deque()
        dq.append((root, root.val))

        while dq:
            node, path = dq.popleft()
            if not node.left and not node.right and path == targetSum:
                return True
            if node.left:
                dq.append((node.left, path + node.left.value))
            if node.right:
                dq.append((node.right, path + node.right.value))
        return False
