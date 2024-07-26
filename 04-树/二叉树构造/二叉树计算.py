"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134607772

题目描述
给出一个二叉树如下图所示：

image

请由该二叉树生成一个新的二叉树，它满足其树中的每个节点将包含原始树中的左子树和右子树的和。

image

左子树表示该节点左侧叶子节点为根节点的一颗新树；右子树表示该节点右侧叶子节点为根节点的一颗新树。

输入描述
2行整数，第1行表示二叉树的中序遍历，第2行表示二叉树的前序遍历，以空格分割

例如：

7 -2 6 6 9

6 7 -2 9 6

输出描述
1行整数，表示求和树的中序遍历，以空格分割

例如：

-2 0 20 0 6

用例1
输入
-3 12 6 8 9 -10 -7
8 12 -3 6 -10 9 -7
输出
0 3 0 7 0 2 0
"""

import collections

# 获取输入
mid_order = list(map(int, input().split()))
pre_order = list(map(int, input().split()))

# 解法
# 根据前序和中序遍历结果构建二叉树（节点值有重复）
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.subSum = 0


# 中序遍历节点值对应的索引数组
val2idx = collections.defaultdict(list)
for i, val in enumerate(mid_order):
    val2idx[val].append(i)
# print(val2idx)


def build_tree(preL, preR, midL, midR):
    if preL > preR:
        return None

    # 前序遍历：根，左，右
    # 中序遍历：左，根，右
    root_val = pre_order[preL]
    root = Node(root_val)

    # 在中序遍历序列中，找到对应根值的位置，这个位置可能有多个，但是只有一个是正确的
    for idx in val2idx[root_val]:
        # 如果对应根值位置越界，则不是正确的
        if idx < midL:
            continue

        left_sz = idx - midL
        midL_vals_set = set(mid_order[midL:idx])
        preL_vals_set = set(pre_order[preL+1: preL+1+left_sz])
        # 如果中序的左子树，和前序的左子树不同，则对应根值位置不正确
        if midL_vals_set != preL_vals_set:
            continue

        # 找到正确根值位置后，开始分治递归处理左子树和右子树
        # print(mid_order[midL:idx])
        root.left = build_tree(preL+1, preL+left_sz, midL, idx-1)
        root.right = build_tree(preL+left_sz+1, preR, idx+1, midR)
        root.subSum += (root.left.val +
                        root.left.subSum) if root.left else 0
        root.subSum += (root.right.val +
                        root.right.subSum) if root.right else 0
        break

    return root


root = build_tree(0, len(pre_order)-1, 0, len(mid_order)-1)
ans = []


def get_mid_order(root):
    global ans
    if not root:
        return

    get_mid_order(root.left)
    ans.append(root.subSum)
    get_mid_order(root.right)


get_mid_order(root)
print(' '.join(map(str, ans)))
