"""
给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。

返回包含原始树中所有 最深节点 的 最小子树 。

如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。
一个节点的 子树 是该节点加上它的所有后代的集合。

示例 1：
         3
       /   \
      5     1
     / \   / \
    6   2 0   8
       / \
      7   4
输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：
我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点(7和4)。
注意，节点 5、3 和 2 包含树中最深的节点，但节点 2 的子树最小，因此我们返回它。

示例 2：
输入：root = [1]
输出：[1]
解释：根节点是树中最深的节点。

示例 3：
         0
        / \
       1   3
        \
         2
输入：root = [0,1,3,null,2]
输出：[2]
解释：树中最深的节点为 2 ，有效子树为节点 2、1 和 0 的子树，但节点 2 的子树最小。


提示：
树中节点的数量在 [1, 500] 范围内。
0 <= Node.val <= 500
每个节点的值都是 独一无二 的。

注意：本题与力扣 1123 重复：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves
"""
from myTreeNode import *

"""
类似：236.二叉树的最近公共祖先.py
题目要求找到具有所有最深节点的最小子树。我们可以使用深度优先搜索（DFS）来解决这个问题。
1.首先，我们需要计算二叉树的深度。
  可以通过递归的方式来计算每个节点的深度。
2.然后，我们可以找到具有最大深度的节点。
  具有最大深度的节点可以是一个或多个。
3.接下来，我们需要找到包含所有具有最大深度的节点的子树。
  我们可以使用递归的方式来查找这样的子树。从根节点开始，我们遍历左子树和右子树，并找到具有最大深度的节点。
  1)如果左子树和右子树的最大深度相等，并且根节点本身是一个最深节点，那么根节点就是我们要找的子树的根节点。
  2)否则，我们将递归地在具有最大深度的子树中继续查找。
"""


# 方法1：先做一次深度优先搜索标记所有节点的深度，再做一次深度优先搜索找到最终答案。
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs_depth(root) -> int:
            if not root:
                return 0
            left_depth = dfs_depth(root.left)
            right_depth = dfs_depth(root.right)
            return max(left_depth, right_depth) + 1

        maxDepth = dfs_depth(root)

        def dfs_findSubtree(root, curDepth):
            if not root:
                return None
            # 前序位置：找到最大深度节点，并直接返回
            if curDepth == maxDepth:
                return root
            left_node = dfs_findSubtree(root.left, curDepth + 1)
            right_node = dfs_findSubtree(root.right, curDepth + 1)

            # 后续位置：根据dfs返回值判断具有最深节点的最小子树
            # 236.二叉树的最近公共祖先.py
            if left_node and right_node:
                return root
            if left_node:
                return left_node
            if right_node:
                return right_node

        return dfs_findSubtree(root, 1)


# 方法2：自底向上
"""
把每棵子树都看成是一个「子问题」，即对于每棵子树，我们需要知道：

这棵子树最深叶结点的深度。这里是指叶子在这棵子树内的深度，而不是在整棵二叉树的视角下的深度。相当于这棵子树的高度。
这棵子树的最深叶结点的最近公共祖先 lca。
"""


class Solution2:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        subtree = collections.namedtuple('subtree', ['node', 'depth'])

        def dfs_findSubtree(root) -> subtree:
            if not root:
                return None, 0

            L = dfs_findSubtree(root.left)
            R = dfs_findSubtree(root.right)
            # 左子树更高
            if L.depth > R.depth:
                return subtree(L.node, L.depth + 1)
            #
            if L.depth < R.depth:
                return subtree(R.node, R.depth + 1)
            if L.depth == R.depth:
                return subtree(root, L.depth + 1)

        return dfs_findSubtree(root).node


"""
1。递归这棵二叉树，同时维护全局最大深度 maxDepth。
2。在「递」的时候往下传 depth，用来表示当前节点的深度。
3。在「归」的时候往上传当前子树最深叶节点的深度。
4。设左子树最深叶节点的深度为 leftMaxDepth，右子树最深叶节点的深度为 rightMaxDepth。
  如果 leftMaxDepth=rightMaxDepth=maxDepth，那么更新答案为当前节点。
  注意这并不代表我们找到了答案，如果后面发现了更深的叶节点，那么答案还会更新

作者：灵茶山艾府
链接：https://leetcode.cn/problems/smallest-subtree-with-all-the-deepest-nodes/description/
"""


# 方法3：递归递归，有递有归
class Solution3:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = -1  # 全局最大深度

        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal ans, max_depth
            if node is None:
                max_depth = max(max_depth, depth)  # 维护全局最大深度
                return depth
            left_max_depth = dfs(node.left, depth + 1)  # 获取左子树最深叶节点的深度
            right_max_depth = dfs(node.right, depth + 1)  # 获取右子树最深叶节点的深度
            if left_max_depth == right_max_depth == max_depth:
                ans = node
            return max(left_max_depth, right_max_depth)  # 当前子树最深叶节点的深度

        dfs(root, 0)
        return ans


if __name__ == '__main__':
    root = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]  # [2,7,4]
    # root = [0, 1, 3, None, 2]  # [2]
    # root = [0, 1, 2, 3, None, None, 4]  # [0, 1, 2, 3, None, None, 4]
    node = buildTree(root)
    # print(Solution().subtreeWithAllDeepest(node))
    print(Solution2().subtreeWithAllDeepest(node))
