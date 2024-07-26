"""
给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。

示例1：
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

示例 2:
输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]


提示:

n ==  链表中的节点数
0 <= n <= 104
-106 <= Node.value <= 106
"""
import myListNode
from myListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
        第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数
        输入: 1->2->3->4->5->NULL
        输出: 1->3->5->2->4->NULL
        """
        # 1、0 或者 1 个节点直接返回
        if not head or not head.next:
            return head

        # 2.构造奇数链表和偶数链表
        even_head = head.next
        odd, even = head, even_head

        while even and even.next:  # 3个节点以上
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        # 3.将奇数链表和偶数链表合并。
        odd.next = even_head

        print(head)
        return head


if __name__ == '__main__':
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = list2Node(nums=[1, 2, 3, 4, 5])
    print(head)
    node = Solution().oddEvenList(head)
    # print(node)
