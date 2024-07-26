"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。
可以按 任意顺序 返回答案。

示例 1：

   1         1         2         3         3
    \         \       / \       /         /
     3         2     1   3     2         1
    /           \             /           \
   2             3           1             2
输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

示例 2：
输入：n = 1
输出：[[1]]


提示：
1 <= n <= 8
"""
from myTreeNode import *

'''
解题思路：
题目要求生成所有可能的二叉搜索树，我们可以考虑采用递归的方法。 
1.对于任意一个节点i，它可以作为根节点，左子树由节点1~i-1构成，右子树由节点i+1~n构成。
2.然后递归构造左右子树的所有合法二叉搜索树，并将它们组合起来，就可以得到以i为根节点的所有合法二叉搜索树。 
3.最后将所有以1~n为根节点的合法二叉搜索树组合起来，就可以得到所有可能的二叉搜索树。 
'''


# 构造二叉搜索树
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # 在[minV..maxV]取值区间构造二叉树
        def dfs(minV, maxV) -> List[Optional[TreeNode]]:
            # 当 lo > hi 时，不存在节点，将 None 存入结果列表中，并返回
            if minV > maxV:
                # todo 如果当前子树为空，不加null行吗？
                return [None]

            # todo list为什么定义为局部变量而不是全局变量？
            allTrees = []
            # 1、穷举 root 节点的所有可能。
            for i in range(minV, maxV + 1):
                # 2、递归构造出左右子树的所有合法 BST。
                # todo root = TreeNode(i)可以在这里开始构建吗？
                leftTree = dfs(minV, i - 1)
                rightTree = dfs(i + 1, maxV)
                # 3、给 root 节点穷举所有左右子树的组合。
                for left in leftTree:
                    for right in rightTree:
                        # i 作为根节点 root 的值
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        allTrees.append(root)

            return allTrees

        return dfs(1, n) if n else []


if __name__ == '__main__':
    n = 3
    # arr = [1, 2]
    # root = insert(arr)
    res = Solution().generateTrees(n)
    for node in res:
        print(levelOrder2(node))
    # [1, None, 2, None, 3] ==> TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    # [1, None, 3, 2]       ==> TreeNode(1, None, TreeNode(3, TreeNode(2), None))
    # [2, 1, 3]             ==> TreeNode(2, TreeNode(1), TreeNode(3))
    # [3, 1, None, None, 2] ==> TreeNode(3, TreeNode(1, None, TreeNode(2)), None)
    # [3, 2, None, 1]       ==> TreeNode(3, TreeNode(2, TreeNode(1), None), None)

'''
当n=3时，以下是递归的过程（假设我们用dfs(1,3)来表示构造[1,2,3]的二叉搜索树的过程）：
 dfs(1,3)
    i=1
    leftTree = dfs(1,0)  # 返回[None]
    rightTree = dfs(2,3)
        i=2
        leftTree = dfs(2,1)  # 返回[None]
        rightTree = dfs(3,3)  # 返回[TreeNode(3)]
        root = TreeNode(2)
        root.left = None
        root.right = TreeNode(3)
        res = [root]
    root = TreeNode(1)
    root.left = None
    root.right = res[0]
    res = [root]
     i=2
    leftTree = dfs(1,1)  # 返回[TreeNode(1)]
    rightTree = dfs(3,3)  # 返回[TreeNode(3)]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    res.append(root)
     i=3
    leftTree = dfs(1,2)
        i=1
        leftTree = dfs(1,0)  # 返回[None]
        rightTree = dfs(2,2)  # 返回[TreeNode(2)]
        root = TreeNode(1)
        root.left = None
        root.right = TreeNode(2)
        res = [root]
         i=2
        leftTree = dfs(1,1)  # 返回[TreeNode(1)]
        rightTree = dfs(3,2)  # 返回[None]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = None
        res.append(root)
     rightTree = dfs(3,3)  # 返回[TreeNode(3)]
    root = TreeNode(3)
    root.left = res[0]
    root.right = res[1]
    res = [root]
 返回res，即[TreeNode(1, None, TreeNode(2, None, TreeNode(3))), TreeNode(1, None, TreeNode(3, TreeNode(2), None)), TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(3, TreeNode(1), TreeNode(2))]
'''
