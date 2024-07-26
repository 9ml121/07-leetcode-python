"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
          1
        /  \
      2     3
     / \   / \
    4  5  6   7
输入:[1,2,3,4,5,6,7]
输出: [1,2,4,5,3,6,7]

示例 1：
输入：root = [1,null,2,3]
输出：[1,2,3]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]

示例 5：
输入：root = [1,null,2]
输出：[1,2]


提示：
树中节点数目在范围 [0, 100] 内
-100 <= Node.value <= 100

进阶：递归算法很简单，你可以通过迭代算法完成吗？
"""
from myTreeNode import *


# 方法1：dfs递归
# 时间复杂度：O(n)，其中 n 是二叉树的节点数。每一个节点恰好被遍历一次。
# 空间复杂度：O(h)，h代表树的深度，为递归过程中栈的开销，平均情况下为 O(log(n+1))，最坏情况下树呈现链状，为 O(n)。
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    ans = []

    def preorder(root):
        if not root:
            return
        # 前序位置：先根节点，再左子树，最后右子树
        ans.append(root.value)

        preorder(root.left)
        preorder(root.right)

    preorder(root)
    return ans


# 方法2：stack迭代
# 本质上是在模拟递归，因为在递归的过程中使用了系统栈，所以在迭代的解法中常用 Stack 来模拟系统栈。
def preorderTraversal2(root: Optional[TreeNode]) -> List[int]:
    """二叉树前序遍历: stack实现"""
    stack = []
    node = root
    res = []
    while stack or node:  # 迭代终止条件：stack和node列表都为空
        while node:
            res.append(node.val)
            # 压栈的顺序是：根节点->右子树->左子树
            stack.append(node)
            node = node.left

        node = stack.pop()
        # 出栈的顺序是：根节点->左子树->右子树
        node = node.right

    return res


class Solution:
    class Action:
        GO = 1
        ADDTORESULT = 2

    class Command:
        def __init__(self, action, node):
            self.action = action
            self.node = node

        def __repr__(self):
            return f"Command({self.action}, {self.node})"

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [self.Command(self.Action.GO, root)]
        while stack:
            command = stack.pop()
            if command.action == self.Action.ADDTORESULT:
                res.append(command.node.value)
            else:
                # 特别注意：以下的顺序与递归执行的顺序反着来，即：倒过来写的结果
                # 前序遍历：根结点、左子树、右子树、
                # 添加到栈的顺序：右子树、左子树、根结点
                if command.node.right:
                    stack.append(self.Command(self.Action.GO, command.node.right))
                if command.node.left:
                    stack.append(self.Command(self.Action.GO, command.node.left))
                stack.append(self.Command(self.Action.ADDTORESULT, command.node))
        return res


if __name__ == '__main__':
    # 给定二叉树 [1,2,3,4,5,6,7]，
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = buildTree(arr)
    sol = Solution()
    print(sol.preorderTraversal(root))
    # print(preorderTraversal(root))


# 方法3：Morris 遍历(有点复杂，没看懂！！！)
# 有一种巧妙的方法可以在线性时间内，只占用常数空间来实现前序遍历
# Morris 遍历的核心思想是利用树的大量空闲指针，实现空间开销的极限缩减
'''
复杂度分析
时间复杂度：O(n)，其中 n 是二叉树的节点数。没有左子树的节点只被访问一次，有左子树的节点被访问两次。
空间复杂度：O(1)。只操作已经存在的指针（树的空闲指针），因此只需要常数的额外空间。
'''


def preorderTraversal3(root: TreeNode) -> List[int]:
    res = list()
    if not root:
        return res

    p1 = root  # p1指针初始化指向头节点
    while p1:
        p2 = p1.left
        if p2:
            # 2.如果p1左节点不为空，并且p1左节点的右节点也不为空，并且p1左节点的右节点不为p1, 就让p1的左节点一直指向这个分支的最右边节点
            while p2.right and p2.right != p1:
                p2 = p2.right

            # 3.如果p1左节点不为空，但是p1左节点的右节点为空，res添加p1当前节点
            # 并将p1左节点的右节点(空节点)改为p1当前节点，p1当前节点改为p1的左节点
            if not p2.right:
                res.append(p1.val)
                p2.right = p1
                p1 = p1.left
                continue
            else:
                p2.right = None
        else:
            # 1.如果p1的左节点为空，res添加p1当前节点val
            res.append(p1.val)
        p1 = p1.right

    return res
