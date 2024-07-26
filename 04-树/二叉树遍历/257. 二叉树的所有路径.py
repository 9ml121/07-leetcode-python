"""
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。

 
示例 1：
输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]

示例 2：
输入：root = [1]
输出：["1"]
 

提示：
树中节点的数目在范围 [1, 100] 内
-100 <= Node.val <= 100
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional

# 写法1
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 返回所有从根节点到叶子节点的路径
        ans = []

        def dfs(root, path=[]):
            if not root:
                return

            path.append(root.val)

            # 叶子节点,更新ans
            if not root.left and not root.right:
                ans.append('->'.join(map(str, path)))
                return

            if root.left:
                dfs(root.left, path)
                path.pop()

            if root.right:
                dfs(root.right, path)
                path.pop()

        dfs(root)
        return ans

# 写法2
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # 返回所有从根节点到叶子节点的路径
        ans = []

        def dfs(root, path=[]):
            if not root:
                return

            # 叶子节点，更新ans
            if not root.left and not root.right:
                path.append(root.val)
                ans.append('->'.join(map(str, path)))
                path.pop()
                return

            # 前序位置添加数据
            path.append(root.val)
            
            # 分别递归左右子树
            dfs(root.left, path)
            dfs(root.right, path)
            
            # 后续位置回溯
            path.pop()

        dfs(root)
        return ans
