from typing import Optional

from myTreeNode2 import TreeNode


class MyBst:
    def __init__(self, root: TreeNode):
        self.root = root

        # 统计以每个结点为根结点的子树的结点数，并存储在哈希表中
        self._node_num = {}
        self._count_node_num(root)

    def kth_smallest(self, k: int):
        """返回二叉搜索树中第k小的元素"""
        node = self.root
        while node:
            left = self._get_node_num(node.left)
            if left < k - 1:
                node = node.right
                k -= left + 1
            elif left == k - 1:
                return node.val
            else:
                node = node.left

    def _count_node_num(self, node) -> int:
        """统计以node为根结点的子树的结点数"""
        if not node:
            return 0
        self._node_num[node] = 1 + self._count_node_num(node.left) + self._count_node_num(node.right)
        return self._node_num[node]

    def _get_node_num(self, node) -> int:
        """获取以node为根结点的子树的结点数"""
        return self._node_num.get(node, 0)

    def getMaxNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """查找二叉搜索树值最大的节点，并返回(迭代写法)"""
        while node.right:
            node = node.right
        return node

    def getMinNode(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """查找二叉搜索树值最小的节点，并返回(迭代写法)"""
        while node.left:
            node = node.left
        return node



