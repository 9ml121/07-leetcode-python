"""
给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。

二叉搜索树的定义如下：
任意节点的左子树中的键值都 小于 此节点的键值。
任意节点的右子树中的键值都 大于 此节点的键值。
任意节点的左子树和右子树都是二叉搜索树。


示例 1：



输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。
示例 2：



输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。
示例 3：

输入：root = [-4,-2,-5]
输出：0
解释：所有节点键值都为负数，和最大的二叉搜索树为空。
示例 4：

输入：root = [2,1,3]
输出：6
示例 5：

输入：root = [5,4,8,3,null,6,3]
输出：7


提示：

每棵树有 1 到 40000 个节点。
每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
"""
from myTreeNode import *

"""
我们用一个结构体来描述一个子树的基本情况，它应当包含以下元素：
isBST，表示该子树是否为二叉搜索树；
minValue，表示该子树中的最小值；
maxValue，表示该子树中的最大值；
sumValue，表示该子树中所有节点的键值之和，用于求解答案。
"""


class SubTree:
    def __init__(self, isBST: bool, minVal, maxVal, sumVal) -> None:
        self.isBST = isBST
        self.minVal = minVal
        self.maxVal = maxVal
        self.sumVal = sumVal


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        maxSum = 0

        def dfs(root) -> SubTree:
            if not root:
                return SubTree(True, float('inf'), float('-inf'), 0)

            leftSubTree = dfs(root.left)
            rightSubTree = dfs(root.right)

            nonlocal maxSum
            if leftSubTree.isBST and rightSubTree.isBST and leftSubTree.maxVal < root.val < rightSubTree.minVal:
                sumVal = root.val + leftSubTree.sumVal + rightSubTree.sumVal
                maxSum = max(maxSum, sumVal)
                return SubTree(True, min(root.val, leftSubTree.minVal), max(root.val, rightSubTree.maxVal), sumVal)
            else:
                return SubTree(False, 0, 0, 0)

        dfs(root)
        return maxSum
