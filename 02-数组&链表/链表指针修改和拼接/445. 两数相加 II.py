"""
题目描述：给定两个非空链表来表示两个非负整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

提示：

链表的长度范围为 [1, 100]
0 <= node.value <= 9
输入数据保证链表代表的数字无前导 0


进阶：如果输入链表不能翻转该如何解决？
"""
from typing import Optional

from myListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next


class Solution2:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表
        方法1：翻转链表
        """

        def reverse(node):
            pre = None
            cur = node

            while cur:
                next_ = cur.next
                cur.next = pre
                pre = cur
                cur = next_
            return pre

        dummy = ListNode(0)
        _l1 = reverse(l1)
        _l2 = reverse(l2)
        carry = 0
        p = dummy
        while _l1 or _l2 or carry:
            val = carry
            if _l1:
                val += _l1.val
                _l1 = _l1.next
            if _l2:
                val += _l2.val
                _l2 = _l2.next
            carry, val = divmod(val, 10)
            p.next = ListNode(val)
            p = p.next

        return reverse(dummy.next)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表
        方法2：不用翻转链表，借助stack实现
        """
        stack1, stack2 = [], []
        p = l1
        while p:
            stack1.append(p.val)
            p = p.next
        p = l2
        while p:
            stack2.append(p.val)
            p = p.next
        carry = 0

        dummy = ListNode(0)
        while stack1 or stack2 or carry:
            val = carry
            if stack1:
                val += stack1.pop()
            if stack2:
                val += stack2.pop()

            carry, val = divmod(val, 10)
            node = ListNode(val)
            node.next = dummy.next
            dummy.next = node
        return dummy.next


if __name__ == '__main__':
    _l1 = ListNode.fromList([7, 2, 4, 3])
    _l2 = ListNode.fromList([5, 6, 4])
    s = Solution()
    node = s.addTwoNumbers(_l1, _l2)
    print(node.toList())
