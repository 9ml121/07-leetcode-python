"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
例如，给定 1->2->3->3->4->4->5，返回 1->2->5。
例如，给定 1->1->1->2->3，返回 2->3。

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.value <= 100
题目数据保证链表已经按升序 排列
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法1：快慢指针
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """删除排序链表中的重复元素, 只保留原始链表中 没有重复出现 的数字"""
        # 与83题不同的是head的头节点可能也被删除，所以需要一个虚拟头节点
        dummy = ListNode(next=head)

        # slow是待修改指针的节点，fast是下一个没有重复元素的节点
        slow = dummy
        fast = head
        while fast:
            if fast.next and fast.val == fast.next.val:
                while fast.next and fast.val == fast.next.val:
                    fast = fast.next
                fast = fast.next
                if not fast:
                    slow.next = None
            else:
                slow.next = fast
                slow = slow.next
                fast = fast.next

        return dummy.next
    

# todo 方法2：单指针
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """删除排序链表中的重复元素, 只保留原始链表中 没有重复出现 的数字"""
        # 与83题不同的是head的头节点可能也被删除，所以需要一个虚拟头节点
        dummy = ListNode(next=head)

        # cur是待修改指针的节点
        cur = dummy
        while cur.next and cur.next.next:  # head至少2个节点才可能有重复
            # todo 提前记录cur.next节点的值，然后判断cur.next的下一个节点值是否跟它重复
            val = cur.next.val  
            if cur.next.next.val == val:
                # 如果重复，将cur.next切换到下下节点
                while cur.next and cur.next.val == val:
                    cur.next = cur.next.next
            else:
                # 如果不重复，将cur节点切换到下节点
                cur = cur.next

        return dummy.next
