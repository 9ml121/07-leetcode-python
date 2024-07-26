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


# 中序遍历：先遍历左子树，再遍历根节点，最后遍历右子树
# dfs递归方法：
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """二叉树中序遍历: dfs实现"""

    def inorder(root):
        if not root:
            return

        inorder(root.left)
        # 中间位置：先左节点，再根节点，最后右节点
        ans.append(root.value)
        inorder(root.right)

    ans = []
    inorder(root)
    return ans


# stack迭代方法
def inorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    """二叉树中序遍历: stack实现"""
    stack = []  # stack用来搜集中序遍历的节点
    curNode = root  # node变量是为了不修改root参数的值
    res = []  # 搜集中序遍历的节点val
    while stack or curNode:
        # 1.当前指针 curNode 不断向左边移动，把遇到的结点都存进 栈 里，直到当前结点为空；
        while curNode:
            stack.append(curNode)
            curNode = curNode.left

        # 2.然后考虑出栈，出栈的元素依次是二叉树的中序遍历结点，
        curNode = stack.pop()
        res.append(curNode.val)

        # 3.左节点和根节点依次出栈之后，在将根节点的右节点入栈
        curNode = curNode.right
    return res


if __name__ == '__main__':
    # 给定二叉树 [1,2,3,4,5,6,7]，
    # 遍历顺序为: [4, 2, 5, 1, 6, 3, 7]
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = buildTree(arr)
    print(inorderTraversal2(root))
