"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。


示例 1:
         5
       /  \
      3    6
     / \    \
    2  4     7
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
        5
       / \
      4   6
     /     \
    2       7
另一个正确答案是 [5,2,6,null,4,null,7]。
         5
       /  \
      2    6
      \     \
       4     7

示例 2:
输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点

示例 3:
输入: root = [], key = 0
输出: []


提示:
节点数的范围 [0, 104].
-105 <= Node.value <= 105
节点值唯一
root 是合法的二叉搜索树
-105 <= key <= 105


进阶： 要求算法时间复杂度为 O(h)，h 为树的高度。
"""
from myTreeNode import *

"""
key = 4
          6                
        /  \
       4    7
      / \    \
     2   5    8
    / \
   1   3
"""


# 方法 1：删除节点之后会让树的高度不平衡
# todo 二叉平衡搜索树，删除节点时旋转子树，使得左右子树平衡
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """删除二叉搜索树中的节点，返回删除之后的根节点对象"""
        if not root:
            return None

        # 1.如果当前节点值大于目标节点，则去左子树中删除；
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        # 2.如果当前节点值小于目标节点，则去右子树中删除；
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # 3.如果目标节点就是当前节点，分为以下三种情况
        else:
            # 1）其左右子节点都有
            # a.其左子树转移到其右子树的最左节点的左子树上，然后右子树顶替其位置，由此删除了该节点。
            # b.或者将右子树转移到其左子树的最右节点的右子树上，然后左子树顶替其位置
            #  todo 注意：上面 2 种方法会让树的高度不平衡，但是编码简单
            if root.left and root.right:
                # todo 查找 root左子树值最大的节点, 并在最大节点右边拼接上 root右子树
                maxNode = self.getMaxNode2(root.left)
                maxNode.right = root.right
                return root.left

            # 2) 其无左子：其右子顶替其位置，删除了该节点；反之亦然
            return root.left if not root.right else root.right

        # 4.最后返回构造之后的根节点
        return root

    def getMaxNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """查找二叉搜索树值最大的节点，并返回(递归方法)"""
        if not root:
            return None
        if not root.right:
            return root
        # 递归函数之前加return,代表的含义是:一旦找到了递归出口,就马上返回,不需要在继续递归下去
        return self.getMaxNode(root.right)

    def getMaxNode2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """查找二叉搜索树值最大的节点，并返回(迭代写法)"""
        while root.right:
            root = root.right
        return root


if __name__ == '__main__':
    # root = [5, 3, 6, 2, 4, None, 7]
    # key = 3
    root = [5, 3, 6, 2, 4, None, 7]
    key = 5
    node = buildTree(root)
    newNode = Solution().deleteNode(node, key)
    print(levelOrder2(newNode))
