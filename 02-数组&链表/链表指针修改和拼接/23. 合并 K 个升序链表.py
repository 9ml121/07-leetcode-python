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


# 暴力解法：把所有结点的值记录到 动态数组，在对动态数组排序，最后生成新链表。
"""
复杂度分析：
时间复杂度：O(NlogN)，这里 K 个链表的结点总数。
    遍历的时间复杂度是 O(N)，
    排序的时间复杂度是 O(NlogN)，
    将动态数组转换为链表的时间复杂度是 O(N)，
    综上所述，整体时间复杂度为 O(NlogN)；
空间复杂度：O(N)，使用动态数组的长度为 N，生成新的链表，又需要 N 个空间。
"""


class Solution1:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
        p = dummy
        for val in vals:
            p.next = ListNode(val)
            p = p.next
        return dummy.next


# 方法二：两两合并有序链表
"""
两个有序数组合并的做法是先把元素拷贝出来，再拷贝回去。
而两个有序链表的合并，由于链表是动态的数据结构，可以很方便地更改结点指针的指向，可以通过 循环 和 递归 两种方式完成合并。
于是我们可以两两合并这些有序链表

复杂度分析：
时间复杂度：O(K^2*N)，这里 N 表示这 K 个有序链表里最长的链表的长度，复杂度分析有一些繁琐，初学的时候可以暂时跳过。
空间复杂度：O(1)，非递归的方式合并两个有序链表，使用的临时变量的个数为常数个。
"""


class Solution2:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        ans = lists[0]
        for i in range(1, n):
            if lists[i]:
                ans = self.mergeTwoSortLists(ans, lists[i])
        return ans

    def mergeTwoSortLists(self, node1: 'ListNode', node2: 'ListNode') -> 'ListNode':
        """合并2个有序链表"""
        dummy = ListNode(0)
        p = dummy
        while node1 and node2:
            if node1.val <= node2.val:
                p.next = node1
                node1 = node1.next
            else:
                p.next = node2
                node2 = node2.next
            p = p.next

        p.next = node1 if node1 else node2
        return dummy.next


# 方法三：分而治之:递归
"""
事实上，合并这 K 个链表的任务还可以分而治之去完成。这样可以充分利用已经的结果，使得时间复杂度降低。请大家仔细思考以下细节：

分治思想的中间过程是存放在方法栈中的，整体执行时间比「方法二」快，体现了 空间换时间 的思想；
由于方法栈「暂时存储」了两个链表合并的结果，整体参与比较的次数更少了。这一点可以类比于「选择排序」和「归并排序」的时间复杂度的差别。

复杂度分析：
时间复杂度：O(K * N * logK)， 这里 N 表示这 K 个有序链表里最长的链表的长度，
    根据方法二的时间复杂度分析，每一次合并都会使得合并的总的操作数加倍，而递归树的高度为 ⌈logK⌉ ，
    故总的时间复杂度为 O(KNlogK)；
空间复杂度：O(logK)，递归树的高度为 ⌈logK⌉，即需要使用 ⌈logK⌉ 空间的代价
"""


class Solution3:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sz = len(lists)
        if sz == 0:
            return None
        return self.mergeKListsHelper(lists, 0, sz - 1)

    def mergeKListsHelper(self, lists: list, left: int, right: int) -> Optional[ListNode]:
        """递归合并左右2个链表"""
        if left == right:
            return lists[left]

        mid = (left + right) // 2
        leftNode = self.mergeKListsHelper(lists, left, mid)
        rightNode = self.mergeKListsHelper(lists, mid + 1, right)

        return self.mergeTwoSortLists(leftNode, rightNode)

    def mergeTwoSortLists(self, node1: 'ListNode', node2: 'ListNode') -> 'ListNode':
        """合并2个有序链表"""
        dummy = ListNode(0)
        p = dummy
        while node1 and node2:
            if node1.val <= node2.val:
                p.next = node1
                node1 = node1.next
            else:
                p.next = node2
                node2 = node2.next
            p = p.next

        p.next = node1 if node1 else node2
        return dummy.next


# 优先队列解法
"""
事实上，将「合并两个有序链表」推广开来， K 个有序链表合并的思路也不难得到。

1.每个链表头结点的元素的值很重要，只需要每一次选取 K 个链表头结点中值最小的那个结点，将它归并回去即可；
2.选取 K 个链表头结点中值最小的那个结点，就需要使用「优先队列」，每一次选出头结点中数组最小的结点以后，
    这个结点的下一个结点（如果有的话），就成为当前链表的新的头结点，参与优先队列的值的比较，
3.这显然是一个 动态选取最值 的过程，再一次说明「优先队列」是完成 K 个链表合并的最合适的数据结构；
4.由于链表是动态数组结构，可以直接在这 K 个链表上进行操作。

复杂度分析：

时间复杂度：O(NlogK)，
    这里 N 表示所有链表的结点总数（注意这里 N 的含义与方法二、方法三不一样，与方法一一样），
    每一个链表结点都会在优先队列里进出一次，维护优先队列的时间复杂度为 O(logK)；
空间复杂度：O(K)，优先队列的大小为 K，故空间复杂度为 O(K)。
"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 定义一个哨兵节点和一个指针
        dummy = ListNode(0)
        cur = dummy

        # 将每个链表的头节点放入堆中
        minHeap = []
        for i, node in enumerate(lists):
            if node:
                # todo 注意：这里必须要把i也推入到堆，因为node.val可能相同，只是推(node.val, node)会报错：node无法比较
                heapq.heappush(minHeap, (node.val, i, node))

        # 循环取出堆顶元素
        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            # 将堆顶元素加入新链表中
            cur.next = node
            cur = cur.next
            # 将堆顶元素所在链表的下一个节点加入堆中
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        return dummy.next


"""
方法 1：优先级队列解法：
1.我们首先定义一个哨兵节点和一个指针，然后将每个链表的头节点放入堆中。
2，堆中的每个元素都是一个三元组  (value, i, node) ，其中
    value  表示节点的值，
    i  表示节点所在的链表在  lists  中的索引，
    node  表示节点本身。
3.我们使用  heapq.heap元push  函数将每个链表的头节点加入堆中，同时保证堆中的元素按照节点的值从小到大排序。
4.接下来，我们循环取出堆顶素，将其加入新链表中，并将其所在链表的下一个节点加入堆中。
这样，我们就可以逐个取出所有节点，最终构建出排好序的新链表。

这种方法的时间复杂度为 $O(n\log k)$，其中 $n$ 表示所有链表中节点的总数，$k$ 表示链表的个数。
空间复杂度为 $O(k)$，即堆的大小。
"""