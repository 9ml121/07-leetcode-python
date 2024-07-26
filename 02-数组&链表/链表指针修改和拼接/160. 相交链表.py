"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。
图示两个链表在节点 c1 开始相交：

题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。

自定义评测：
评测系统 的输入如下（你设计的程序 不适用 此输入）：
intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
listA - 第一个链表
listB - 第二个链表
skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。
如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。



示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。
换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。


示例 2：
输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。


提示：
listA 中节点数目为 m
listB 中节点数目为 n
1 <= m, n <= 3 * 104
1 <= Node.value <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]


进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？
"""
from myListNode import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.value = x
#         self.next = None

"""
A = [a1,a2,c1,c2]
B = [b1,b2,b3,c1,c2]
如果用两个指针 p1 和 p2 分别在两条链表上前进，并不能同时走到公共节点，也就无法得到相交节点 c1。
解决这个问题的关键是，通过某些方式，让 p1 和 p2 能够同时到达相交节点 c1。

所以，我们可以让 p1 遍历完链表 A 之后开始遍历链表 B，让 p2 遍历完链表 B 之后开始遍历链表 A，
这样相当于「逻辑上」两条链表接在了一起。
如果这样进行拼接，就可以让 p1 和 p2 同时进入公共部分，也就是同时到达相交节点 c1：
a1 -> a2 -> c1 -> c2 -> b1 -> b2 -> b3 -> c1
b1 -> b2 -> b3 -> c1 -> c2 -> a1 -> a2 -> c1
"""


# todo 方法 1：双指针（推荐！）
# 对两个链表分别拼接另外一个链表，让长度保持一致，然后双指针判断相交点
# headA  1->2->3->4->5->n->1->4 （两个链表相交点是节点4）
# headB  1->4->5->n->1->2->3->4
# 证明 a, b 指针相遇的点一定是相交的起始节点?
# 1.将两条链表分别按相交点截断，链表 A 节点数为: A + C，链表 B 节点数为: B + C
# 2.当 a 指针将链表 A 遍历完后, 重定位到链表 B 的头结点, 然后继续遍历直至相交点(a 指针遍历的距离为 A + C + B)
# 3.同理 b 指针遍历的距离为 B + C + A
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。"""
        # 两个指针分别指向 A, B 这两条链表, 两个指针相同的速度向后移动
        a, b = headA, headB
        while a != b:
            # 让 pA 遍历完链表 A 之后开始遍历链表 B，让 pB 遍历完链表 B 之后开始遍历链表 A
            a = a.next if a else headB
            b = b.next if b else headA
            
        # todo 如果两个链表相交，最后pa和pb会相遇，跳出循环。(思考为什么？)
        # 如果不相交, 最后 pA=pB=None， 也会跳出循环
        return a


#  方法 2：哈希法
# 用 set集合先保存 headA遍历过的结点,然后遍历 headB, 如果 2 者相交，headB的子节点会在 set出现
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。"""
        vis = set()
        pA, pB = headA, headB
        while pA:
            vis.add(pA)
            pA = pA.next
            
        while pB:
            # 如果 pB 在 set 中出现过，说明两者相交
            if pB in vis:
                return pB
            pB = pB.next
            
        # 如果没有相交节点，返回 None
        return None


# 方法 3：双指针的另外一个思路
# 1.先计算两个链表的长度，
# 2.然后让长度更长的链表先移动一定的步数，使得两个链表到达尾部的距离相同，
# 3.然后同步移动两个链表的指针，直到找到相交的节点。
class Solution3:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。"""

        def getLength(node: ListNode) -> int:
            """计算链表node节点个数"""
            p = node
            ans = 0
            while p:
                ans += 1
                p = p.next
            return ans

        lenA = getLength(headA)
        lenB = getLength(headB)
        # 让 pA 和 pB 到达尾部的距离相同
        pA, pB = headA, headB
        # 长度更长的节点，前面超出的部分不可能是相交点
        if lenA > lenB:
            for _ in range(lenA - lenB):
                pA = pA.next
        else:
            for _ in range(lenB - lenA):
                pB = pB.next
                
        # 同步移动 2 个节点指针
        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA
