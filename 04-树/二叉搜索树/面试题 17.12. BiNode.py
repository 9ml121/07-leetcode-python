"""
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

注意：本题相对原题稍作改动

 

示例：

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
提示：

节点数量不会超过 100000。
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        # 二叉搜索树原地转换为单向链表，返回链表head节点
        self.ans = None
        self.pre = self.ans  # 记录前驱节点

        def dfs(root: TreeNode) -> None:
            if not root:
                return

            dfs(root.left)

            # todo 中序位置：修改前驱节点和当前节点的指针即可，类似 206. 反转链表.py
            root.left = None
            if self.pre:
                self.pre.right = root
            else:
                # 当第一次执行到下面这一行代码，恰好是在最左下角，此时 self.pre = None，
                # 其他任何时候 self.pre 都不是 None。
                self.ans = root
            self.pre = root  # 记录前驱节点

            dfs(root.right)

        dfs(root)
        return self.ans
