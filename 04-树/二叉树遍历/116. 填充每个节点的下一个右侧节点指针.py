"""
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int value;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

示例 1：
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。
序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

示例 2:
输入：root = []
输出：[]

提示：
树中节点的数量在 [0, 2^12 - 1] 范围内
-1000 <= node.value <= 1000

进阶：
你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
"""
import collections
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 方法1: 迭代,按照BFS思路，迭代访问每一层
# 空间复杂度：O(N)
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """填充每个节点的下一个右侧节点指针"""
        if not root:
            return None

        # 层序遍历BFS
        dq = collections.deque([root])

        # 从上往下，从左往右遍历整棵树
        while dq:
            size = len(dq)
            pre = None
            for _ in range(size):
                cur = dq.popleft()
                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)

                if pre:
                    pre.next = cur
                pre = cur
        return root


# 方法2：推荐！！！
# 递归：传统的 dfs 函数是遍历二叉树的所有节点，但现在我们想遍历的其实是两个相邻节点之间的「空隙」。
class Solution2:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # 三叉树遍历框架
        # 函数定义：参数node1和node2代表三叉数左右相邻的2个节点, 无返回值。
        # 函数作用：将传入的两个节点穿起来
        def dfs(node1: Optional[Node], node2: Optional[Node]) -> None:
            if not node1 or not node2:
                return

            # 前序位置，将传入的两个节点穿起来
            node1.next = node2

            # 连接相同父节点的两个子节点
            dfs(node1.left, node1.right)
            dfs(node2.left, node2.right)
            # 连接跨越父节点的两个子节点
            dfs(node1.right, node2.left)

        # 填充每个节点的下一个右侧节点指针
        if not root:
            return None

        dfs(root.left, root.right)  # 遍历「三叉树」，连接相邻节点
        return root
