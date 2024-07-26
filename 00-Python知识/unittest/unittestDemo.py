# from myTreeNode import *
# from BSTIterator import BSTIterator


import unittest
from myTreeNode2 import *
from _173二叉搜索树迭代器 import BSTIterator


class TestBSTIterator(unittest.TestCase):
    def test_hasNext(self):
        root = TreeNode(1)
        bst = BSTIterator(root)
        self.assertTrue(bst.hasNext())
        bst.next()
        self.assertFalse(bst.hasNext())

    def test_next(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        bst = BSTIterator(root)
        self.assertEqual(bst.next(), 1)
        self.assertEqual(bst.next(), 2)
        self.assertEqual(bst.next(), 3)

    def test_empty_tree(self):
        bst = BSTIterator(None)
        self.assertFalse(bst.hasNext())
        # self.assertRaises(StopIteration, bst.next)

    def test_single_node(self):
        root = TreeNode(1)
        bst = BSTIterator(root)
        self.assertTrue(bst.hasNext())
        self.assertEqual(bst.next(), 1)
        self.assertFalse(bst.hasNext())

    def test_large_tree(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
        bst = BSTIterator(root)
        self.assertEqual(bst.next(), 1)
        self.assertEqual(bst.next(), 2)
        self.assertEqual(bst.next(), 3)
        self.assertEqual(bst.next(), 4)
        self.assertEqual(bst.next(), 5)
        self.assertEqual(bst.next(), 6)
        self.assertEqual(bst.next(), 7)
        self.assertFalse(bst.hasNext())


if __name__ == '__main__':
    unittest.main()