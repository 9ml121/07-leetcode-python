"""
给你一棵二叉树的根节点 root ，返回树的 最大宽度 。

树的 最大宽度 是所有层中最大的 宽度 。

每一层的 宽度 被定义为该层最左和最右的非空节点（即，两个端点）之间的长度。
将这个二叉树视作与满二叉树结构相同，两端点间会出现一些延伸到这一层的 null 节点，这些 null 节点也计入长度。

题目数据保证答案将会在  32 位 带符号整数范围内。



示例 1：
输入：root = [1,3,2,5,3,null,9]
输出：4
解释：最大宽度出现在树的第 3 层，宽度为 4 (5,3,null,9) 。

示例 2：
输入：root = [1,3,2,5,null,null,9,6,null,7]
输出：7
解释：最大宽度出现在树的第 4 层，宽度为 7 (6,null,null,null,null,null,7) 。

示例 3：
输入：root = [1,3,2,5]
输出：2
解释：最大宽度出现在树的第 2 层，宽度为 2 (3,2) 。


提示：

树中节点的数目范围是 [1, 3000]
-100 <= Node.value <= 100
"""
import collections
from typing import Optional

from myTreeNode import TreeNode

'''
要求二叉树的最大宽度，可以使用层序遍历的方式来解决。
在遍历过程中，记录每层的最左和最右节点的位置，并计算宽度，最后找到最大的宽度。
'''


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 1
        # (节点，节点在满二叉树中的位置)
        dq = collections.deque([(root, 1)])
        while dq:
            level_size = len(dq)
            _, left_pos = dq[0]
            _, right_pos = dq[-1]
            max_width = max(max_width, right_pos - left_pos + 1)

            for _ in range(level_size):
                node, pos = dq.popleft()
                if node.left:
                    # 左子节点在满二叉树中的位置为父节点位置的两倍
                    dq.append((node.left, pos * 2))
                if node.right:
                    # 右子节点在满二叉树中的位置为父节点位置的两倍加一
                    dq.append((node.right, pos * 2 + 1))

        return max_width


if __name__ == '__main__':
    # 示例使用
    # 构建一个二叉树
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)

    # 计算最大宽度
    width = Solution().widthOfBinaryTree(root)
    print(width)  # 输出: 4
