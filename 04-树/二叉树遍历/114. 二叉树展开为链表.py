"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：
1.展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
2.展开后的单链表应该与二叉树 先序遍历 顺序相同。

示例 1：
          1                 1
        /  \                 \
       2    5      ==>        2
     / \     \                 \
    3   4     6                 3
                                 \
                                  4
                                   \
                                    5
                                     \
                                      6
输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [0]
输出：[0]
提示：

树中结点数在范围 [0, 2000] 内
-100 <= Node.value <= 100
进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？
"""
from typing import Optional

from myTreeNode2 import TreeNode

"""
思路：
首先将根节点的左子树变成链表
其次将根节点的右子树变成链表
最后将变成链表的右子树放在变成链表的左子树的最右边

这就是一个递归的过程，递归的一个非常重要的点就是：
    不去管函数的内部细节是如何处理的，我们只看其函数作用以及输入与输出!!!
对于函数flatten来说：
函数作用：将一个二叉树，原地将它展开为链表
输入：树的根节点
输出：无
"""


# 方法1: 后续遍历
def flatten(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if not root:
        return

    # 1.将根节点的左/右子树变成链表
    flatten(root.left)
    flatten(root.right)

    '''后续遍历位置'''
    left = root.left
    right = root.right

    # 2.把树的右边换成左边的链表，左边置空
    root.left = None
    root.right = left

    # 3.找到树的最右边的节点，连接上原来的右节点right
    tmp = root
    while tmp.right:
        tmp = tmp.right
    tmp.right = right


