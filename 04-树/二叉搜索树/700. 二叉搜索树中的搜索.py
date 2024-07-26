"""
给定二叉搜索树（BST）的根节点 root 和一个整数值 value。
你需要在 BST 中找到节点值等于 value 的节点。 返回以该节点为根的子树。
如果节点不存在，则返回 null 。

示例 1:
        4
       / \
      2   7
     / \
    1   3
输入：root = [4,2,7,1,3], value = 2
输出：[2,1,3]

示例 2:
输入：root = [4,2,7,1,3], value = 5
输出：[]


提示：
数中节点数在 [1, 5000] 范围内
1 <= Node.value <= 10^7
root 是二叉搜索树
1 <= value <= 10^7
"""
from myTreeNode import *


# 方法1：递归查找  平均O(logN)
# 最坏情况下二叉搜索树是一条链，且要找的元素比链末尾的元素值还要小（大），这种情况下我们需要迭代 n 次。
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """在二叉搜索树中查找根节点值为val的子树，并返回该节点"""
        if not root:
            return None

        if root.val == val:
            return root  # 找到了，就直接返回该节点

        # 如果没找到，根据二叉树右边节点val总是大于左边节点的特点，判断该去左子树还是右子数查找
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)


# 方法2: 将方法1递归改为迭代写法  平均O(logN), 最差O(n)
def searchBST2(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    while root:
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
        else:
            root = root.right
    return None


if __name__ == '__main__':
    nums = [5, 3, 7, 2, None, 6, 8]
    '''
         5
        / \
       3   7
       /  / \
      2  6   8
    '''
    val = 0
    root = buildTree(nums)
    print(Solution().searchBST(root, val).val)
