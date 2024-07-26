"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

示例 1：


输入：head = [1,2,2,1]
输出：true
示例 2：


输入：head = [1,2]
输出：false


提示：

链表中节点数目在范围[1, 10^5] 内
0 <= Node.value <= 9


进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""
from myListNode import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """判断是否为回文链表
        避免使用 O(n) 额外空间的方法就是改变输入。最后记得恢复链表
        1->2->1  1->1   1->2->2->1
        """
        # 链表节点=0或1，返回 True
        if not head or not head.next:
            return True
        # 1.使用快慢指针找到链表的中点。(这里slow最终指向的是中点或者中点偏左)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2.将链表的后半部分反转。
        secondHalf = self.reverseList(slow.next)
        # 3.比较链表前半部分和后半部分是否相同。
        left, right = head, secondHalf
        while right:
            if left.val != right.val:
                self.reverseList(secondHalf)
                return False
            left = left.next
            right = right.next
        # 4.将链表后半部分反转回来。
        self.reverseList(secondHalf)
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            next_ = cur.next
            cur.next = pre
            pre = cur
            cur = next_
        return pre
