from myTreeNode2 import *
from _173二叉搜索树迭代器 import BSTIterator


class TestBSTIterator:
    def test_next_positive(self):
        root = TreeNode(7)
        root.left = TreeNode(3)
        root.right = TreeNode(15)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(20)
        bst_iter = BSTIterator(root)
        assert bst_iter.next() == 3
        assert bst_iter.next() == 7
        assert bst_iter.hasNext() == True
        assert bst_iter.next() == 9
        assert bst_iter.next() == 15
        assert bst_iter.next() == 20
        assert bst_iter.hasNext() == False

    def test_next_empty(self):
        bst_iter = BSTIterator(None)
        assert bst_iter.next() == None
        assert bst_iter.hasNext() == False
