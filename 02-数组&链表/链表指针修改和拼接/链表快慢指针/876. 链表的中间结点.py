"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

例如，给定链表 1->2->3->4->5->NULL，返回3。

另一个例子，给定链表 1->2->3->4->5->6->NULL，返回4。

提示：
链表的结点数范围是 [1, 100]
1 <= Node.value <= 100
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """快慢指针寻找链表的中间节点,如果有两个中间结点，则返回第二个中间结点"""
        slow, fast = head, head
        while fast and fast.next:  # 无环情况下，保证fast来到最后一个节点或者None
            slow = slow.next
            fast = fast.next.next
            
        # fast指向最后一个节点，或者None
        # slow指向中间节点或者第二个中间节点
        return slow
