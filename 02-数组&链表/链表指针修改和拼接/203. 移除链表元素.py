"""
给你一个链表的头节点 head 和一个整数 value ，请你删除链表中所有满足 Node.value == value 的节点，并返回 新的头节点 。


示例 1：
输入：head = [1,2,6,3,4,5,6], value = 6
输出：[1,2,3,4,5]

示例 2：
输入：head = [], value = 1
输出：[]

示例 3：
输入：head = [7,7,7,7], value = 7
输出：[]


提示：
列表中的节点数目在范围 [0, 10^4] 内
1 <= Node.value <= 50
0 <= value <= 50
"""
from myListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """删除链表中值为val 的节点，并返回 新的头节点 。
        方法 1：迭代方法
        """
        # 创建虚拟节点dummy，使得删除头节点和其他节点的逻辑一致
        dummy = ListNode(next=head)
     
        pre = dummy  # pre指向待删除节点的前驱节点
        while pre.next:
            if pre.next.value == val:
                # 如果待删除节点的值等于val，则将其前驱节点的next指向其后继节点
                pre.next = pre.next.next
            else:
                # 否则将pre指向下一个节点
                pre = pre.next
                
        return dummy.next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """删除链表中值为val 的节点，并返回 新的头节点 。
        方法 2：递归解法，一叉树的后续遍历
        """
        if not head:
            return None

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next
        else:
            return head
