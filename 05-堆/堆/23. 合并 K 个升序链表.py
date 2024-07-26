"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

示例 2：
输入：lists = []
输出：[]

示例 3：
输入：lists = [[]]
输出：[]


提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
"""

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 暴力解法：O(Nlog(N))
class Solution0:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 将所有链表的节点值存储在一个列表中
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        # 对节点值进行排序
        vals.sort()
        # 构建新的链表
        dummy = ListNode(0)
        tail = dummy
        for val in vals:
            tail.next = ListNode(val)
            tail = tail.next
        return dummy.next


"""
此题最佳方法：优先级队列解法
1.我们首先定义一个哨兵节点和一个指针，然后将每个链表的头节点放入堆中。
2，堆中的每个元素都是一个三元组  (value, i, node) ，其中  
    - value  表示节点的值， 
    - i  表示节点所在的链表在  lists  中的索引， 
    - node  表示节点本身。
    这个三元组相当于我们自定义了一个比较器cmp, 其中
    堆元素的比较规则如下： 
        1. 首先比较节点值  node.value ，节点值较小的元素排在前面。 
        2. 如果节点值相同，则比较节点在链表数组中的索引  i ，索引较小的元素排在前面。 
    这样定义比较器的目的是为了保证堆中元素的顺序满足从小到大排列，
    并且在节点值相同的情况下，按照链表在数组中的索引从小到大排列。
    这样可以保证在合并有序链表时，每次取出堆顶元素时都是取出当前所有链表中最小的元素。

3.我们使用  heapq.heappush  函数将每个链表的头节点加入堆中，同时保证堆中的元素按照节点的值从小到大排序。
4.接下来，我们循环取出堆顶元素，将其加入新链表中，并将其所在链表的下一个节点加入堆中。
这样，我们就可以逐个取出所有节点，最终构建出排好序的新链表。 
 
这种方法的时间复杂度为 $O(n\log k)$，其中 $n$ 表示所有链表中节点的总数，$k$ 表示链表的个数。
    只需要遍历每个节点一次，堆的大小最多为 $k$, 维护堆的有序性需要 logK次操作。
空间复杂度为 $O(k)$，即堆的大小。
"""


class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 将每个链表的头节点放入堆中(初始化堆)
        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, (lists[i].val, i, lists[i]))

        # 定义一个哨兵节点和一个指针
        dummy = ListNode(0)
        cur = dummy

        # 循环取出堆顶元素
        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            # 将堆顶元素加入新链表中
            cur.next = node
            cur = cur.next
            # 将堆顶元素所在链表的下一个节点加入堆中
            if node.next:
                heapq.heappush(minHeap, (node.next.value, i, node.next))
        return dummy.next


"""
# 优化1：可以使用  heapreplace  代替  heappop  和  heappush  操作。  
1.heapreplace  操作会先弹出堆顶元素，然后将新元素加入堆中，并保持堆的性质。
2.这样可以避免在弹出堆顶元素后再进行一次插入操作，从而提高代码的效率。
3.但需要注意的是，如果堆为空， heapreplace  操作会抛出  IndexError  异常，
    因此需要在使用  heapreplace  操作前先判断堆是否为空。

下面是使用  heapreplace  实现合并有序链表的代码示例：
"""


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 初始化堆
        minHeap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(minHeap)
        # 初始化哨兵节点
        dummy = ListNode(0)
        tail = dummy
        # 不断取出堆顶元素，并将其后继节点加入堆中
        while minHeap:
            # 先看一眼，并不取出
            _, i, node = minHeap[0]
            if not node.next:
                # 如果堆顶元素的后继节点为空，则直接弹出堆顶元素
                heapq.heappop(minHeap)
            else:
                # heapreplace会先弹出堆顶节点，然后将该节点下一个节点加入堆中，并保持堆的性质。
                # 如果堆顶元素的后继节点非空，则将其后继节点加入堆中
                heapq.heapreplace(minHeap, (node.next.value, i, node.next))
            tail.next = node
            tail = tail.next
        return dummy.next


"""
# 优化2：
可以使用  heapq  的  merge  方法来优化合并有序链表的代码。
heapq.merge  方法可以将多个有序序列合并成一个有序序列，而不需要构建一个堆。
 
下面是使用  heapq.merge  实现合并有序链表的代码示例：
"""


class Solution3:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 将所有链表的节点值存储在一个列表中
        vals = []
        for node in lists:
            tmp = []
            while node:
                tmp.append(node.val)
                node = node.next
            vals.append(tmp)

        # 构建新的链表
        dummy = ListNode(0)
        tail = dummy
        # 这里相当于vals.sort()
        for val in heapq.merge(*vals):
            tail.next = ListNode(val)
            tail = tail.next
        return dummy.next
