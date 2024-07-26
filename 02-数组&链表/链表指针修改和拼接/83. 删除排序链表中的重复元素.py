"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。


示例 1：
输入：head = [1,1,2]
输出：[1,2]

示例 2：
输入：head = [1,1,2,3,3]
输出：[1,2,3]


提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.value <= 100
题目数据保证链表已经按升序 排列
"""
from typing import Optional
from myListNode import ListNode


# 方法1：快慢指针
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """删除已排序链表中的的重复元素, 返回已排序的链表"""
        # slow是待修改指针的节点，fast是要和slow比较是否是重复值的节点
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next
            if fast.val == slow.val:
                # 如果快慢指针节点值相同，就将慢指针next指向快指针的下一个节点
                slow.next = fast.next
            else:
                # 否则，慢指针直接跳到快指针节点
                slow = fast

        return head

# todo 方法2：单指针(推荐！)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """删除已排序链表中的的重复元素, 返回已排序的链表"""
        p = head
        while p and p.next:
            if p.next.val == p.val:
                # p.next是重复元素节点，将p.next切换到下下个节点
                p.next = p.next.next
            else:
                # p.next不是重复元素节点，将p切换到p.next
                p = p.next
        
        return head

if __name__ == '__main__':
    sol = Solution()
    node = ListNode.fromList([1, 1, 2])
    print(sol.deleteDuplicates(node))
    # print(sol2.deleteDuplicates(ListNode.fromList([1, 1, 2, 3, 3])))
