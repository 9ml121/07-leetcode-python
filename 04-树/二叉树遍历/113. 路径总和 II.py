"""
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。


示例 1：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

示例 2：
输入：root = [1,2,3], targetSum = 5
输出：[]

示例 3：
输入：root = [1,2], targetSum = 0
输出：[]


提示：
树中节点总数在范围 [0, 5000] 内
-1000 <= Node.value <= 1000
-1000 <= targetSum <= 1000

"""
from typing import Optional, List
from myTreeNode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right

# 类似：06-二叉树&BST\二叉树遍历\257. 二叉树的所有路径.py
# 写法1
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 找出所有 从根节点到叶子节点 路径总和等于targetSum的路径。
        ans = []

        def dfs(root, targetSum, path=[]):
            if not root:
                return

            targetSum -= root.val
            path.append(root.val)

            # 叶子节点更新ans
            if not root.left and not root.right:
                if targetSum == 0:
                    ans.append(path[:])  # 拷贝path
                return

            # 在递归调用之前如果先判断了非空，在递归完成以后，需要重置 path
            if root.left:
                dfs(root.left, targetSum, path)
                path.pop()
                
            if root.right:
                dfs(root.right, targetSum,  path)
                path.pop()

        dfs(root, targetSum)
        return ans

# 写法2
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # 找出所有 从根节点到叶子节点 路径总和等于targetSum的路径。
        ans = []

        def dfs(root, targetSum, path=[]):
            if not root:
                return

            targetSum -= root.val

            # 叶子节点更新ans
            if not root.left and not root.right:
                if targetSum == 0:
                    path.append(root.val)
                    ans.append(path[:])  # 拷贝path
                    path.pop()
                return
            
            path.append(root.val)
            dfs(root.left, targetSum, path)
            dfs(root.right, targetSum, path)
            path.pop()

        dfs(root, targetSum)
        return ans
