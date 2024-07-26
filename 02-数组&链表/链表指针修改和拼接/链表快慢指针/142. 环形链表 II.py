"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。


提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.value <= 105
pos 的值为 -1 或者链表中的一个有效索引

"""
from myListNode import *


# 方法 1：集合记录遍历过的节点，如果有环，入环的第一个节点就是(最好理解！)
class Solution2:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """返回链表开始入环的第一个节点。 如果链表无环，则返回 null"""
        vis = set()
        p = head
        while p:
            if p in vis:
                return p
            vis.add(p)
            p = p.next
        return None


# 方法 2：快慢指针（最高效！）
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """返回链表开始入环的第一个节点。 如果链表无环，则返回 null
        1.假设相遇时慢指针(每次1步)走的总步数为s，那么快指针(每次2步)走的总步数f为2s：
        f = 2s     (快指针步数f刚好是慢指针s的2倍)
        f = s + nb (快指针一定比慢指针多走了环长b的整数倍）
        推出：s = nb, 也就是相遇时，慢指针正好走了环长b的整数倍
        
        2.假设环起点到相遇点节点数为m:
        环起点到head节点数为s-m, 也就是nb-m
        相遇点再次走到相遇点的节点数为nb-m
        推出: 把快慢指针中的任一个重新指向 head，然后两个指针同速前进，nb - m 步后一定会相遇，相遇之处就是环的起点了
        """
        # 1.slow和fast初始位置都在head, 每次slow走1步，fast走2步，直到快慢指针相遇
        slow = head
        fast = head
        while True:
            # fast节点或者下一个节点为空，代表链表无环
            if not fast or not fast.next:
                return None
            
            slow = slow.next
            fast = fast.next.next
            
            # 快慢指针相遇，证明有环，跳出循环
            if slow is fast:
                break
            
        # 2.把快慢指针中的任一个重新指向 head，然后两个指针同速前进，相遇之处就是环的起点
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow
