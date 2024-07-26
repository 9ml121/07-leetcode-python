"""
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，
或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。
对序列化/反序列化算法的工作方式没有限制。
您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。


示例 1：
输入：root = [2,1,3]
输出：[2,1,3]

示例 2：
输入：root = []
输出：[]


提示：
树中节点数范围是 [0, 104]
0 <= Node.val <= 104
题目数据 保证 输入的树是一棵二叉搜索树。
"""
from myTreeNode import *


# 方法 1：前序遍历
class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []

        # 前序遍历
        def dfs(root) -> None:
            if not root:
                res.append('*')  # 空节点用*表示
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)  # 2,1,3,*,*,*,*

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        dq = collections.deque(data.split(','))

        def dfs(dq: collections.deque):
            if not dq:
                return

            # 构建根节点
            rootVal = dq.popleft()
            if rootVal == '*':
                return None
            root = TreeNode(int(rootVal))

            # 构建左右子树(顺序不能颠倒)
            root.left = dfs(dq)
            root.right = dfs(dq)

            return root

        return dfs(dq)
