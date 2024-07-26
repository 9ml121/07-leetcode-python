"""
给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。

如果存在多个答案，您可以返回其中 任何 一个。

示例 1：



输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]
示例 2:

输入: preorder = [1], postorder = [1]
输出: [1]
提示：

1 <= preorder.n <= 30
1 <= preorder[i] <= preorder.n
preorder 中所有值都 不同
postorder.n == preorder.n
1 <= postorder[i] <= postorder.n
postorder 中所有值都 不同
保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历
"""
from typing import List, Optional
from myTreeNode2 import TreeNode

"""
不同之处一 寻找当前根节点
这一部分总的来说是在寻找可以将左右子树划分开的根节点

前+后 首先我们可以显然知道当前根节点为pre[pre_start],并且它在后序中的位置为post_end，因此这里我们需要找到能区分左右子树的节点。 
    我们知道左子树的根节点为pre[pre_start+1]，因此只要找到它在后序中的位置就可以分开左右子树（index的含义）
前+中 首先我们可以显然知道当前根节点为pre[pre_start],只用找出它在中序中的位置，就可以把左右子树分开（index的含义）
中+后 首先我们可以显然知道当前根节点为post[post_end]，只用找出它在中序中的位置，就可以把左右子树分开（index的含义）
"""


# 方法1
def constructFromPrePost(preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    # 通过前序中序，或者后序中序遍历结果可以确定一棵原始二叉树，但是通过前序后序遍历结果无法确定原始二叉树
    # 如果存在多个答案，您可以返回其中 任何 一个
    # preorder = [1,2,3]  postOrder =[3,2,1] 有可能2，3都是左节点，也可能都是右节点val

    # 函数定义：根据preOrder闭区间索引[preStart...preEnd]
    # 和postOrder闭区间索引[postStart...postEnd],返回二叉树root对象
    def build(preStart, preEnd, postStart, postEnd):
        # 后续遍历: [左子树，右子树，root]
        # 前序遍历: [root, 左子树， 右子树]

        # base case
        if preStart > preEnd:
            return None
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        # 先构造出当前根节点
        root = TreeNode(rootVal)

        # 递归构造左右子树
        # root.left 的值是前序遍历第二个元素(如果root.left为空，那就是root.right)
        # 通过前序和后序遍历构造二叉树的关键在于通过左子树的根节点
        # 确定 preorder 和 postorder 中左右子树的元素区间
        leftRootVal = preorder[preStart + 1]
        # leftRootVal 在后序遍历数组中的索引
        idxOfPost = postorder.index(leftRootVal)
        # 左子树的元素个数
        leftSize = idxOfPost - postStart + 1

        # 根据左子树的根节点索引和元素个数推导左右子树的索引边界
        root.left = build(preStart + 1, preStart + leftSize,
                          postStart, idxOfPost)
        root.right = build(preStart + leftSize + 1, preEnd,
                           idxOfPost + 1, postEnd - 1)

        return root

    return build(0, len(preorder) - 1, 0, len(postorder) - 1)  # 闭区间


# 方法2；
# 方法1的另外一种写法
def constructFromPrePost2(self, pre, post):
    if not pre:
        return None
    root = TreeNode(pre[0])
    if len(pre) == 1:
        return root

    L = post.index(pre[1]) + 1
    root.left = self.constructFromPrePost(pre[1:L + 1], post[:L])
    root.right = self.constructFromPrePost(pre[L + 1:], post[L:-1])
    return root
