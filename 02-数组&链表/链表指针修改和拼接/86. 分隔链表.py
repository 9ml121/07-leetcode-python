"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。



示例 1：
输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

示例 2：
输入：head = [2,1], x = 2
输出：[1,2]


提示：
链表中节点的数目在范围 [0, 200] 内
-100 <= Node.value <= 100
-200 <= x <= 200
"""
from typing import Optional

from myListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 存储小于 x 的节点
        lt_node = ListNode(-1)
        # 存储大于等于 x 的节点
        ge_node = ListNode(-1)
        ge = ge_node
        lt = lt_node

        cur = head
        while cur:
            if cur.val >= x:
                ge.next = cur
                ge = cur
            else:
                lt.next = cur
                lt = cur
            cur = cur.next

        # 将最后一个节点的 next 指针置为 None
        ge.next = None
        # 连接两个链表
        lt.next = ge_node.next

        return lt_node.next
