"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]


提示：

链表中节点数目为 n
1 <= n <= 500
-500 <= Node.value <= 500
1 <= left <= right <= n


进阶： 你可以使用一趟扫描完成反转吗？
"""
from typing import Optional
from myListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# todo 指针修改 + 链表拼接
# 写法1: 三指针(left前驱节点p0，left节点p0.next, right节点pre, right后继节点cur)
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
        # todo 核心在于取出需要反转的这一小段链表，反转完后再插入到原先的链表中
        dummy = ListNode(next=head)

        # 1.p0指向left前驱节点, p0.next指向left节点： 1-> 2->3->4 ->5, p0=1
        p0 = dummy
        for _ in range(left-1):
            p0 = p0.next

        # 执行 206. 反转链表.py 的逻辑
        # 1-> 2->3->4 ->5 => 1—> 4->3->2 ->5
        pre = None      # 2.反转之后的链表头节点, 也就是反转前的right节点
        cur = p0.next   # 3.待反转链表头节点2 -> 链表反转之后的后继节点5
        for _ in range(right - left + 1):
            # 1.保留下一个待反转节点联系方式：3,4,5
            nxt = cur.next
            # 2.指针修改
            cur.next = pre # 2->None, 3->2->None, 4->3->2->None
            pre = cur # 2,3,4
            cur = nxt # 3,4,5

        # 3.链表拼接
        p0.next.next = cur
        p0.next = pre   

        return dummy.next

# 写法2：四点法


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
        # todo 核心在于取出需要反转的这一小段链表，反转完后再插入到原先的链表中
        dummy = ListNode(next=head)
        
        pre = None
        cur = head
        i = 0
        # todo 四点分别代表反转前left的前驱节点，left节点，right节点，right的后驱节点
        p1 = dummy
        p2 = p3 = p4 = None 
        while cur:
            i += 1
            nxt = cur.next
            if m < i <= n:
                cur.next = pre  # 指针修改
            if i == m - 1:
                p1 = cur
            if i == m:
                p2 = cur
            if i == n:
                p3 = cur
            if i == n + 1:
                p4 = cur
            pre = cur
            cur = nxt
            
        # 链表拼接
        p1.next = p3
        p2.next = p4
        
        return dummy.next

# 写法3：两指针（比较难理解）
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 反转从位置 left 到位置 right 的链表节点，返回 反转后的链表
        dummy = ListNode(next=head)

        # 1-> 2->3->4 ->5 => 1—> 4->3->2 ->5
        # pre：反转前left的上一个节点：1
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next

        # cur：反转前left节点：2
        cur = pre.next
        for _ in range(right - left):
            # 1.保留反转后下一个节点联系方式：3,4
            nxt = cur.next
            # 2.修改指针:2->4, 3->2
            cur.next = nxt.next # 2->4, 2->5
            nxt.next = pre.next # 3->2, 4->3
            pre.next = nxt      # 1->3, 1->4

        return dummy.next


if __name__ == '__main__':
    s = Solution()
    # head = ListNode(1)
    # head.next = ListNode(2)
    # head.next.next = ListNode(3)
    # head.next.next.next = ListNode(4)
    # head.next.next.next.next = ListNode(5)

    nums = [1, 2, 3, 4, 5]
    head = ListNode.fromList(nums)
    print(f'init : {head}')
    s.reverseBetween(head, 2, 4)
