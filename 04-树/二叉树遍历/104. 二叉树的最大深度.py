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
树中节点的数量在 [0, 10^4] 区间内。
-100 <= Node.val <= 100
"""
from myTreeNode import *


# todo dfs方法(带返回值)
class Solution:
    # dfs方法1：分解问题思路(动态规划思路)：dfs有返回值
    # 一棵二叉树的最大深度可以通过子树的最大深度推导出来，这就是分解问题计算答案的思路。
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """计算二叉树的最大深度 
        递归写法1：分解问题思路, 递归函数带返回值，返回子树的最大深度
        """
        if not root:
            return 0

        # 利用定义，计算左右子树的最大深度
        left_depth = maxDepth(root.left)
        right_depth = maxDepth(root.right)
        
        # 整棵树的最大深度等于左右子树的最大深度取最大值，然后再加上根节点自己
        return max(left_depth, right_depth) + 1


    # dfs方法2：遍历思路:用一个全局变量更新最大深度，dfs无返回值，递归参数多一个当前节点深度
    # 遍历一遍二叉树，用一个外部变量记录每个节点所在的深度，取最大值就可以得到最大深度。
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        """计算二叉树的最大深度:
        递归写法2：用全局变量更新最大深度，递归函数无返回值, curDepth 参数用来记录当前节点的深度
        """
        # 记录最大深度
        ans = 0

        def dfs(root: TreeNode, curDepth: int) -> None:
            if not root:
                return
            
            # 前序位置: 每递归一次，深度+ 1，同时更新最大深度
            curDepth += 1
            nonlocal ans
            ans = max(ans, curDepth)

            dfs(root.left, curDepth)
            dfs(root.right, curDepth)

        dfs(root, 0)
        return ans


# bfs方法：(队列实现)
def maxDepth3(root: Optional[TreeNode]) -> int:
    """计算二叉树的最大深度: 广度优先遍历解法"""
    if not root:
        return 0

    ans = 1
    dq = collections.deque([(root, ans)])

    while dq:
        node, ans = dq.popleft()
        if node.left:
            dq.append((node.left, ans + 1))
        if node.right:
            dq.append((node.right, ans + 1))

    return ans


if __name__ == '__main__':
    # 给定二叉树 [3,9,20,null,null,15,7]，
    root = TreeNode(3, TreeNode(9, None, None),
                    TreeNode(20, TreeNode(15, None, None),
                             TreeNode(7, None, None)))

    print(maxDepth(root))
    print(maxDepth3(root))

    # TreeNode.create([3, 9, 20, null, null, 15, 7])
