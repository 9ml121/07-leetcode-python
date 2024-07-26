"""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。



示例 1:
     3
    / \
   2   3
    \   \
     3   1

输入: root = [3,2,3,null,3,null,1]
输出: 7
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7

示例 2:
     3
    / \
   4   5
  / \   \
 1   3   1

输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9


提示：
树的节点数在 [1, 10^4] 范围内
0 <= Node.val <= 10^4
"""

from typing import Optional

import myTreeNode
from myTreeNode import TreeNode

"""
问题描述：
给定一个二叉树，每个节点表示一个房屋，节点上的值表示该房屋中的钱。
相连的两个房屋不能同时被抢劫。求在不触发警报的情况下，能够抢劫的最大金额。

解题思路：
这个问题可以使用动态规划来解决。我们可以定义一个递归函数 rob(root)，它返回在以 root 为根节点的子树中能够抢劫的最大金额。

对于当前节点 root，我们有两个选择：抢劫当前节点和不抢劫当前节点。
1.如果我们抢劫了当前节点，那么我们不能抢劫其左右子节点。
2.如果我们不抢劫当前节点，那么我们可以选择抢劫其左右子节点。

因此，递归函数的定义如下：
rob(root) = max(root.val + rob(root.left.left) + rob(root.left.right) + rob(root.right.left) + rob(root.right.right),
                rob(root.left) + rob(root.right))
其中，
root.val 表示当前节点的值，
rob(root.left) 表示抢劫当前节点左子树能够获得的最大金额，
rob(root.right) 表示抢劫当前节点右子树能够获得的最大金额。

为了避免重复计算，我们可以使用一个哈希表来存储每个节点对应的最大金额，以便在需要时进行查找。
"""


# 方法1：dfs+memo
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def dfs(node):
            if not node:
                return 0

            if node in memo:
                return memo[node]

            rob_current = node.val
            if node.left:
                rob_current += dfs(node.left.left) + dfs(node.left.right)
            if node.right:
                rob_current += dfs(node.right.left) + dfs(node.right.right)

            rob_next = dfs(node.left) + dfs(node.right)

            res = max(rob_current, rob_next)
            memo[node] = res
            return res

        return dfs(root)


# 方法2：dp
"""
在动态规划的方法中，我们可以使用一个长度为 2 的数组来表示当前节点的状态，
其中 dp[0] 表示不抢劫当前节点的最大金额，dp[1] 表示抢劫当前节点的最大金额。

对于当前节点 root，我们可以根据其左右子节点的状态来更新当前节点的状态。具体地，
1.如果我们不抢劫当前节点，那么我们可以选择抢劫其左右子节点，因此当前节点的最大金额为左右子节点的最大金额之和。
2.如果我们抢劫当前节点，那么我们不能抢劫其左右子节点，因此当前节点的最大金额为当前节点的值加上不抢劫其左右子节点的最大金额。

根据上述思路，我们可以使用后序遍历的方式从底向上计算每个节点的状态，并不断更新最大金额。
最终，根节点的状态中的较大值就是能够抢劫的最大金额。
"""
class Solution2:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            # 不抢劫当前节点
            not_rob = max(left) + max(right)
            # 抢劫当前节点
            rob = node.val + left[0] + right[0]

            return [not_rob, rob]

        res = dfs(root)
        return max(res)


if __name__ == '__main__':
    root = [3, 2, 3, None, 3, None, 1]  # 7
    # root = [3, 4, 5, 1, 3, None, 1] # 9
    node = myTreeNode.insert(root)
    # print(node)
    print(Solution2().rob(node))
