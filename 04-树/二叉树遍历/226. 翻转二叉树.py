"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

示例 1：
         4
       /   \
      2     7
     / \   / \
    1   3 6   9
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
         4
       /   \
      7     2
     / \   / \
    9   6 3   1

示例 2：
     2
   /   \
  1     3
输入：root = [2,1,3]
输出：[2,3,1]
     2
   /   \
  3     1

示例 3：
输入：root = []
输出：[]

提示：
树中节点数目范围在 [0, 100] 内
-100 <= Node.value <= 100
"""
from myTreeNode import *


# 方法1：递归(前序遍历或者后序遍历都可以，但是中序遍历不行)
# 自顶向下(前序遍历)，或者自底向上(后续遍历都可以)，只要交换每层节点的左右子节点
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 定义：将以 root 为根的这棵二叉树翻转，返回翻转后的二叉树的根节点
        if not root:
            return None

        # 自顶向下:从第一层开始，对每一层node的左右子节点进行翻转
        root.left, root.right = root.right, root.left

        # 利用函数定义，先翻转左右子树
        self.invertTree(root.left)
        self.invertTree(root.right)

        # 自底向上：从最后一层开始，翻转每个节点左右子节点
        # root.left, root.right = root.right, root.left

        # 和定义逻辑自恰：以 root 为根的这棵二叉树已经被翻转，返回 root
        return root


# 方法2： 迭代(按照BFS层序遍历的方法，分别交换每层的左右节点)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 遍历二叉树，交换每个节点的左右节点。
        if not root:
            return None

        # 按照层级遍历，从上到下，从左往右，依次交换每一层左右节点
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            node.left, node.right = node.right, node.left
            
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

        return root



