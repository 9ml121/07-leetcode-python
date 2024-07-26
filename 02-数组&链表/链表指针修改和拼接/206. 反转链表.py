"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

示例 2：
输入：head = [1,2]
输出：[2,1]

示例 3：
输入：head = []
输出：[]


提示：
链表中节点的数目范围是 [0, 5000]
-5000 <= Node.value <= 5000


进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
"""
from myListNode import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# todo 方法1：双指针迭代方法（推荐！！）
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """反转链表：双指针迭代解法"""
        # 2->3->4->None => None<-2<-3<-4
        pre = None
        cur = head
        while cur:
            nxt = cur.next  # 记录当前节点的下一个节点（留下联系方式）
            cur.next = pre  # 修改指针
            
            # 继续往下走
            pre = cur
            cur = nxt

        # 反转后的新的头节点返回出去
        return pre

# todo 方法2：递归解法（可以理解为一叉树的后续遍历）
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """反转链表：递归解法
        递归调用  reverseList  函数，传入当前节点的下一个节点，返回反转后的新链表的头节点。
        初始节点：1->2->3->4->5->null
        """
        # 最后一个非空节点返回
        if not head or not head.next:
            return head

        # 将当前节点的下一个节点压入系统栈中,注意：这里的newNode就是最后一个节点 5
        ans = self.reverseList(head.next)

        # 后续位置处理（递归返回的过程会执行到）： head=4
        head.next.next = head
        # 避免出现环形链表。
        head.next = None

        # 每层递归函数都返回newNode，也就是最后一个节点
        return ans
    



if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    new_head = Solution().reverseList(head)
    print(new_head)

    nums = [1, 2, 3, 4, 5]
    node = ListNode.fromList(nums)
    # print(f'node = {node}')
    print(Solution().reverseList(node))
    # print(node)


