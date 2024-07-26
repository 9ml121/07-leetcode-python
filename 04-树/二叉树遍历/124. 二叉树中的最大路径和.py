"""
二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。
同一个节点在一条路径序列中 至多出现一次 。
该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。


示例 1：
     1
   /  \
  2    3
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
        -10
       /   \
      9     20
           /  \
          15   7
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42


提示：
树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.value <= 1000
"""
from myTreeNode import *


# dfs方法
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """返回二叉树中的最大路径和"""
        # 初始化最大路径和为负无穷
        max_sum = float('-inf')

        def dfs(node) -> int:
            """递归函数，返回当前节点的最大贡献值"""
            if not node:
                return 0
            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # 后续遍历：更新最大路径和
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            nonlocal max_sum
            max_sum = max(max_sum, left + right + node.val)

            # 返回当前节点的最大贡献值
            return max(left, right) + node.val

        # 调用递归函数，返回最大路径和
        dfs(root)
        return max_sum


if __name__ == '__main__':
    root = [-10, 9, 20, None, None, 15, 7]  # 42
    node = buildTree(root)
    print(Solution().maxPathSum(node))
