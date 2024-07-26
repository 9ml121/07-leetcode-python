"""
给定一个长度为 n 的链表 head

对于列表中的每个节点，查找下一个 更大节点 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 严格大于 它的值。

返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值。
如果第 i 个节点没有下一个更大的节点，设置 answer[i] = 0 。



示例 1：
输入：head = [2,1,5]
输出：[5,5,0]

示例 2：
输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]


提示：
链表中节点数为 n
1 <= n <= 10^4
1 <= Node.value <= 10^9
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode(value={self.val}, next={self.next})"


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # 返回一个整数数组 answer ，其中 answer[i] 是第 i 个节点( 从1开始 )的下一个更大的节点的值
        vals = []
        p = head
        while p:
            vals.append(p.val)
            p = p.next

        sz = len(vals)
        ans = [0] * sz
        stack = [0]  # 逆序遍历，单调递减栈, 保存 value, 0是哨兵节点
        # 为什么要单调递减：因为 stack中的元素都是尚未找到更大节点的
        for i in range(sz - 1, -1, -1):
            curVal = vals[i]
            #
            while stack[-1] != 0 and stack[-1] <= curVal:
                stack.pop()
            #
            ans[i] = stack[-1]
            stack.append(curVal)

        return ans


# 代码优化 1
"""
这道题的时间复杂度最优解是 O(n)，可以使用单调栈来实现。

1.具体来说，可以使用一个单调递减的栈来维护尚未找到下一个更大节点的节点，(注意：这里stack要保存节点索引)
2.每次遍历到一个新节点时，将栈中所有小于该节点的节点弹出栈，并将这些节点的下一个更大节点设置为当前节点。
3.最后，栈中剩余的节点的下一个更大节点都为0。 (因为栈本身为单调递减)
"""


class Solution2:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        vals = []
        p = head
        while p:
            vals.append(p.val)
            p = p.next

        sz = len(vals)
        ans = [0] * sz
        stack = []  # 单调递减栈，保存节点的索引
        for i in range(sz):
            while stack and vals[stack[-1]] < vals[i]:
                ans[stack.pop()] = vals[i]
            stack.append(i)
        return ans


# 代码优化 2
"""
可以在链表节点遍历的过程中搜集答案，只需要在遍历链表的同时使用单调栈来维护尚未找到下一个更大节点的节点即可。

1.具体来说，我们可以使用一个单调递减的栈来维护尚未找到下一个更大节点的节点，
2.每次遍历到一个新节点时，将栈中所有小于该节点的节点弹出栈，并将这些节点的下一个更大节点设置为当前节点。
3.同时，我们还需要使用一个变量来记录当前遍历到的节点的索引，以便在遍历完成后将剩余节点的下一个更大节点设置为0。
4.最后，我们将搜集到的答案存储在一个列表中并返回即可。 
以下是在链表节点遍历的过程中搜集答案的代码示例：

- 这段代码的核心思想是维护一个单调递减的栈，栈中保存的是节点的索引，
- 栈顶元素对应的节点的值是栈中所有元素所对应的节点的值中最小的一个。
- 当遍历到一个新的节点时，如果该节点的值比栈顶元素所对应的节点的值要大，则将栈顶元素所对应的节点的值更新为当前节点的值，并弹出栈顶元素，
- 直到栈为空或者栈顶元素所对应的节点的值大于等于当前节点的值。
- 这样，当遍历完整个链表后，ans 列表中保存的就是每个节点后面第一个比它大的节点的值。
- 如果栈中还有元素，说明这些元素后面没有更大的节点，将它们对应的 ans 列表中的值更新为 0。

这个算法的时间复杂度为 O(n)，空间复杂度为 O(n)，并且只需要遍历一次链表，因此比使用两次遍历的解法更加高效。
"""


class Solution3:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        ans = []
        stack = []  # 单调栈（节点值，节点下标）
        while head:
            while stack and stack[-1][0] < head.val:
                ans[stack.pop()[1]] = head.val  # 用当前节点值更新答案
            stack.append((head.val, len(ans)))  # 当前 ans 的长度就是当前节点的下标
            ans.append(0)  # 占位
            head = head.next
        return ans


class Solution4:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans = []
        stack = []  # 单调递减栈，保存节点的索引
        i = 0  # 当前遍历到的节点的索引
        while head:
            while stack and ans[stack[-1]] < head.val:
                ans[stack.pop()] = head.val
            ans.append(head.val)
            stack.append(i)
            i += 1
            head = head.next
        while stack:
            ans[stack.pop()] = 0  # 没有下一个更大元素
        return ans


if __name__ == '__main__':
    solution = Solution3()
    head = ListNode(2, ListNode(7, ListNode(4, ListNode(3, ListNode(5)))))
    assert [7, 0, 5, 5, 0] == solution.nextLargerNodes(head)
