"""
题目描述：给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

示例:
输入: 1->2->3->4
输出: 2->1->4->3

说明:
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

这是一道链表的经典题目，可以使用递归或迭代的方式来解决。具体实现如下：
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """两两交换链表中的节点
        方法1：迭代解法
        """
        pre = dummy = ListNode(0, head)
        p = head
        # 链表有2个节点以上才需要交换
        while p and p.next:
            first = p
            second = p.next
            first.next = second.next
            second.next = first
            # 交换节点之后需要记录前序节点
            pre.next = second
            pre = first
            p = first.next

        return dummy.next


class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """两两交换链表中的节点
        方法1：递归解法
        """
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head

        return second