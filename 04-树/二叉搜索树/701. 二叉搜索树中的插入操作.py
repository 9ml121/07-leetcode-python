"""
给定二叉搜索树（BST）的根节点 root 和要插入树中的值 value ，将值插入二叉搜索树。
返回插入后二叉搜索树的根节点。

输入数据 保证 ，新值和原始二叉搜索树中的任意节点值都不同。
注意，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 任意有效的结果 。

示例 1：
        4
       / \
      2  7
    / \
   1  3
输入：root = [4,2,7,1,3], value = 5
输出：[4,2,7,1,3,5]
         4
       /  \
      2    7
    / \   /
   1  3  5
解释：另一个满足题目要求可以通过的树是：
        5
      /  \
     2    7
    / \
   1   3
       \
        4

示例 2：
        40
       /  \
      20   60
     / \   / \
    10 30 50 70
输入：root = [40,20,60,10,30,50,70], value = 25
输出：[40,20,60,10,30,50,70,null,null,25]
         40
       /    \
     20      60
    /  \    /  \
   10  30  50  70
       /
      25

示例 3：
        4
       / \
      2  7
    / \
   1  3
输入：root = [4,2,7,1,3,null,null,null,null,null,null], value = 5
输出：[4,2,7,1,3,5]


提示：

树中的节点数将在 [0, 10^4]的范围内。
-10^8 <= Node.value <= 10^8
所有值 Node.value 是 独一无二 的。
-10^8 <= value <= 10^8
保证 value 在原始BST中不存在。
"""
from myTreeNode import *

'''
对数据结构的操作无非遍历 + 访问，遍历就是「找」，访问就是「改」。
具体到这个问题，插入一个数，就是先找到插入位置，然后进行插入操作。

上一个问题，我们总结了 BST 中的遍历框架，就是「找」的问题。直接套框架，加上「改」的操作即可。
一旦涉及「改」，就类似二叉树的构造问题，函数要返回 TreeNode 类型，并且要对递归调用的返回值进行接收。
'''


# 方法 1：递归语法
# todo:一旦涉及「改」，就类似二叉树的构造问题，函数要返回 TreeNode 类型，并且要对递归调用的返回值进行接收。
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """往二叉搜索树中插入新元素,返回新的二叉树根节点对象"""
        # 递归边界：如果根节点为空，返回新的构造节点
        if root is None:
            return TreeNode(val)

        # 构造 root 的左右节点
        if root.val > val:  # 要插入的节点在左边
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:  # 要插入的节点在右边
            root.right = self.insertIntoBST(root.right, val)

        # 最后返回构造之后的根节点
        return root


# 方法 2：迭代语法
class Solution2:
    def insertIntoBST2(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """往二查搜索树中插入新元素,返回新的二叉树根节点对象"""
        if not root:
            return TreeNode(val)

        p = root  # p指向二叉树中能够插入val的节点的父节点
        while p:
            if p.val > val:
                if not p.left:
                    p.left = TreeNode(val)
                    break
                else:
                    p = p.left

            if p.val < val:
                if not p.right:
                    p.right = TreeNode(val)
                    break
                else:
                    p = p.right
        return root
