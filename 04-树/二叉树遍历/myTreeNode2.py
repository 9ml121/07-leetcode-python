"""
列表转化为二叉树
已知列表nums，将其转化为二叉树。举例：
nums = [3,9,20,None,None,15,7]，转化为二叉树后:

节点3的左子节点9，右子节点20，9的左右子节点都为None，20的左子节点15，右子节点7，参考下面：
        3
       / \
      9   20
          / \
         15  7

nums = [1,2,3,4,None,5,6,None,None,None, 7]
        1
      /   \
     2     3
    /     / \
   4     5   6
          \
           7

nums = [1,null,3,2,4,null,null,null,5]
   1
    \
     3
    / \
   2   4
        \
         5

nums = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
         1
        / \
       1   1
        \
         1
        / \
       1   1
        \
         1
todo LeetCode 序列化二叉树的格式
https://support.leetcode.cn/hc/kb/article/1567641/

1.输入标准格式为 [] 或 [值1,值2,值3,值4,值5,……]。
 - 若只输入[]则代表输入的测试用例是一棵空二叉树。
 - 若按[值1,值2,值3,值4,值5,……]格式输入，则“值 1”代表的是这棵二叉树的根节点，
    且从“值 1”开始一直到最后的数，依次是 水平顺序 遍历二叉树的各个节点的值，
 - 函数入参是已经构建完成的二叉树的根节点。

2. 若二叉树 非空节点 的某个子节点为空，则用None 表示
特殊层序遍历会遍历有值节点的 None 子节点，末尾连续输入的若干空节点会被去除。
"""
import collections
from typing import List, Optional


# 二叉树对象
class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val}, {self.left}, {self.right})"


# 将数组列表反序列化为TreeNode对象
def buildTree(values: List[int]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    dq = collections.deque([root])

    idx = 1  # idx变量记录正在序列化的节点在数组中的位置
    while idx < len(values):
        node = dq.popleft()
        # 1.为父节点构造左侧子节点
        leftVal = values[idx]
        if leftVal is not None:
            node.left = TreeNode(leftVal)
            dq.append(node.left)
        idx += 1
        # 2.为父节点构造右侧子节点
        if idx < len(values):
            rightVal = values[idx]
            if rightVal is not None:
                node.right = TreeNode(rightVal)
                dq.append(node.right)
        idx += 1

    return root


if __name__ == '__main__':
    # 创建二叉树
    nums = [1, 2, 3, 4, None, 5, 6, None, None, None, 7]
    # nums = [3, 9, 20, None, None, 15, 7]
    # nums = [1, None, 3, 2, 4, None, None, None, 5]
    # nums = [1, 1, 1, None, 1, None, None, 1, 1, None, 1]
    print(buildTree(nums))
