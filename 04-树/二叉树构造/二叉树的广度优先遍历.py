"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/128192362

OJ用例
题解 - 二叉树的广度优先遍历 - Hydro

题目描述
有一棵二叉树，每个节点由一个大写字母标识(最多26个节点）。

现有两组字母，分别表示后序遍历（左孩子->右孩子->父节点）和中序遍历（左孩子->父节点->右孩子）的结果，请你输出层序遍历的结果。

输入描述
每个输入文件一行，第一个字符串表示后序遍历结果，第二个字符串表示中序遍历结果。（每串只包含大写字母）

中间用单空格分隔。

输出描述
输出仅一行，表示层序遍历的结果，结尾换行。

用例1
输入
CBEFDA CBAEDF
输出
ABDCEF
说明
二叉树为：

image


"""

import collections
# 输入后续遍历，中序遍历
post, mid = input().split()

# 输出：层序遍历结果
ans = []

# 1.根据后续和中序遍历结果，分解二叉树的根节点和下一个层级左右子树在后续和中序遍历数组中的索引位置
def build(post_i, post_j, mid_i, mid_j):
    # 后序遍历（左孩子->右孩子->父节点）
    root_val = post[post_j]
    ans.append(root_val)

    # 中序遍历（左孩子->父节点->右孩子）
    root_idx = mid.index(root_val)
    left_sz = root_idx - mid_i
    right_sz = mid_j - root_idx

    # 左子树
    if left_sz > 0:
        q.append([post_i, post_i + left_sz - 1,  mid_i, root_idx-1])
    # 右子树
    if right_sz > 0:
        q.append([post_i + left_sz, post_j - 1,  root_idx+1, mid_j])

# q保存下一个层级左右子树在后续和中序遍历数组中的索引位置
n = len(post)
q = collections.deque([[0, n-1, 0, n-1]])
# 2. bfs获取层序遍历结果
while q:
    post_i, post_j, mid_i, mid_j = q.popleft()
    build(post_i, post_j, mid_i, mid_j)
    
print(''.join(ans))
