"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。


示例 1：


输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]


提示：

每个链表中的节点数在范围 [1, 100] 内
0 <= Node.value <= 9
题目数据保证列表表示的数字不含前导零
"""
from myListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """请你将两个数相加，并以相同形式返回一个表示和的链表。
        每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
        """
        p1, p2 = l1, l2
        dummy = ListNode(-1)
        p = dummy
        carry = 0
        '''
        l1  1->2-9->None
        l2  9->9
        res 0->2->0->1
        921 + 99 = 1020
        '''
        while p1 or p2 or carry:
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            # 处理进位情况
            carry, val = divmod(val, 10)  # (value//10, value%10)
            p.next = ListNode(val)
            p = p.next

        return dummy.next
