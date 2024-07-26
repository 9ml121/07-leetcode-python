"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，
请你构造并返回这颗 二叉树 。

示例 1:
     3
    / \
   9  20
      / \
     15  7
输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

示例 2:
输入：inorder = [-1], postorder = [-1]
输出：[-1]

提示:
1 <= inorder.n <= 3000
postorder.n == inorder.n
-3000 <= inorder[i], postorder[i] <= 3000
inorder 和 postorder 都由 不同 的值组成
postorder 中每一个值都在 inorder 中
inorder 保证是树的中序遍历
postorder 保证是树的后序遍历
"""
from myTreeNode import *


# 方法1 :分解思路
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        valToIndex = {val: i for i, val in enumerate(inorder)}  # 中序遍历val对应的数组索引下标
        
        def build(inStart, inEnd, postStart, postEnd):
            # base case
            if inStart > inEnd:
                return

            # 先从postOrder确定根节点val,构建root对象
            rootVal = postorder[postEnd]
            root = TreeNode(rootVal)

            # 在根据inOrder确定构建左左子树长度，构建左右子树对象
            idxOfRoot = valToIndex[rootVal]
            leftSize = idxOfRoot - inStart
            root.left = build(inStart, idxOfRoot - 1,  # 左--根--右
                              postStart, postStart + leftSize - 1)  # 左--右--根
            root.right = build(idxOfRoot + 1, inEnd,
                               postStart + leftSize, postEnd - 1)

            return root

        return build(0, len(inorder) - 1, 0, len(postorder) - 1)  # 闭区间


# 方法2：递归函数中直接修改题目给定的遍历数组(不推荐)
def buildTree2(inorder: List[int], postorder: List[int]) -> TreeNode:
    # todo 函数定义：根据inorder数组[in_left..in_right]闭区间索引位置，返回二叉树root对象
    def helper(in_left, in_right):
        # 如果这里没有节点构造二叉树了，就结束
        if in_left > in_right:
            return None

        # 选择 post_idx 位置的元素作为当前子树根节点
        val = postorder.pop()  # 将后续遍历数组的根节点依次弹出
        root = TreeNode(val)

        # 根据 root 所在位置分成左右两棵子树
        rootIdx = valToIdx[val]

        # 先构造右子树
        root.right = helper(rootIdx + 1, in_right)
        # 后构造左子树
        root.left = helper(in_left, rootIdx - 1)
        return root

    # 建立（元素，下标）键值对的哈希表
    valToIdx = {val: idx for idx, val in enumerate(inorder)}
    return helper(0, len(inorder) - 1)
