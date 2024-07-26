"""
给定一个二叉搜索树 root 和一个目标结果 k，如果二叉搜索树中存在两个元素且它们的和等于给定的目标结果，则返回 true。



示例 1：


输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
示例 2：


输入: root = [5,3,6,2,4,null,7], k = 28
输出: false


提示:

二叉树的节点个数的范围是  [1, 104].
-104 <= Node.val <= 104
题目数据保证，输入的 root 是一棵 有效 的二叉搜索树
-105 <= k <= 105
"""
from myTreeNode import *


# 方法一：深度优先搜索 + 哈希表
# dfs也可以换成 bfs
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(root, k):
            if not root:
                return False

            target = k - root.val
            if target in seen:
                return True

            seen.add(root.val)

            return dfs(root.left, k) or dfs(root.right, k)

        return dfs(root, k)


# 方法三：深度优先搜索 + 中序遍历 + 双指针
class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        sortedList = []

        # 1.中序遍历得到一个升序的数组
        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            sortedList.append(root.val)
            inOrder(root.right)

        # 2.利用双指针从升序数组寻找是否存在两数之和为 k
        left, right = 0, len(sortedList) - 1
        while left < right:
            sumV = sortedList[left] + sortedList[right]
            if sumV < k:
                left += 1
            elif sumV > k:
                right -= 1
            else:
                return True

        return False
