"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

示例 2：
输入：head = [1], n = 1
输出：[]

示例 3：
输入：head = [1,2], n = 1
输出：[1]


提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.value <= 100
1 <= n <= sz


进阶：你能尝试使用一趟扫描实现吗？
"""
from myListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
# todo 可以使用：快慢指针 | 栈 | 计算链表长度

# todo 方法1：快慢指针查找链表倒数第n个节点 n：[1..sz]
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """删除链表的倒数第 n个节点，并且返回链表的头结点。"""
        # todo dummy节点的好处，可以避免讨论头结点被删除的情况
        dummy = ListNode(next=head)
    
        # slow和fast初始化都指向dummy节点，保证链表至少有2个节点，避免讨论sz=1的情况
        # todo fast指针先走n步, 然后快慢指针一起走，可以保证slow和fast之间永远相隔n个节点
        fast = dummy
        for _ in range(n):
            fast = fast.next

        slow = dummy
        while fast.next:  
            fast = fast.next
            slow = slow.next
            
        # todo 此时fast来到最后一个节点, slow来到倒数第n个节点的前驱节点, 删除倒数第n个节点
        slow.next = slow.next.next

        return dummy.next


# 方法 2：正常思路解法，需要先获取链表长度，然后按照链表删除index节点去操作
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """删除链表的倒数第 n个节点，并且返回链表的头结点。"""
        # 1.计算链表长度
        p = head
        sz = 0
        while p:
            sz += 1
            p = p.next

        # 2.查找倒数第 n个节点，也就是正数索引为 size-n 的节点
        dummy = ListNode(next=head)  
        p = dummy  # p指向要删除节点的前一个节点
        for _ in range(sz - n):
            p = p.next
        p.next = p.next.next

        return dummy.next


# 方法 3：利用栈压入前序节点，最后弹出 n个节点，此时栈顶就是要删除节点的前一个节点
class Solution3:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """删除链表的倒数第 n个节点，并且返回链表的头结点。"""
        st = []
        dummy = ListNode(next=head)
        p = dummy
        while p:
            st.append(p)
            p = p.next
            
        for _ in range(n):
            st.pop()
            
        pre = st[-1]
        pre.next = pre.next.next

        return dummy.next
