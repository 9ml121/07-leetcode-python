"""
给定一个不重复的整数数组 nums 。 最大二叉树 可以用下面的算法从 nums 递归地构建:

1.创建一个根节点，其值为 nums 中的最大值。
2.递归地在最大值 左边 的 子数组前缀上 构建左子树。
3.递归地在最大值 右边 的 子数组后缀上 构建右子树。
返回 nums 构建的 最大二叉树 。

示例 1：


输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]
解释：递归调用如下所示：
- [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。

示例 2：


输入：nums = [3,2,1]
输出：[3,null,2,null,1]
提示：

1 <= nums.n <= 1000
0 <= nums[i] <= 1000
nums 中的所有整数 互不相同
"""
from typing import List, Optional

from myTreeNode2 import TreeNode
import myTreeNode2


def constructMaximumBinaryTree(nums: List[int]) -> Optional[TreeNode]:
    # 1.创建一个根节点，其值为 nums 中的最大值。
    # 2.递归地在最大值 左边 的 子数组前缀上 构建左子树。
    # 3.递归地在最大值 右边 的 子数组后缀上 构建右子树。
    if not nums:
        return None

    if len(nums) == 1:
        return TreeNode(nums[0])
    # 找到数组中的最大值及其索引
    maxV = max(nums)
    idx = nums.index(maxV)

    # 1.以最大值构造根节点
    root = TreeNode(maxV)

    # 2.递归地在最大值 左边 的 子数组前缀上 构建左子树。
    left = nums[0:idx]
    right = nums[idx + 1:]
    root.left = constructMaximumBinaryTree(left)
    # 3.递归地在最大值 右边 的 子数组后缀上 构建右子树
    root.right = constructMaximumBinaryTree(right)

    return root


if __name__ == '__main__':
    nums = [3, 2, 1, 6, 0, 5]
    root = constructMaximumBinaryTree(nums)
    print(myTreeNode.levelOrder(root))
    print(myTreeNode.levelOrder2(root))