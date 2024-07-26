"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

        3
       / \
      9  20
        / \
       15  7

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

提示：
树中节点数目在范围 [0, 2000] 内
-1000 <= Node.value <= 1000
"""
from myTreeNode import *

import collections


# 方法1：BFS(队列实现)迭代解法  => 自顶向下
def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """返回二叉树按照层序遍历的节点val: 队列实现"""
    if not root:
        return []

    res = []
    dq = collections.deque([root])
    # 1.从上往下遍历二叉树的每一层
    while dq:
        level_size = len(dq)
        curr_level = []
        # 2.从左到右遍历每一层的节点： 不需要记录level时可以去掉 for 循环
        for _ in range(level_size):
            node = dq.popleft()
            curr_level.append(node.val)
            # 3. 将下一层节点放入队列，注意：这2个if顺序不能换
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        # 4.记录每一层遍历结果
        res.append(curr_level)

    return res


# 方法2：按照层序遍历的递归解法 => 自顶向下，没有返回值
def levelOrder2(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res = []  # 全局结果变量

    def dfs(nodes=[root]) -> None:
        """从上往下递归遍历二叉树的同一高度节点列表，没有返回值"""
        if not nodes:  # 节点列表为空就不用再遍历了
            return

        path = []  # 用来存放遍历当前层的val
        nextLevelNodes = []  # 用来存放当前层的下一层节点对象
        # 先记录当前层遍历结果，同时把子节点加入下一次递归遍历列表中
        for node in nodes:
            path.append(node.value)
            if node.left:
                nextLevelNodes.append(node.left)
            if node.right:
                nextLevelNodes.append(node.right)
        # 记录每一层遍历结果
        res.append(path)
        # todo 优化：递归遍历下一层节点前，先判断是否已经到了最后一层
        if nextLevelNodes:
            dfs(nextLevelNodes)

    dfs()
    return res


if __name__ == '__main__':
    # values = [3, 9, 20, None, None, 15, 7]
    values = [1, 2, 3, 4, 5, 6, 7]
    root = buildTree(values)
    print(levelOrder(root))
