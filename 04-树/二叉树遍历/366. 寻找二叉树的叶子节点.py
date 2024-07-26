"""
给你一棵二叉树，请按以下要求的顺序收集它的全部节点：

依次从左到右，每次收集并删除所有的叶子节点
重复如上过程直到整棵树为空

示例1:
          1
         / \
        2   3
       / \
      4   5
输入: [1,2,3,4,5]
输出: [[4,5,3],[2],[1]]


解释:
1. 删除叶子节点 [4,5,3] ，得到如下树结构：
          1
         /
        2

2. 现在删去叶子节点 [2] ，得到如下树结构：
          1

3. 现在删去叶子节点 [1] ，得到空树：
          []
"""
from myTreeNode import *


# 解法1：dfs后续位置，计算每个节点高度。对于同一高度的节点，创建一个新列表进行搜集（也可以换成字典）
# 自底向上搜集二叉树的叶子节点，并没有删除叶子节点
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = []
        self.dfs(root)
        return self.res

    def dfs(self, root) -> int:
        """返回每个节点的高度，默认叶子节点高度为0"""
        if not root:
            return -1
        leftHeight = self.dfs(root.left)
        rightHeight = self.dfs(root.right)

        # 后续位置，计算节点高度
        height = max(leftHeight, rightHeight) + 1

        # 如果节点高度不在结果列表中，说明要新建一个列表
        if height == len(self.res):
            self.res.append([])
        self.res[height].append(root.val)
        # 返回节点高度
        return height


# 解法2：自顶向下，每次判断节点是否为叶子节点，如果是，进行搜集，搜集完之后将节点删除。
# 需要多次递归！！时间复杂度O(n^2)
class Solution2:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        while root:
            levelVals = []
            root = self.dfs(root, levelVals)
            res.append(levelVals)
        return res

    def dfs(self, root, levelVals) -> Optional[TreeNode]:
        """返回叶子层节点"""
        if not root:
            return None
        if not root.left and not root.right:
            levelVals.append(root.val)
            return None

        root.left = self.dfs(root.left, levelVals)
        root.right = self.dfs(root.right, levelVals)

        return root


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    root = buildTree(arr)
    print(Solution().findLeaves(root))
    print(levelOrder2(root))

    print(Solution2().findLeaves(root))
    print(levelOrder2(root))