"""
给你一个整数数组 nums 和一个链表的头节点 head。从链表中移除所有存在于 nums 中的节点后，返回修改后的链表的头节点。

 

示例 1：

输入： nums = [1,2,3], head = [1,2,3,4,5]

输出： [4,5]

解释：



移除数值为 1, 2 和 3 的节点。

示例 2：

输入： nums = [1], head = [1,2,1,2,1,2]

输出： [2,2,2]

解释：



移除数值为 1 的节点。

示例 3：

输入： nums = [5], head = [1,2,3,4]

输出： [1,2,3,4]

解释：



链表中不存在值为 5 的节点。

 

提示：

1 <= nums.length <= 105
1 <= nums[i] <= 105
nums 中的所有元素都是唯一的。
链表中的节点数在 [1, 105] 的范围内。
1 <= Node.val <= 105
输入保证链表中至少有一个值没有在 nums 中出现过。
"""


from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# todo 哈希集合 + 链表


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set_ = set(nums)
        # 注意：dummy 和 p 是同一个节点的引用，修改 p.next 也会修改 dummy.next。
        p = dummy = ListNode(next=head)
        while p.next:
            if p.next.val in set_:
                p.next = p.next.next   # 删除
            else:
                p = p.next  # 向后移动

        return dummy.next
