"""
给你一棵指定的二叉树的根节点 root ，请你计算其中 最长连续序列路径 的长度。
最长连续序列路径 是依次递增 1 的路径。
该路径，可以是从某个初始节点到树中任意节点，通过「父 - 子」关系连接而产生的任意路径。
且必须从父节点到子节点，反过来是不可以的。


示例 1：
   1
    \
     3
    / \
   2   4
        \
         5
输入：root = [1,null,3,2,4,null,null,null,5]
输出：3
解释：当中，最长连续序列是 3-4-5 ，所以返回结果为 3 。

示例 2：
        2
         \
          3
         /
        2
         \
          1
输入：root = [2,null,3,2,null,1]
输出：2
解释：当中，最长连续序列是 2-3 。注意，不是 3-2-1，所以返回 2 。


提示：
树中节点的数目在范围 [1, 3 * 10^4] 内
-3 * 10^4 <= Node.val <= 3 * 10^4
"""
from typing import Optional

import myTreeNode2
from myTreeNode2 import TreeNode

"""
问题描述：
给你一棵指定的二叉树的根节点 root ，请你计算其中 最长连续序列路径 的长度。
最长连续序列路径 是从父节点到子节点依次递增 1 的路径。
# 注意跟549题的区别
# 298题：只处理从父节点到子节点依次递增 1 的最长连续路径，可以用后续遍历，或者前序遍历
# 549题：连续路径是路径中相邻节点的值相差 1 的路径。此路径可以是增加或减少，就只能用后续遍历
"""


# 后续遍历
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # 从父节点到子节点依次递增 1 的最长连续路径
        maxLen = 1

        def dfs(node):
            nonlocal maxLen
            if not node:
                return 1

            leftLen = dfs(node.left)
            rightLen = dfs(node.right)

            if node.left and node.left.val == node.val + 1:
                leftLen += 1
            else:
                leftLen = 1
            if node.right and node.right.val == node.val + 1:
                rightLen += 1
            else:
                rightLen = 1

            maxLen = max(maxLen, leftLen, rightLen)
            return max(leftLen, rightLen)

        dfs(root)
        return maxLen


"""
解题思路：(前序遍历)
对于二叉树中的每个节点，我们可以考虑以下情况：
1.当前节点与其父节点值连续递增：
  如果当前节点的值比其父节点值大 1，那么当前节点可以加入到连续递增序列路径中，并继续向下递归。
2.当前节点与其父节点值不连续：
  如果当前节点的值与其父节点值不连续，那么当前节点无法加入到连续递增序列路径中，我们需要重新开始计算连续递增序列路径的长度。
3.因此，我们可以定义一个递归函数 dfs(node, parent, length)，它返回以 node 为根节点的子树中最长连续递增序列路径的长度。
  在递归函数中，我们首先处理递归的终止条件，即节点为空时，返回 0。
  然后，根据当前节点与其父节点的值来判断是否能够加入到连续递增序列路径中。
  1）如果可以，我们将路径长度加一，并继续向下递归。
  2）如果不可以，我们重新开始计算连续递增序列路径的长度。

4.为了记录最长连续递增序列路径的长度，我们可以使用一个全局变量 max_length 来存储当前最长的路径长度。
  在递归函数中，我们更新 max_length 的值，每次都取当前路径长度与 max_length 的较大值。
"""


# 前序遍历
class Solution2:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        # 计算其中 最长连续序列路径 的长度
        maxLen = 0

        def dfs(node, parent, curLen) -> None:
            nonlocal maxLen
            if not node:
                return
            # 前序遍历
            if not parent or node.val != parent.val + 1:
                curLen = 1
            else:
                curLen += 1
            maxLen = max(maxLen, curLen)

            dfs(node.left, node, curLen)
            dfs(node.right, node, curLen)

        dfs(root, None, 0)
        return maxLen


if __name__ == '__main__':
    node = [1, None, 3, 2, 4, None, None, None, 5]  # 3
    # node = [2, None, 3, 2, None, 1]  # 2
    root = myTreeNode2.insert(node)
    # root2 = myTreeNode.create(node)
    print(root)
    # print(root2)
    print(Solution().longestConsecutive(root))
