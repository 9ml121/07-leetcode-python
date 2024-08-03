"""
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

示例1：
    3
   / \
  9  20
    /  \
   15   7
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2


提示：
树中节点的数量在 [0, 104] 区间内。
-100 <= Node.val <= 100
"""
from myTreeNode import *


# dfs方法1：分解问题思路(动态规划思路)：dfs有返回值
# 一棵二叉树的最大深度可以通过子树的最大深度推导出来，这就是分解问题计算答案的思路。
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """计算二叉树的最大深度: 分解问题思路, 递归函数带返回值，返回子树的最大深度"""
        if not root:
            return 0

        # 利用定义，计算左右子树的最大深度
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        # 整棵树的最大深度等于左右子树的最大深度取最大值，
        # 然后再加上根节点自己
        return max(left_depth, right_depth) + 1


# dfs方法2：遍历思路:用一个全局变量更新最大深度，dfs无返回值
# 遍历一遍二叉树，用一个外部变量记录每个节点所在的深度，取最大值就可以得到最大深度。
def maxDepth2(root: Optional[TreeNode]) -> int:
    """递归思路：用全局变量"""
    # 记录最大深度
    maxDepth = 0

    def dfs(root: TreeNode, curDepth: int) -> None:
        """递归函数无返回值, depth  参数用来记录当前节点的深度"""
        if not root:
            return
        # 前序位置: 每递归一次，深度+ 1，同时更新最大深度
        curDepth += 1
        nonlocal maxDepth
        maxDepth = max(maxDepth, curDepth)

        dfs(root.left, curDepth)
        dfs(root.right, curDepth)

    dfs(root, 0)
    return maxDepth


# bfs方法：(队列实现)
def maxDepth3(root: Optional[TreeNode]) -> int:
    """计算二叉树的最大深度: 广度优先遍历解法"""
    if not root:
        return 0

    maxDepth = 1
    queues = collections.deque([(root, maxDepth)])

    while queues:
        node, maxDepth = queues.popleft()
        if node.left:
            queues.append((node.left, maxDepth + 1))
        if node.right:
            queues.append((node.right, maxDepth + 1))

    return maxDepth


if __name__ == '__main__':
    # 给定二叉树 [3,9,20,null,null,15,7]，
    root = TreeNode(3, TreeNode(9, None, None),
                    TreeNode(20, TreeNode(15, None, None),
                             TreeNode(7, None, None)))

    print(maxDepth(root))
    print(maxDepth3(root))

    # TreeNode.create([3, 9, 20, null, null, 15, 7])
