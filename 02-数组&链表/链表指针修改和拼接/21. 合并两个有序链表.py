"""
两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

示例 2：
输入：l1 = [], l2 = []
输出：[]

示例 3：
输入：l1 = [], l2 = [0]
输出：[0]


提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.value <= 100
l1 和 l2 均按 非递减顺序 排列
"""

from typing import Optional
from myListNode import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val) + '->' + str(self.next)



# todo 方法 1：迭代解法(推荐)
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """合并两个有序链表: 迭代解法(容易理解)"""
        # 创建一个包含虚拟头节点val的链表,最后返回它的next节点对象
        dummy = ListNode(-1)
        
        # 创建3个临时指针，分别代表dummy，l1和l2的当前节点对象
        cur = dummy
        p1 = l1
        p2 = l2

        # 比较 p1 和 p2 两个指针, 将值较小的的节点接到 cur 指针
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
    
            cur = cur.next  

        cur.next = p1 if p1 else p2  # 拼接上p1或者p2剩余节点

        return dummy.next



# 方法 2：递归解法
class Solution2:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """合并两个有序链表: 递归解法
        递归解法是将两个链表的头节点进行比较，将较小的头节点与剩余链表的合并结果进行合并，直到其中一个链表为空，返回另一个链表即可。
        """
        if not l1 or not l2:
            return l1 if l1 else l2
       
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2



# 方法 3. 堆解法： 
# 时间复杂度为 $O(Nlog2)$，其中 $n$ 表示两个链表中节点的总数。
# 空间复杂度为 $O(2)$，即堆的大小。


class Solution3:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """合并两个有序链表: 堆解法（不推荐）"""
        import heapq
        # 定义一个哨兵节点和一个指针，用于构建新链表
        dummy = ListNode(0)
        cur = dummy
        
        # 先将两个链表的头节点放入小根堆
        # todo 堆中的元素是一个三元组  (value, i, node),分别表示节点值，节点所在链表在堆中索引，节点
        # 堆中永远只有2个元素
        min_heap = []
        if l1:
            heapq.heappush(min_heap, (l1.val, 0, l1))
        if l2:
            heapq.heappush(min_heap, (l2.val, 1, l2))
        
        # 循环取出堆顶元素，将节点加入新链表中，并将其所在链表的下一个节点加入堆中。
        while min_heap:
            _, i, node = heapq.heappop(min_heap)
            # 将堆顶节点加入新链表中
            cur.next = node
            cur = cur.next
            # 将堆顶节点所在链表的下一个节点加入堆中
            if node.next:
                heapq.heappush(min_heap, (node.next.value, i, node.next))
        
        # 返回哨兵节点的下一个节点，即合并后的新链表的头节点。
        return dummy.next


# 暴力解法：把结点的值记录到 动态数组，在对动态数组排序，最后生成新链表。
# 这个思路没有利用「每个链表均有序」这个条件，并且使用了新的空间来保存链表的元素。而链表的问题，绝大多数要求我们 改变结点的指针指向 以完成相关任务。
# 这种方法的时间复杂度为 O(nlogn)，空间复杂度为 O(n)。
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 将两个链表的节点放入一个列表中
        nodes = []
        while l1:
            nodes.append(l1)
            l1 = l1.next
        while l2:
            nodes.append(l2)
            l2 = l2.next
            
        # 对节点列表进行排序
        nodes = sorted(nodes, key=lambda x: x.value)
        # 构建新的链表
        dummy = ListNode(0)
        cur = dummy
        for node in nodes:
            cur.next = node
            cur = cur.next
        return dummy.next

if __name__ == '__main__':
    # l1 = [1, 2, 4]
    # l2 = [1, 3, 4]
    # node1 = myListNode.ListNode.fromList(l1)
    # node2 = myListNode.ListNode.fromList(l2)
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    node = Solution().mergeTwoLists(l1, l2)

    print(node)
