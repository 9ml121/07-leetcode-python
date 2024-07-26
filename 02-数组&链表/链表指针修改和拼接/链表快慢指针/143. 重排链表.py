"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


示例 1：
输入：head = [1,2,3,4]
输出：[1,4,2,3]

示例 2：
输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]

提示：
链表的长度范围为 [1, 5 * 10^4]
1 <= node.value <= 1000
"""
from typing import Optional

from myListNode import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # Step1 快慢指针寻找链表的中间节点
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # fast指向最后一个节点，或者最后一个节点的前节点
        # slow指向中间节点, 或者第一个中间节点

        # Step2 将链表从中间分为 2 部分
        second_head = slow.next
        slow.next = None
      

        # Step3 反转链表后半部分节点
        pre, cur = None, second_head
        while cur:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
        second_head = pre

        # Step4 交叉合并两链表
        p1, p2 = head, second_head
        while p2:
            next1 = p1.next
            next2 = p2.next
            p1.next = p2
            p2.next = next1
            p1 = next1
            p2 = next2
      