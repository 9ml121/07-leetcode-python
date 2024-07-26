"""
题目描述：
给你一个链表的头节点 head 和一个整数 k ，旋转链表，使其每个节点向右移动 k 个位置。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

示例 2：
输入：head = [0,1,2], k = 4
输出：[2,0,1]

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 旋转链表
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """将链表每个节点向右移动 k 个位置
        方法1：快慢指针找倒数第k个节点
        """
        # 链表长度为0或者1或者k=0, 直接返回
        if not head or not head.next or k == 0:
            return head

        # 1.获取链表长度
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        k = k % length
        if k == 0:
            return head

        # 2.快慢指针找倒数第k个节点 k:[1..n-1)
        slow, fast = head, head
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        # 此时fast来到最后一个节点，slow在倒数第k-1个节点
        newHead = slow.next
        slow.next = None
        fast.next = head

        return newHead