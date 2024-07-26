"""
实现一个二叉搜索树迭代器类BSTIterator ，表示一个按 中序遍历 二叉搜索树（BST）的迭代器：
1.BSTIterator(TreeNode root)
    初始化 BSTIterator 类的一个对象。BST 的根节点 root 会作为构造函数的一部分给出。
    指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
2.boolean hasNext()
    如果向指针右侧遍历存在数字，则返回 true ；否则返回 false 。
3.int next()
    将指针向右移动，然后返回指针处的数字。

注意，指针初始化为一个不存在于 BST 中的数字，所以对 next() 的首次调用将返回 BST 中的最小元素。
你可以假设 next() 调用总是有效的，也就是说，当调用 next() 时，BST 的中序遍历中至少存在一个下一个数字。

示例：
        7
       / \
      3   15
         /  \
        9    20
输入:
    ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
输出:
    [null, 3, 7, true, 9, true, 15, true, 20, false]
解释:
    BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20])
    bSTIterator.next()    // 返回 3
    bSTIterator.next()    // 返回 7
    bSTIterator.hasNext() // 返回 True
    bSTIterator.next()    // 返回 9
    bSTIterator.hasNext() // 返回 True
    bSTIterator.next()    // 返回 15
    bSTIterator.hasNext() // 返回 True
    bSTIterator.next()    // 返回 20
    bSTIterator.hasNext() // 返回 False


提示：
树中节点的数目在范围 [1, 10^5] 内
0 <= Node.value <= 10^6
最多调用 10^5 次 hasNext 和 next 操作
"""
from myTreeNode import *


# 方法 1：利用stack迭代，模拟中序遍历
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.pushLeft(root)  # 先把根节点和左节点入栈

    def next(self) -> int:
        if len(self.stack) > 0:
            curr = self.stack.pop()
            self.pushLeft(curr.right)  # 维护栈顶元素
            return curr.value

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def pushLeft(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left


# 方法 2：遍历写法：中序遍历
class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []  # stack保存中序遍历的节点val
        self.inorder(root)  # 先用中序遍历扁平化所有节点
        self.idx = 0  # stack中下一个元素索引

    def next(self) -> int:
        if self.idx < len(self.stack):
            curr = self.stack[self.idx]
            self.idx += 1
            return curr

    def hasNext(self) -> bool:
        return self.idx < len(self.stack)

    def inorder(self, node) -> None:
        if not node:
            return
        self.inorder(node.left)
        self.stack.append(node.value)
        self.inorder(node.right)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
if __name__ == '__main__':
    arr = [7, 3, 15, None, None, 9, 20]
    root = buildTree(arr)
    bst = BSTIterator(root)
    print(bst.next())  # 返回 3
    print(bst.next())  # 返回 7
    print(bst.hasNext())  # 返回 True
    print(bst.next())  # 返回 9
    print(bst.hasNext())  # 返回 True
    print(bst.next())  # 返回 15
    print(bst.hasNext())  # 返回 True
    print(bst.next())  # 返回 20
    print(bst.hasNext())  # 返回 False
