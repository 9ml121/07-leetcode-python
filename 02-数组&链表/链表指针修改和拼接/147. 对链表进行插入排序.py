"""
给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。

插入排序 算法的步骤:
插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。
每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。

对链表进行插入排序。


示例 1：
输入: head = [4,2,1,3]
输出: [1,2,3,4]

示例 2：
输入: head = [-1,5,3,4,0]
输出: [-1,0,3,4,5]


提示：
列表中的节点数在 [1, 5000]范围内
-5000 <= Node.value <= 5000

"""
from typing import Optional

from myListNode import ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        # sorted_tail表示有序部分链表的最后一个节点
        sorted_tail = head
        while sorted_tail.next:
            if sorted_tail.val <= sorted_tail.next.value:
                sorted_tail = sorted_tail.next
            else:
                cur = sorted_tail.next
                sorted_tail.next = cur.next

                # 对 cur节点在链表 dummy进行插入排序
                pre = dummy
                while pre.next.value < cur.value:
                    pre = pre.next
                # pre处于最后一个小于 cur的节点
                cur.next = pre.next
                pre.next = cur

        return dummy.next
