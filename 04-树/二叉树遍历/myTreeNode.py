"""
列表转化为二叉树
已知列表nums，将其转化为二叉树。举例：
nums = [3,9,20,None,None,15,7]，转化为二叉树后:

节点3的左子节点9，右子节点20，9的左右子节点都为None，20的左子节点15，右子节点7，参考下面：
        3
       / \
      9   20
          / \
         15  7

nums = [1,2,3,4,None,5,6,None,None,None, 7]
        1
      /   \
     2     3
    /     / \
   4     5   6
          \
           7

todo LeetCode 序列化二叉树的格式
https://support.leetcode.cn/hc/kb/article/1567641/

1.输入标准格式为 [] 或 [值1,值2,值3,值4,值5,……]。
 - 若只输入[]则代表输入的测试用例是一棵空二叉树。
 - 若按[值1,值2,值3,值4,值5,……]格式输入，则“值 1”代表的是这棵二叉树的根节点，
    且从“值 1”开始一直到最后的数，依次是 水平顺序 遍历二叉树的各个节点的值，
 - 函数入参是已经构建完成的二叉树的根节点。

2. 若二叉树 非空节点 的某个子节点为空，则用None 表示
特殊层序遍历会遍历有值节点的 None 子节点，末尾连续输入的若干空节点会被去除。
"""
import collections
import unittest
from typing import List, Optional


# 二叉树对象
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


# 1.将数组列表反序列化为TreeNode对象
def buildTree(values: List[int]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    dq = collections.deque([root])

    idx = 1  # idx变量记录正在序列化的节点在数组中的位置
    while idx < len(values):
        node = dq.popleft()
        # 1.为父节点构造左侧子节点
        leftVal = values[idx]
        if leftVal is not None:
            node.left = TreeNode(leftVal)
            dq.append(node.left)
        idx += 1
        # 2.为父节点构造右侧子节点
        if idx < len(values):
            rightVal = values[idx]
            if rightVal is not None:
                node.right = TreeNode(rightVal)
                dq.append(node.right)
        idx += 1

    return root


# 2.前序遍历:先根节点，再左子树，最后右子树
def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    ans = []

    def dfs(root):
        if not root:
            return
        else:
            # 先根节点，再左子树，最后右子树
            ans.append(root.value)
            dfs(root.left)
            dfs(root.right)

    dfs(root)
    return ans


# 3.中序遍历：先遍历左子树，再遍历根节点，最后遍历右子树
def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    ans = []

    def dfs(root):
        if not root:
            return
        else:
            # 先左子树，再根节点，最后右子树
            dfs(root.left)
            ans.append(root.value)
            dfs(root.right)

    dfs(root)
    return ans


# 4.后续遍历：先遍历左子树，再遍历右子树，最后遍历根节点
def postorderTraversal(root: Optional[TreeNode]) -> List[int]:
    ans = []

    def dfs(root):
        if not root:
            return
        else:
            # 先左节点，再右节点，最后根节点
            dfs(root.left)
            dfs(root.right)
            ans.append(root.value)

    dfs(root)
    return ans


# 5.层序遍历：按树的层级，从上到下，从左到右进行遍历
# 1）返回的是二叉树第一层到最后一层节点val的二维数组列表
# 2）队列 queues 中不会存在 None 指针。
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    res = []
    queues = [root]
    # 1。从上往下遍历二叉树的每一层
    while queues:
        size = len(queues)
        tmp = []  # 用来存每一层左右节点val
        # 2。从左到右遍历每一层的每个节点： 不需要记录层数（步数）时可以去掉 for 循环
        for _ in range(size):
            node = queues.pop(0)  # 先进先出
            tmp.append(node.val)
            # 将下一层节点放入队列，注意：这2个if顺序不能换，queues中不存空节点
            if node.left:
                queues.append(node.left)
            if node.right:
                queues.append(node.right)
        # 3。将临时list加入最终返回结果中
        res.append(tmp)
    return res


# 5.层序遍历：返回一维数组列表
# 1）返回的一维数组按照leetcode的表现形式
# 2）queues 队列包含：非空节点 的某个子节点为空，则用None 表示
# 特殊层序遍历会遍历有值节点的 None 子节点，末尾连续输入的若干空节点会被去除。
def levelOrder2(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    res = []
    queues = [root]

    while queues:
        size = len(queues)
        for _ in range(size):
            node = queues.pop(0)
            # 对空指针的检验从「将元素加入队列」的时候改成了「从队列取出元素」的时候。
            # 1。当前节点不为空: queues只添加不为空的node左右子节点，res记录节点val
            if node:
                res.append(node.val)
                queues.append(node.left)
                queues.append(node.right)
            # 2。当前节点为空，并且队列里面至少有一个节点不为空: queues不添加空节点,res记录None值
            elif not node and any(queues):
                res.append(None)
                continue
            # 3.queues里面全是空值，打破循环
            else:
                break
    return res


# 6.二叉树最大深度：整棵树的最大深度等于左右子树的最大深度取最大值 + 根节点
def maxDepth(root: Optional[TreeNode]) -> int:
    # 自底向上搜索：后续遍历(分解问题的思路)
    if not root:
        return 0

    # 利用定义，计算左右子树的最大深度
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    # 整棵树的最大深度等于左右子树的最大深度取最大值，
    # 然后再加上根节点自己
    res = max(left_depth, right_depth) + 1
    return res


# 7.二叉树的所有节点个数
def countNodes(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    # 先算出左右子树有多少节点
    left = countNodes(root.left)
    right = countNodes(root.right)
    # 后序位置，子树加上自己，就是整棵二叉树的节点数
    return (left + right) + 1


def searchNode(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """8.在普通二叉树中查找根节点值为target的子节点，并返回该节点(默认二叉树所有节点元素唯一)"""
    if not root:
        return None
    # 分别查找根节点，左子树，右子树，如果找到target，马上返回，结束递归
    if root.val == target:
        return root
    left = searchNode(root.left, target)
    if left:
        return left
    right = searchNode(root.right, target)
    if right:
        return right
    return None


if __name__ == '__main__':
    # values = [3, 9, 20, None, None, 15, 7]
    # values = [1, 2, 3, 4, None, 5, 6, None, None, 7]
    # values = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    values = [1, None, 3, 2, 4, None, None, None, 5]
    # root = create(values)
    root2 = insert(values)
    # print(root)
    print(root2)
    # print(levelOrder2(root))
    # print(levelOrder2(root2))
    # print(countNodes(root))
    # print(countNodes(root2))
    # print(levelOrder(root))
    # print(preorderTraversal(root))
    # print(preorderTraversal(root1))
    # print(count(root))


