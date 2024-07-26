"""
给定一个单链表的头节点  head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。



示例 1:



输入: head = [-10,-3,0,5,9]
输出: [0,-3,9,-10,null,5]
解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
示例 2:

输入: head = []
输出: []


提示:

head 中的节点数在[0, 2 * 104] 范围内
-105 <= Node.val <= 105
"""
from typing import Optional

from myListNode import ListNode
from myTreeNode import TreeNode


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # 使用快慢指针找到链表中间节点的前一个节点(至少 2 个节点)
        slow, fast = head, head.next
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 此时 slow是中间位置的前一个节点
        # 断开链表，将链表分为左右两部分
        midNode = slow.next
        slow.next = None

        # 创建根节点，并递归构建左右子树
        root = TreeNode(midNode.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(midNode.next)

        return root
