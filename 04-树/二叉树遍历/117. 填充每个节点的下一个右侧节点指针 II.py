"""
给定一个二叉树：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL 。

初始状态下，所有 next 指针都被设置为 NULL 。



示例 1：
输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。

示例 2：
输入：root = []
输出：[]


提示：
树中的节点数在范围 [0, 6000] 内
-100 <= Node.val <= 100

进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序的隐式栈空间不计入额外空间复杂度。
"""
import collections


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 常规解法：bfs, 空间复杂度O(N)
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dq = collections.deque([root])
        while dq:
            sz = len(dq)
            pre = None
            for _ in range(sz):
                cur = dq.popleft()
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
                if pre:
                    pre.next = cur
                pre = cur

        return root


# bfs写法2
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        dq = collections.deque([root])
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                node = dq.popleft()
                if i < level_size - 1:
                    node.next = dq[0]
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root


# 空间复杂度O(1): 把每一层都当作一个链表，前后相连的节点构建 next指针。  推荐！！！
class Solution3:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur = root

        while cur:
            dummy = Node()  # 用作下一层的虚拟头节点
            head = dummy

            while cur:  # 遍历当前层的节点，同时将下一层节点通过 next指针串联起来
                if cur.left:
                    head.next = cur.left
                    head = head.next
                if cur.right:
                    head.next = cur.right
                    head = head.next
                cur = cur.next

            cur = dummy.next  # 移动到下一层的第一个节点
        return root
