"""
给你一个二叉搜索树的根节点 root ，返回 树中任意两不同节点值之间的最小差值 。
差值是一个正数，其数值等于两值之差的绝对值。

示例 1：
        4
       / \
      2   6
     / \
    1  3

输入：root = [4,2,6,1,3]
输出：1
示例 2：


输入：root = [1,0,48,null,null,12,49]
输出：1


提示：

树中节点的数目范围是 [2, 104]
0 <= Node.value <= 105


注意：本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同
"""
from myTreeNode2 import *


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """返回二叉搜索树任意两不同节点值之间的最小差值
         写法1：中序遍历迭代写法
        """
        stack = []  # 用来存储中序遍历节点
        node = root  # 不修改原参数root
        preNode = None  # 记录前一个节点
        res = float('inf')  # 保存两节点最小差值
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if preNode:
                res = min(res, node.val - preNode.val)
            preNode = node

            node = node.right

        return res

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        # 初始化最小差值和前一个节点。
        res = float('inf')
        preNode = None

        # 定义中序遍历函数以遍历二叉树。
        def inorder(root):
            nonlocal res, preNode
            if not root:
                return
            inorder(root.left)
            if preNode is not None:
                res = min(res, abs(root.value - preNode.val))
            preNode = root
            inorder(root.right)

        # 调用中序遍历函数以获取最小差值。
        inorder(root)
        return res


if __name__ == '__main__':
    # root = [4, 2, 6, 1, 3]
    root = [1, 0, 48, None, None, 12, 49]
    node = create(root)
    print(Solution().getMinimumDifference(node))
