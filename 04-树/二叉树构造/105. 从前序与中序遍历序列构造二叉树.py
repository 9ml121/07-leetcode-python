"""
给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1:
     3
    / \
   9  20
      / \
     15  7
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2:
输入: preorder = [-1], inorder = [-1]
输出: [-1]

提示:
1 <= preorder.n <= 3000
inorder.n == preorder.n
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证 为二叉树的前序遍历序列
inorder 保证 为二叉树的中序遍历序列
"""
from myTreeNode import *


# 方法1
# 分解问题思路：递归函数有返回值
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(inorder)
        # valToIndex记录 inorder 中 val 对应的索引位置
        valToIndex = {val: i for i, val in enumerate(inorder)}

        # print(valToIndex)

        # build函数：根据root的左右节点值在 preorder[preStart..preEnd]和 inorder[inStart..inEnd]中对应的索引位置，返回root对象
        def build(preStart, preEnd, inStart, inEnd):
            # base case
            if preStart > preEnd:
                return

            # root的val很容易确定，就在preorder的第一位, 先构造出当前根节点
            rootVal = preorder[preStart]
            root = TreeNode(rootVal)

            # todo 计算root左右节点在preorder数组中的索引位置，构建root的左右节点
            # root左右子节点val在preorder不容易确定，但是在inorder是确定的，就在inorder根节点val的左边和右边
            idx = valToIndex[rootVal]  # 根节点在中序遍历数组中的索引
            leftSize = idx - inStart   # 左节点长度
            root.left = build(preStart + 1, preStart + leftSize,  # 根节点->左节点->右节点
                              inStart, idx - 1)  # 左节点->根节点->右节点

            root.right = build(preStart + leftSize + 1, preEnd,
                               idx + 1, inEnd)
            return root

        return build(0, n - 1, 0, n - 1)


if __name__ == '__main__':
    preOrder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    inOrder = [3, 2, 5, 4, 6, 1, 8, 7, 9]
    root = Solution().buildTree(preOrder, inOrder)
    print(levelOrder2(root))
