from myTreeNode import *


# 方法3：二叉树后序遍历方法 =》进行序列化和反序列化
class Codec:
    res = []
    SEP = ','
    NONE = '#'

    def serialize(self, root: 'TreeNode') -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def traverse(root) -> None:
            if not root:
                self.res.append(self.NONE)
                return

            traverse(root.left)
            traverse(root.right)
            # 后序位置
            self.res.append(str(root.value))

        traverse(root)
        return self.SEP.join(self.res)

    def deserialize(self, data: str) -> 'TreeNode':
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodeVals = collections.deque(data.split(self.SEP))

        def traverse(nodeVals: collections.deque):
            if not nodeVals:
                return None

            # todo 后序遍历列表最右侧就是根节点val
            last = nodeVals.pop()
            if last == self.NONE:
                return None

            root = TreeNode(int(last))
            # 从后往前在 nodes 列表中取元素，一定要先构造 root.right 子树，后构造 root.left 子树。
            root.right = traverse(nodeVals)
            root.left = traverse(nodeVals)

            return root

        return traverse(nodeVals)


if __name__ == '__main__':
    # root = [1, 2, 3, None, None, 4, 5]
    root = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    # root = []
    root = buildTree(root)
    serialize = Codec().serialize(root)
    print(serialize)

    deserialize = Codec().deserialize(serialize)
    print(levelOrder2(deserialize))
