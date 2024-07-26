"""
给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。



示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]


示例 2：
输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]


提示：
链表中的节点数目为 n
1 <= k <= n <= 5000
0 <= Node.value <= 1000


进阶：你可以设计一个只用 O(1) 额外内存空间的算法解决此问题吗？
"""
from typing import Optional



# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
        
# 写法2（推荐！）
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k 个节点一组翻转链表，返回修改后的链表
        def reverse(head: ListNode, tail: ListNode) -> tuple[ListNode]:
            # head:链表的left节点, tail:链表的right节点的下一个节点, 返回反转之后的链表头节点和尾节点
            pre = None
            cur = head
            while cur != tail:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            # 返回翻转后的头节点和尾节点
            return pre, head

        dummy = ListNode(next=head)
        pre = dummy
        while head:
            # 找k个一组的头节点和尾节点
            tail = head  # head:反转前链表的头节点 -> tail:反转后链表的尾节点的下一个节点
            for _ in range(k):
                if not tail:  # 不足k个节点
                    pre.next = head
                    return dummy.next
                tail = tail.next

            # k个一组节点进行反转
            newHead, newTail = reverse(head, tail)
            # 反转之后的链表拼接
            pre.next = newHead
            pre = newTail
            # head重指向下一组节点的头节点
            head = tail

        return dummy.next
    
    
# 写法1：
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # k 个节点一组翻转链表，返回修改后的链表
        # 预先计算链表节点个数n
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        # 构造虚拟头节点
        dummy = ListNode(next=head)
        # p0是需要反转链表区间的前一个节点，p0.next是反转链表的left节点
        p0 = dummy
    
        #  k 个节点一组进行翻转
        while n >= k:
            n -= k
            # 沿用之前反转链接的逻辑
            # 92. 反转链表II.py   206. 反转链表.py
            pre = None
            cur = p0.next
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                
            # 此时cur是反转前right节点的下一个节点， pre是反转之后的链表头节点
            nxt = p0.next  # 反转前链表的头节点，反转后链表的尾节点
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
            
        return dummy.next
            
                



