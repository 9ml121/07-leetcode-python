"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，
你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。


示例 1：
       1
      / \
     2   3
        / \
       4   5
输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

示例 2：
输入：root = []
输出：[]

示例 3：
输入：root = [1]
输出：[1]

示例 4：
输入：root = [1,2]
输出：[1,2]


提示：
树中结点数在范围 [0, 10^4] 内
-1000 <= Node.val <= 1000
"""

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
from myTreeNode import *


# 方法1：二叉树前序遍历方法 =》进行序列化和反序列化
# 注意：根据前序遍历结果可以反序列化为二叉树，前提是所有的空节点都需要标识出来
class Codec:
    res = []  # 遍历节点的存放列表
    SEP = ','  # 节点之间的分隔符
    NONE = '*'  # 空节点的代表符号

    def serialize(self, root: 'TreeNode') -> str:
        def traverse(root) -> None:
            if not root:
                self.res.append(self.NONE)
                return
            # 前置位置
            self.res.append(str(root.val))

            traverse(root.left)
            traverse(root.right)

        traverse(root)
        return self.SEP.join(self.res)

    def deserialize(self, data: str) -> 'TreeNode':
        if not data:
            return None
        nodeVals = collections.deque(data.split(self.SEP))

        def traverse(nodeVals: collections.deque):
            if not nodeVals:
                return None
            # todo 前序遍历列表最左则就是根节点val
            rootVal = nodeVals.popleft()
            if rootVal == self.NONE:
                return None

            root = TreeNode(int(rootVal))

            # 因为每个节点左右子树都在data中有标识，所有可以直接按照顺序递归构造
            root.left = traverse(nodeVals)
            root.right = traverse(nodeVals)

            return root

        return traverse(nodeVals)


if __name__ == '__main__':
    root = [1, 2, 3, None, None, 4, 5]
    # root = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    # root = []
    root = buildTree(root)
    serialize = Codec().serialize(root)
    print(serialize)

    deserialize = Codec().deserialize(serialize)
    print(levelOrder(deserialize))

