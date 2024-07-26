"""
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：
在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。
若最底层为第 h 层，则该层包含 1~ 2^h 个节点。



示例 1：
         1
       /  \
      2    3
     / \  /
    4  5 6
输入：root = [1,2,3,4,5,6]
输出：6

示例 2：
输入：root = []
输出：0

示例 3：
输入：root = [1]
输出：1

提示：
树中节点的数目范围是[0, 5 * 10^4]
0 <= Node.val <= 5 * 10^4
题目数据保证输入的树是 完全二叉树


进阶：遍历树来统计节点是一种时间复杂度为 O(n) 的简单解决方案。你可以设计一个更快的算法吗？
"""
from myTreeNode import *


# 方法 1：dfs计算普通二叉树节点个数
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftCnt = self.countNodes(root.left)
        rightCnt = self.countNodes(root.right)

        # 后序位置，子树加上自己，就是整棵二叉树的节点数
        return leftCnt + rightCnt + 1


"""
要计算完全二叉树的节点数量，可以利用完全二叉树的特性进行计算。

完全二叉树的定义是：
除了最后一层外，其他层的节点都是满的，并且最后一层的节点依次从左到右排列。

根据这个定义，我们可以使用以下步骤计算完全二叉树的节点数量：
1.首先，计算完全二叉树的高度。
  可以从根节点开始，一直沿着左子节点向下遍历，直到遇到空节点为止。
  记下遍历的次数，即为完全二叉树的高度。
  
2.计算最后一层的节点数量。
  最后一层的节点数量可能不满，但是一定是从左到右连续排列的。
  可以通过遍历最后一层的节点，依次计数，直到遇到空节点为止。

3.计算完全二叉树除最后一层外的节点数量。
  完全二叉树除最后一层外的节点总数可以通过公式计算得到。
  假设完全二叉树的高度为 h，则除最后一层外的节点数量为 2^h - 1。

4.将最后一层的节点数量与除最后一层外的节点数量相加，即可得到完全二叉树的总节点数量。
"""


# 方法 2：计算完全二叉数的节点个数
class Solution2:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # 1.计算完全二叉树的高度
        height = 0
        p = root
        while p:
            height += 1
            p = p.left

        # 2.计算最后一层的节点数量。
        def countLastLevel(root, level, height) -> int:
            if not root:  # 如果叶子节点为空，计为 0
                return 0
            if level == height:  # 如果叶子节点不为空，最后一层每个节点计为 1
                return 1

            leftCnt = countLastLevel(root.left, level + 1, height)
            rightCnt = countLastLevel(root.right, level + 1, height)

            return leftCnt + rightCnt

        last_level_cnt = countLastLevel(root, 1, height)

        # 3.计算完全二叉树除最后一层外的节点数量(满二叉树)
        other_level_cnt = 2 ** (height - 1) - 1
        # print(other_level_cnt)

        # 4.完全二叉树的总节点数量
        return other_level_cnt + last_level_cnt


# 方法 3：计算完全二叉数的节点个数（优化版）  推荐！！！
# 完全二叉树的左子树或者右子树一定有一边是满二叉树
class Solution3:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # 计算完全二叉树的高度
        def getHeight(node) -> int:
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        if not root:
            return 0

        leftH = getHeight(root.left)
        rightH = getHeight(root.right)
        if leftH == rightH:
            # 1.如果左右子树高度相等，说明左子树一定是满二叉树
            # return 2 ** leftH + self.countNodes(root.right)  # 或者用位运算
            return (1 << leftH) + self.countNodes(root.right)
        else:
            # 2.如果左右子树高度不相等，说明右子树一定是满二叉树
            # return self.countNodes(root.left) + 2 ** rightH  # 或者用位运算
            return self.countNodes(root.left) + (1 << rightH)


if __name__ == '__main__':
    root = [1, 2, 3, 4, 5, 6]  # 6
    node = buildTree(root)
    print(Solution2().countNodes(node))
    print(Solution3().countNodes(node))
