"""
给你一棵二叉树的根节点 root ，返回所有 重复的子树 。
对于同一类的重复子树，你只需要返回其中任意 一棵 的根结点即可。

如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。

示例 1：



输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]
示例 2：



输入：root = [2,1,1]
输出：[[1]]
示例 3：



输入：root = [2,2,2,3,null,3,null]
输出：[[2,3],[3]]
提示：

树中的结点数在 [1, 5000] 范围内。
-200 <= Node.value <= 200
"""
from typing import Optional, List

from myTreeNode2 import TreeNode
import myTreeNode2


def findDuplicateSubtrees(root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
    # 寻找重复的子树
    # 如果两棵树具有 相同的结构 和 相同的结点值 ，则认为二者是 重复 的。
    memo = {}
    res = []

    def traverse(root):
        if not root:
            return '#'

        left = traverse(root.left)
        right = traverse(root.right)

        subTree = left + "," + right + "," + str(root.value)  # 注意，这里必须要插入一个分隔符

        # 给子树对应的出现次数加一
        memo[subTree] = memo.get(subTree, 0) + 1
        # 多次重复也只会被加入结果集一次
        if memo[subTree] == 2:
            res.append(root)

        return subTree

    traverse(root)
    # print(memo)
    return res


if __name__ == '__main__':
    lst = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    root = myTreeNode.insert(lst)
    print(myTreeNode.levelOrder(root))
    res = findDuplicateSubtrees(root)
    for elem in res:
        print(myTreeNode.preorderTraversal(elem))
