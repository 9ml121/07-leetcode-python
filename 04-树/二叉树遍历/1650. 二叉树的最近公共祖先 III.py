"""
给定一棵二叉树中的两个节点 p 和 q，返回它们的最近公共祖先节点（LCA）。

每个节点都包含其父节点的引用（指针）。Node 的定义如下：
class Node {
    public int value;
    public Node left;
    public Node right;
    public Node parent;
}

根据维基百科中对最近公共祖先节点的定义：
“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是后代节点中既包括 p 又包括 q 的最深节点（我们允许一个节点为自身的一个后代节点）”。
一个节点 x 的后代节点是节点 x 到某一叶节点间的路径中的节点 y。



示例 1:
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和 1 的最近公共祖先是 3。

示例 2:
            3
          /   \
         5     1
        / \   / \
       6   2 0   8
          / \
         7   4

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和 4 的最近公共祖先是 5，根据定义，一个节点可以是自身的最近公共祖先。

示例 3:
输入: root = [1,2], p = 1, q = 2
输出: 1


提示:
树中节点个数的范围是 [2, 105]。
-109 <= Node.value <= 109
所有的 Node.value 都是互不相同的。
p != q
p 和 q 存在于树中。
"""
import unittest


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


"""
给定一棵二叉树中的两个节点 p 和 q，返回它们的最近公共祖先节点（LCA）。
每个节点都包含其父节点的引用（指针）。
函数参数不含根节点！！！

这道题其实不是公共祖先的问题，而是单链表相交的问题，你把 parent 指针想象成单链表的 next 指针，题目就变成了：
给你输入两个单链表的头结点 p 和 q，这两个单链表必然会相交，请你返回相交点。
力扣160. 相交链表.py
"""


# 1650. 二叉树的最近公共祖先 III
# 方法 1：对两个链表分别拼接另外一个链表，让长度保持一致，然后判断相交点(推荐)
#         headA  1->2->3->4->5->n->1->4
#         headB  1->4->5->n->1->2->3->4
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # 施展链表双指针技巧
        a, b = p, q
        while a != b:
            # a 走一步，如果走到根节点，转到 q 节点
            a = a.parent if a else q
            # b 走一步，如果走到根节点，转到 p 节点
            b = b.parent if b else p
        # 最后2个节点的相遇点，就是2个节点的公共祖先
        return a


class TestSolution(unittest.TestCase):
    def test_lowestCommonAncestor_positive(self):
        # 构建二叉树
        root = Node(3)
        root.left = Node(5)
        root.right = Node(1)
        root.left.parent = root
        root.right.parent = root
        root.left.left = Node(6)
        root.left.right = Node(2)
        root.left.left.parent = root.left
        root.left.right.parent = root.left
        root.right.left = Node(0)
        root.right.right = Node(8)
        root.right.left.parent = root.right
        root.right.right.parent = root.right
        root.left.right.left = Node(7)
        root.left.right.right = Node(4)
        root.left.right.left.parent = root.left.right
        root.left.right.right.parent = root.left.right
        # 测试
        p = root.left
        # q = root.right
        # expected_output = root
        q = root.left.right.right
        expected_output = p
        self.assertEqual(Solution().lowestCommonAncestor(p, q), expected_output)

    def test_lowestCommonAncestor_negative(self):
        # 构建二叉树
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.parent = root
        root.right.parent = root
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.left.left.parent = root.left
        root.left.right.parent = root.left
        # 测试
        p = root.left
        q = Node(6)
        expected_output = None
        self.assertEqual(Solution().lowestCommonAncestor(p, q), expected_output)


if __name__ == '__main__':
    unittest.main()
