"""
给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。
这条路径可能经过也可能不经过根节点 root 。
两节点之间路径的 长度 由它们之间边数表示。

示例 1：
            1
           / \
          2   3
         / \
        4   5
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。

示例 2：
输入：root = [1,2]
输出：1


提示：
树中节点数目在范围 [1, 10^4] 内
-100 <= Node.value <= 100
"""
from myTreeNode import *

"""
需要明确3个定义:
1.树的深度定义: 为根节点到最远叶子节点的最长路径上的节点数。
2.树的直径定义: 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。
3.两节点之间路径定义: 两节点之间路径的 长度 由它们之间边数表示。(也就是树的总节点个数-1)

             9
              \
               1
             /  \
            2    3
           / \    \
          4  5     6
它的最长直径是 4，即 [4,2,1,3,6] 或者 [5,2,1,3,6] 这几条「直径」的长度。没有经过根节点
解决这题的关键在于，每一条二叉树的「直径」长度，就是一个节点的左右子树的最大深度之和。
"""


# todo 遇到子树问题，首先想到的是给函数设置返回值，然后在后序位置做文章。
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """求二叉树的直径, 就是计算每个节点左右子树高度之和的最大值"""
        maxL = 0  # 全局变量,代表二叉树中每个节点左右子树高度和的最大值

        def dfs(root) -> int:
            """返回每个节点左右子树高度之和， 同时更新每个节点左右子树高度之和的最大值
            """
            nonlocal maxL
            # 节点为空时，左右高度都为0
            if root is None:
                return 0

            # 左右子节点为根的子树深度
            leftH = dfs(root.left)
            rightH = dfs(root.right)

            # 后续位置更新左右子树高度之和的最大值
            maxL = max(leftH + rightH, maxL)

            # 返回该节点为根的子树的深度
            return max(leftH, rightH) + 1

        dfs(root)
        return maxL


if __name__ == '__main__':
    # root = TreeNode(1, TreeNode(2, TreeNode(4, None,  None),  TreeNode(5, None,  None)),  TreeNode(3, None,  None))
    arr = [1, 2, 3, 4, 5, 6, 7]  # 4
    root = buildTree(arr)
    print(Solution().diameterOfBinaryTree(root))

    # diameterOfBinaryTree(TreeNode.create([1, 2, null, 3, 5, null, null, 4, 2]));
