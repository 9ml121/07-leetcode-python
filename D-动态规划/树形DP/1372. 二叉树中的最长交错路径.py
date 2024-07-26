"""
给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

选择二叉树中 任意 节点和一个方向（左或者右）。
如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
改变前进方向：左变右或者右变左。
重复第二步和第三步，直到你在树中无法继续移动。
交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

请你返回给定树中最长 交错路径 的长度。

示例 1：
         1
          \
           1
          / \
         1   1
            / \
           1   1
            \
             1
              \
               1
输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。

示例 2：
         1
        / \
       1   1
        \
         1
        / \
       1   1
        \
         1
输入：root = [1,1,1,null,1,null,null,1,1,null,1]
输出：4
解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。

示例 3：
输入：root = [1]
输出：0


提示：
每棵树最多有 50000 个节点。
每个节点的值在 [1, 100] 之间。
"""
from myTreeNode import *

"""
题目要求找出二叉树中的最长交错路径的长度。交错路径是指在路径中相邻节点的左右子树交替的路径。

下面给出解题的思路：
1.定义一个全局变量 max_length，用于记录最长交错路径的长度。
2.创建一个递归函数 dfs(node, is_left, length)，其中 
    node 表示当前节点，
    is_left 表示当前节点是否为左子节点，
    length 表示当前路径的长度。
3.在递归函数中，首先处理递归的终止条件，即节点为空时，返回。
4.判断当前节点与父节点的关系，
    如果是左子节点且上一个节点是右子节点，
    或者是右子节点且上一个节点是左子节点，
    说明路径交替，将当前路径长度加 1，否则将路径长度重置为 1。
5.更新 max_length 的值，取当前路径长度和 max_length 中的较大值。
6.递归调用 dfs 函数，分别处理当前节点的左子节点和右子节点，传递对应的参数。
7.在主函数中，调用 dfs 函数处理根节点，并返回 max_length 的值作为结果。
"""


# 树形 DP
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxLen = 0

        def dfs(node, is_left: bool, curLen: int):
            """
            @node 表示当前节点，
            @is_left 表示当前节点是否为左子节点，
            @curLen 表示当前路径的长度。
            """
            if not node:
                return

            if is_left:
                # 当前节点是左节点
                if node.left:
                    dfs(node.left, True, 1)
                if node.right:
                    dfs(node.right, False, curLen + 1)
            else:
                # 当前节点不是左节点
                if node.left:
                    dfs(node.left, True, curLen + 1)
                if node.right:
                    dfs(node.right, False, 1)
            nonlocal maxLen
            maxLen = max(maxLen, curLen)

        dfs(root, False, 0)
        return maxLen


if __name__ == '__main__':
    root = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1]
    # root = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
    node = buildTree(root)
    print(node)
    print(Solution().longestZigZag(node))
