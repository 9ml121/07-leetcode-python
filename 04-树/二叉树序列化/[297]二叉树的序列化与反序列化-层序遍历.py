"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，
同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。

这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示:
输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。
你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

示例 1：


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

树中结点数在范围 [0, 104] 内
-1000 <= Node.value <= 1000
"""

from myTreeNode import *


# 方法1：二叉树层序遍历方法进行序列化和反序列化
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''

        res = []
        queues = collections.deque([root])
        while queues:  # 将any是为了res只添加二叉树最后一层至少有一个节点不为空
            # size = len(queues)
            # for _ in range(size):
            node = queues.popleft()
            # 对空指针的检验从「将元素加入队列」的时候改成了「从队列取出元素」的时候。
            # 1。当前节点不为空: queues只添加不为空的node左右子节点，res记录节点val
            if node:
                res.append(str(node.val))
                queues.append(node.left)
                queues.append(node.right)
            # 2。当前节点为空，并且队列里面至少有一个节点不为空: queues不添加空节点,res记录None值
            elif not node and any(queues):
                res.append('None')
                continue
            # 3.queues里面全是空值，打破循环
            else:
                break

        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        nodeVals = data.split(',')
        rootVal = int(nodeVals[0])
        root = TreeNode(rootVal)
        queues = collections.deque([root])

        idx = 1  # idx变量记录正在序列化的节点在数组中的位置
        while queues and idx < len(nodeVals):
            # size = len(queues)
            # for _ in range(size):
            parent = queues.popleft()
            # 为父节点构造左侧子节点
            leftVal = nodeVals[idx]
            if leftVal != 'None':
                parent.left = TreeNode(int(leftVal))
                queues.append(parent.left)
            else:
                parent.left = None
                # 空节点不加入queues
            idx += 1

            if idx < len(nodeVals):
                # 为父节点构造右侧子节点
                rightVal = nodeVals[idx]
                if rightVal != 'None':
                    parent.right = TreeNode(int(rightVal))
                    queues.append(parent.right)
                else:
                    parent.right = None
                    # 空节点不加入queues
                idx += 1

        return root


if __name__ == '__main__':
    # root = [1, 2, 3, None, None, 4, 5]
    root = [1, 2, 3, 4, None, 2, 4, None, None, 4]
    root = buildTree(root)
    serialize = Codec().serialize(root)
    print(serialize)

    deserialize = Codec().deserialize(serialize)
    print(levelOrder(deserialize))
