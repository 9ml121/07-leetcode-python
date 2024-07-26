"""
给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.



示例 1：



输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
示例 2：



输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]


提示：

每棵树的节点数在 [0, 5000] 范围内
-105 <= Node.val <= 105
"""
from myTreeNode import *


# 方法 1：使用中序遍历分别获取2 个二叉搜索树的有序节点值序列，并将两个序列合并后排序，得到最终的升序结果。
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # 定义中序遍历函数
        def inorder(node, arr):
            if not node:
                return
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        # 中序遍历获取有序节点值序列
        arr1 = []
        arr2 = []
        inorder(root1, arr1)
        inorder(root2, arr2)

        # 合并两个有序序列并排序
        merged = sorted(arr1 + arr2)

        # 返回最终的升序结果数组
        return merged


# 方法 2：使用迭代中序遍历的代码实现(推荐)
# 使用迭代的方式进行中序遍历，并在遍历过程中将节点值添加到结果数组中。
# 这种方法可以在不使用额外空间的情况下得到有序的节点值序列，从而提高性能。
class Solution2:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []
        stack1, stack2 = [], []
        p1, p2 = root1, root2

        # 中序遍历的迭代实现
        while p1 or p2 or stack1 or stack2:
            # 先遍历 p1和p2左节点
            while p1:
                stack1.append(p1)
                p1 = p1.left
            while p2:
                stack2.append(p2)
                p2 = p2.left

            # 此时 p1, p2都为 None, 需要判断 stack1 和 stack2
            # 注意：这时候 stack1和 stack2 至少有 1 个不为None
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                p1 = stack1.pop()
                res.append(p1.val)
                p1 = p1.right
            else:
                p2 = stack2.pop()
                res.append(p2.val)
                p2 = p2.right

        return res
