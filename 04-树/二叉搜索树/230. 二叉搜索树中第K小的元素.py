"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

示例 1：
        3
       / \
      1  4
      \
       2
输入：root = [3,1,4,null,2], k = 1
输出：1

示例 2：
        5
       / \
      3   6
     / \
    2  4
   /
  1
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3


提示：
树中的节点数为 n 。
1 <= k <= n <= 10^4
0 <= Node.value <= 10^4

进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
"""

from myTreeNode import *


# todo 二叉搜索树中序遍历应用
# 方法 1：BST 的中序遍历结果是有序的（升序），所以用一个外部变量记录中序遍历结果第 k 个元素即是第 k 小的元素。
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """查找二叉搜索树中第K小的元素, 返回元素 value"""
        res = 0  # 二叉搜索树中第k个元素的val
        rank = 0  # 二叉搜索树中元素正序位置

        def inOrder(root, k) -> None:
            if not root:
                return

            inOrder(root.left, k)

            # 中序位置
            nonlocal rank, res
            rank += 1
            if rank == k:
                res = root.value  # 找到第 k 小的元素, 立刻返回，不再执行后面遍历右节点逻辑
                return

            inOrder(root.right, k)

        inOrder(root, k)
        return res


# 方法 2：模拟栈，在中序遍历到第 k 大结点的时候程序终止
class Solution2:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []  # 单调递减栈,存储中序遍历的节点

        # 1.当前指针 currentNode 不断向左边移动，把遇到的结点都存进 栈 里，直到当前结点为空；
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            # 2.然后考虑出栈，出栈的元素依次是二叉树的中序遍历结点
            minNode = stack.pop()
            # print(minNode.value)

            # 4.第 k 个元素就是我们要找的目标元素
            k -= 1
            if k == 0:
                return minNode.val

            # 3.然后把当前指针 currentNode 指向出栈结点的右孩子结点，继续上面的过程，直到 k 个元素出栈
            root = minNode.right


if __name__ == '__main__':
    # src = [3, 1, 4, None, 2]  # 1
    # src = [4, 2, 5, None, 3]
    src = [5, 3, 6, 2, 4, None, None, 1]
    root = buildTree(src)
    k = 6
    print(Solution().kthSmallest(root, k))
