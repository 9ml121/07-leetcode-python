"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：
“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


示例 1：
          3
        /   \
       5     1
      / \   / \
     6   2 0   8
        / \
       7   4
输入：root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

示例 2：
          3
        /   \
       5     1
      / \   / \
     6   2 0   8
        / \
       7   4
输入：root = [3,5,1,6,2,0,8,None,None,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

示例 3：
输入：root = [1,2], p = 1, q = 2
输出：1


提示：
树中节点数目在范围 [2, 10^5] 内。
-10^9 <= Node.value <= 10^9
所有 Node.value 互不相同 。
p != q
p 和 q 均存在于给定的二叉树中。
"""
from myTreeNode import *

# 分析
"""
若 root 是 p,q 的 最近公共祖先 ，则只可能为以下3种情况之一：
    1          
   / \
  2   3  
 / \
4   5
   / \
  6   7
1.p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
    p=4  q=7  root=2
2.p=root，且 q 在 root 的左或右子树中；
    p=2  q=7  root=p
3.q=root，且 p 在 root 的左或右子树中；
    p=4  q=1  root=q
    
找2个节点的最近公共祖先，分为3步：
1.先在二叉树中找到目标节点，
2,再将他们的最近祖先节点通过递归函数返回值传递回去
3.最后判断返回值是上面3种情况的那一种
"""


# https://www.yuque.com/limq/sycuqd/is3bsyrni03tgw4p?singleDoc# 《典型问题 2：二叉树的最近公共祖先》
# leetcode236.二叉树的最近公共祖先
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        返回以root为根节点，子节点p, q的最近祖先节点: p,q均在给定的二叉树
        todo 如果一个节点能够在它的左右子树中分别找到 p 和 q，则该节点为 LCA 节点
        """
        if not root:
            return None

        # 1.前序位置: 看看 root 是不是目标值，如果是，直接返回，后面的节点不用再遍历
        if root == p or root == q:
            return root

        # 2.root 不是目标节点，去左右子树寻找
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 3.后序位置，判断当前节点是不是 LCA 节点
        # 如果 left 和 right 都不为空，则说明 p 和 q 分别在左右子树中，此时根节点为最近公共祖先，返回根节点。
        if left and right:
            return root

        # root 不是目标节点，再去看看哪边的子树找到了
        return left if left else right


# leetcode 1644. 二叉树的最近公共祖先 II
class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        返回给定节点 p 和 q 的最近公共祖先（LCA）节点: p,q不一定在给定的二叉树节点上
        todo 如果 p 或 q 之一 不存在 于该二叉树中，返回 null
        """
        # 用于记录 p 和 q 是否存在于二叉树中
        self.findP = False
        self.findQ = False
        lca = self.find(root, p, q)

        # p 和 q 都存在二叉树中，才有公共祖先
        if self.findP and self.findQ:
            return lca
        return None

    # 在二叉树中寻找 val1 和 val2 的最近公共祖先节点
    def find(self, root, p, q) -> 'TreeNode':
        if not root:
            return None

        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)

        # 后序位置，判断当前节点是不是 LCA 节点
        # 如果 left 和 right 都不为空，则说明 p 和 q 分别在左右子树中，此时当前节点为最近公共祖先
        if left and right:
            return root

        # todo 后序位置，判断当前节点是不是目标值
        if root == p or root == q:
            # 找到了，记录一下
            if root == p:
                self.findP = True
            if root == q:
                self.findQ = True
            return root

        # root 不是目标节点，再去看看哪边的子树找到了
        return left if left else right


# leetcode 1676. 二叉树的最近公共祖先 IV
class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        给定一棵二叉树的根节点 root 和 TreeNode 类对象的数组（列表） nodes，
        todo 返回 nodes 中所有节点的最近公共祖先（LCA）。
        1.数组（列表）中所有节点都存在于该二叉树中，且二叉树中所有节点的值都是互不相同的。
        2.允许一个节点是其自身的后代
        """
        # 将列表转化成哈希集合，便于判断元素是否存在
        nodes = set(nodes)

        # 在二叉树中寻找 values 的最近公共祖先节点
        def find(root, nodes: set) -> 'TreeNode':
            # 递归终止条件：如果root为空，返回None
            if not root:
                return None

            # 1.前序位置：找到一个目标节点就把目标节点返回，目标节点后续节点不用再遍历
            if root in nodes:
                return root

            # 2.递归查找左右子树
            left = find(root.left, nodes)
            right = find(root.right, nodes)

            # 3.后序位置，已经知道左右子树是否存在目标值
            if left and right:
                return root

            return left if left else right

        return find(root, nodes)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    # p = root.left
    # q = root.right
    # self.assertEqual(Solution().lowestCommonAncestor(root, p, q), root)

    p = root.left
    q = root.left.right.right
    # self.assertEqual(Solution().lowestCommonAncestor(root, p, q), p)
    print(Solution().lowestCommonAncestor(root, p, q))
