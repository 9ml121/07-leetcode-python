"""
给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。



示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。


提示：
链表中节点的数目范围是 [0, 10^4]
-10^5 <= Node.value <= 10^5
pos 为 -1 或者链表中的一个 有效索引 。


进阶：你能用 O(1)（即，常量）内存解决此问题吗？
"""
from myListNode import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.value = x
#         self.next = None



# todo 方法 1：快慢指针。快指针每次移动两个节点，慢指针每次移动一个节点。(龟兔赛跑算法)
# 优点：时间O(n) 内存 O(1)
class Solution:
    # 写法1
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """pos 来表示链表尾连接到链表中的位置,判断链表head是否有环 """
        # todo slow和fast都指向头节点，slow每次走一步，fast每次走2步，如果相遇，证明有环
        slow = head
        fast = head
        while fast and fast.next:  # 无环情况下，保证fast来到最后一个节点或者None
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                # 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
                return True
            
        # 如果fast或者它后一个节点为空，能够跳出循环，证明无环
        return True

  
    # 写法2
    def hasCycle2(self, head: ListNode) -> bool:
        # 判断链表head是否有环
        if not head or not head.next:
            return False

        # todo slow指向头节点，fast指向头节点的下一个节点，slow每次走一步，fast每次走2步，如果相遇，证明有环
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True



# 方法 2：哈希集合记录已经遍历的节点，如果有环，会有节点重复遍历
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        vis = set()
        p = head
        while p:
            if p in vis:
                # 如果有节点重复遍历，证明有环
                return True
            vis.add(p)
            p = p.next
            
        # 如果打破循环，说明链表有空节点，证明无环
        return False
