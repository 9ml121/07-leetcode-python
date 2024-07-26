"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134709517

题目描述
定义构造三叉搜索树规则如下：

每个节点都存有一个数，当插入一个新的数时，从根节点向下寻找，直到找到一个合适的空节点插入。查找的规则是：

如果数小于节点的数减去500，则将数插入节点的左子树
如果数大于节点的数加上500，则将数插入节点的右子树
否则，将数插入节点的中子树
给你一系列数，请按以上规则，按顺序将数插入树中，构建出一棵三叉搜索树，最后输出树的高度。

输入描述
第一行为一个数 N，表示有 N 个数，1 ≤ N ≤ 10000

第二行为 N 个空格分隔的整数，每个数的范围为[1,10000]

输出描述
输出树的高度（根节点的高度为1）

用例1
输入
5
5000 2000 5000 8000 1800
输出
3
说明
最终构造出的树如下，高度为3： image

用例2
输入
3
5000 4000 3000
输出
3
说明
最终构造出的树如下，高度为3： image

用例3
输入
9
5000 2000 5000 8000 1800 7500 4500 1400 8100
输出
4
说明
最终构造出的树如下，高度为4： image
"""


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.mid = None
        self.right = None
        self.height = 0


class Tree:
    def __init__(self) -> None:
        self.root = None
        self.height = 0

    def add(self, val):
        node = Node(val)

        if not self.root:
            #  构造根节点
            self.root = node
            self.height = 1
            node.height = 1
        else:
            cur = self.root
            while True:
                node.height = cur.height + 1
                self.height = max(self.height, node.height)

                if val < cur.val - 500:
                    if not cur.left:
                        cur.left = node
                        break
                    else:
                        cur = cur.left

                elif val > cur.val + 500:
                    if not cur.right:
                        cur.right = node
                        break
                    else:
                        cur = cur.right
                else:
                    if not cur.mid:
                        cur.mid = node
                        break
                    else:
                        cur = cur.mid


while True:
    try:
        n = int(input())
        vals = list(map(int, input().split()))
        tree = Tree()
        for val in vals:
            tree.add(val)
        print(tree.height)
    except:
        break
