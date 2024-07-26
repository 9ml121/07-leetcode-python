"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：
1.节点的左子树只包含 小于 当前节点的数。
2.节点的右子树只包含 大于 当前节点的数。
3.所有左子树和右子树自身必须也是二叉搜索树。


示例 1：
输入：root = [2,1,3]
输出：true

示例 2：
      5
     / \
    1   4
       / \
      3  6
输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。

示例：!!!
        5
       / \
      4   6
         / \
        3   7
输入：root = [5, 4, 6, None, None, 3, 7]
输出：false
解释：BST 的每个节点应该要小于右边子树的所有节点，节点5有一个右节点为3，是不满足BST定义的

       5
       / \
      4   7
         / \
        6   8
提示：
树中节点数目范围在[1, 10^4] 内
-2^31 <= Node.value <= 2^31 - 1
"""
from math import inf
from typing import Tuple
from myTreeNode import *

'''
总结：来自《灵茶山艾府》
1。前序遍历在某些数据下不需要递归到边界（base case）就能返回，而另外两种需要递归到至少一个边界，从这个角度上来说它是最快的。
2。中序遍历很好地利用到了二叉搜索树的性质，使用到的变量最少。
3。后序遍历的思想是最通用的，即自底向上计算子问题的过程。想要学好动态规划的话，请务必掌握这个思想。
'''


class Solution:
    # todo 方法1：中序遍历解法: 中序遍历以后得到的序列一定是升序序列(最好理解！)
    pre = -inf  # 代表中序遍历的上一个节点val

    def isValidBST1(self, root: Optional[TreeNode]) -> bool:
        """验证二叉搜索树:
        1.中序遍历时，判断当前节点是否大于中序遍历的前一个节点，如果大于，说明满足 BST，继续遍历；
        2.否则直接返回 false。
        """
        # 递归的边界条件判断: 空节点属于BST
        if not root:
            return True

        # 遍历左子树: 如果左子树不满足BST, 返回False， 后面代码不执行
        if not self.isValidBST1(root.left):
            return False

        # 中序位置: 如果当前节点值不大于中序遍历的上一个节点值，返回False，后面代码不执行
        if root.val <= self.pre:
            return False
        self.pre = root.val

        # 遍历右子树:
        return self.isValidBST1(root.right)

    # 方法2：中序遍历解法：栈实现(本质是模拟递归调用系统栈的过程)
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        stack = []  # 栈用来压入遍历过的节点对象
        preVal = float('-inf')  # preVal代表上一次访问的节点val

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个节点val，说明不是二叉搜索树
            if root.val <= preVal:
                return False

            preVal = root.val
            root = root.right
        return True  # 前面校验全部通过，返回True

    # 方法3：前序遍历：todo 增加函数参数列表，在参数中携带额外信息，将这种约束传递给子树的所有节点
    def isValidBST3(self, root: Optional[TreeNode], minVal=- float('inf'), maxVal=float('inf')) -> bool:
        # base case
        if not root:
            return True
        # 若 root.value 不符合 max 和 min 的限制，说明不是合法 BST
        curVal = root.val
        if curVal <= minVal or curVal >= maxVal:
            return False

        # 限定左子树的最大值是 root.value，右子树的最小值是 root.value
        if not self.isValidBST3(root.left, minVal, curVal):
            return False
        if not self.isValidBST3(root.right, curVal, maxVal):
            return False
        return True

    # 方法4：todo 后序遍历：自底向上(没有理解！！！)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> Tuple:
            # 返回的元祖两个值分别代表什么？
            if node is None:
                return inf, -inf

            l_min, l_max = dfs(node.left)
            r_min, r_max = dfs(node.right)

            # 后续遍历位置：
            x = node.val
            # 也可以在递归完左子树之后立刻判断，如果不是二叉搜索树，就不用递归右子树了
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)

        return dfs(root)[1] != inf


if __name__ == '__main__':
    # root = [5, 1, 4, None, None, 3, 6]  # False
    root = [5, 4, 6, None, None, 3, 7]  # False
    # root = [5, 4, 7, None, None, 6, 8]  # True
    node = buildTree(root)
    print(Solution().isValidBST3(node))
