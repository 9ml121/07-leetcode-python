"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

示例 1：
        1
       / \
      2   2
     / \ / \
    3  4 4  3
输入：root = [1,2,2,3,4,4,3]
输出：true

示例 2：
        1
       / \
      2   2
       \   \
        3   3
输入：root = [1,2,2,null,3,null,3]
输出：false


提示：
树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100

进阶：你可以运用递归和迭代两种方法解决这个问题吗？
"""
from myTreeNode import *


# todo dfs方法(推荐)：本质上是动态规划的思想(后续遍历)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 判断二叉树是否轴对称
        
        def dfs(l_node=root.left, r_node=root.right)->bool:
            # 1.如果两个节点都为空，返回 True
            if not l_node and not r_node:
                return True
            
            # 2.如果其中一个节点为空或者左右节点值不相同，返回 False
            if not l_node or not r_node or l_node.val != r_node.val:
                return False

            # 3.递归判断两个节点的左右子树是否镜像对称
            res1 = dfs(l_node.left, r_node.right)
            res2 = dfs(l_node.right, r_node.left)
            return res1 and res2

        # 如果根节点为空，返回 True（空树被认为是对称的）
        if not root:
            return True

        return dfs()


# bfs方法
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 如果根节点为空，返回 True（空树被认为是对称的）
        if not root:
            return True

        # todo dq每个位置保存镜像对称的2个节点
        dq = collections.deque([(root.left, root.right)])
        
        while dq:
            node1, node2 = dq.popleft()
            # 如果两个节点都为空，继续遍历下一对节点
            if not node1 and not node2:
                continue
            
            # 如果其中一个节点为空，或者两个节点的值不相等，返回 False
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # 将 node1 的左子节点和 node2 的右子节点按照 [left, right] 的顺序入队。
            dq.append((node1.left, node2.right))
            # 将 node1 的右子节点和 node2 的左子节点按照 [left, right] 的顺序入队。
            dq.append((node1.right, node2.left))
        return True


if __name__ == '__main__':
    # root = [1, 2, 2, 3, 4, 4, 3]
    root = [1, 2, 2, None, 3, None, 3]
    node = buildTree(root)
    print(Solution2().isSymmetric(node))
