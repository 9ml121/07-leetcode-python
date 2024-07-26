"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。



示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]

示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

示例 3：
输入：head = []
输出：[]


提示：
链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105


进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
"""
from myListNode import *


# 考察点：归并排序， 分治算法
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 只有0个或者1个节点，直接返回
        if not head or not head.next:
            return head

        # 使用快慢指针找到中间节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 此时slow处于中间或中间靠左的节点
        mid = slow.next
        slow.next = None

        # 递归调用进行链表排序
        left = self.sortList(head)
        right = self.sortList(mid)

        # 后序位置：合并2个有序链表
        return self.merge(left, right)

    def merge(self, node1: ListNode, node2: ListNode):
        dummy = ListNode(0)
        p = dummy
        while node1 and node2:
            if node1.val <= node2.val:
                p.next = node1
                node1 = node1.next
            else:
                p.next = node2
                node2 = node2.next
            p = p.next

        p.next = node1 if node1 else node2
        return dummy.next
