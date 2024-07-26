"""
给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），
使每个节点 node 的新值等于原树中大于或等于 node.value 的值之和。

提醒一下，二叉搜索树满足下列约束条件：
1.节点的左子树仅包含键 小于 节点键的节点。
2.节点的右子树仅包含键 大于 节点键的节点。
3.左右子树也必须是二叉搜索树。

注意：本题和 1038: https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/ 相同

示例 1：
             4(30)
           /      \
          1(36)   6(21)
         / \      /     \
    0(36)  2(35) 5(26) 7(15)
            \            \
             3(33)        8(8)

输入：[4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
输出：[30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
示例 2：

输入：root = [0,None,1]
输出：[1,None,1]
示例 3：

输入：root = [1,0,2]
输出：[3,3,2]
示例 4：

输入：root = [3,2,4,1]
输出：[7,9,4,10]


提示：

树中的节点数介于 0 和 104 之间。
每个节点的值介于 -104 和 104 之间。
树中的所有值 互不相同 。
给定的树为二叉搜索树。
"""
from myTreeNode import *


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """将二叉搜索树转换为累加树, 返回新的二叉树
        todo 反序中序遍历
        """
        # 全局变量，代表当前节点的累计和
        self.total = 0

        def dfs(root) -> Optional[TreeNode]:
            """按照累加和，更新root， 返回值有或者没有都可以"""
            if not root:
                return None
            root.right = dfs(root.right)
            self.total += root.value
            root.value = self.total
            root.left = dfs(root.left)

            return root

        return dfs(root)


if __name__ == '__main__':
    # 输入：[4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    # 输出：[30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
    arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
    # root = create(arr)
    root = buildTree(arr)

    print(levelOrder2(root))

    tree = Solution().convertBST(root)
    print(levelOrder2(tree))
