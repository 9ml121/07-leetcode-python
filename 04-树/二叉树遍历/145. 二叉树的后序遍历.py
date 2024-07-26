"""
# 二叉树
        1
      /   \
     2      3
    / \    / \
   4   5  6   7
中序遍历
    先遍历左子树，再遍历根节点，最后遍历右子树
    遍历顺序为: [4, 2, 5, 1, 6, 3, 7]

后续遍历
    先遍历左子树，再遍历右子树，最后遍历根节点
    最后输出: [4, 5, 2, 6, 7, 3, 1]
"""

from myTreeNode import *


def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """二叉树后续遍历：
    1.遍历的思路，回溯算法的底层思想
    """
    ans = []

    def postorder(root) -> None:
        if not root:
            return

        postorder(root.left)
        postorder(root.right)
        # 后续位置：先左节点，再右节点，最后根节点
        ans.append(root.value)

    postorder(root)
    return ans


class Solution1:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """二叉树后续遍历：
        2.分解问题思路：动态规划的基本思想
        """
        res = []
        if not root:
            return res
        # 后序遍历结果特点：先是左子树，接着是右子树，最后是根节点的值
        res += self.postorderTraversal(root.left)
        res += self.postorderTraversal(root.right)
        res.append(root.val)
        return res


def postorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    """二叉树后续遍历：stack实现"""
    stack = []
    node = root
    rightNode = None  # todo 为了避免重复遍历右子树，使用了一个变量rightNode来记录已经遍历过的最近一个右节点
    res = []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        # res先记录左节点，在记录右节点，最后记录他们的根节点val
        node = stack[-1]
        # todo 取出栈顶元素node，判断其右子树是否存在并且有没有遍历过。
        # 如果右子树存在且未遍历过，则将指针node指向右子树；否则，将node出栈，并将其val值加入结果列表res中。
        if node.right and node.right != rightNode:
            node = node.right
        else:
            node = stack.pop()
            res.append(node.val)
            rightNode = node
            node = None
    return res


from typing import List


class Solution:
    class Action:
        # 如果当前结点有孩子结点（左右孩子结点至少存在一个），执行 GO
        GO = 0
        # 添加到结果集（真正输出这个结点）
        ADDTORESULT = 1

    class Command:
        def __init__(self, action: int, node: TreeNode):
            # 将动作类与结点类封装起来
            self.action = action
            self.node = node

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [self.Command(self.Action.GO, root)]
        while stack:
            command = stack.pop()
            if command.action == self.Action.ADDTORESULT:
                res.append(command.node.val)
            else:
                assert command.action == self.Action.GO
                # 特别注意：以下的顺序与递归执行的顺序反着来，即：倒过来写的结果
                # 后序遍历：左子树、右子树、根结点
                # 添加到栈的顺序：根结点、右子树、左子树
                stack.append(self.Command(self.Action.ADDTORESULT, command.node))
                if command.node.right:
                    stack.append(self.Command(self.Action.GO, command.node.right))
                if command.node.left:
                    stack.append(self.Command(self.Action.GO, command.node.left))
        return res


if __name__ == '__main__':
    # 给定二叉树 [1,2,3,4,5,6,7]，
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = insert(arr)
    postorderTraversal2(root)
