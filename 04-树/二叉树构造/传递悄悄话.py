"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134658206?spm=1001.2014.3001.5502

题目描述
给定一个二叉树，每个节点上站一个人，节点数字表示父节点到该节点传递悄悄话需要花费的时间。

初始时，根节点所在位置的人有一个悄悄话想要传递给其他人，求二叉树所有节点上的人都接收到悄悄话花费的时间。

输入描述
给定二叉树

0 9 20 -1 -1 15 7 -1 -1 -1 -1 3 2

注：-1表示空节点

image

输出描述
返回所有节点都接收到悄悄话花费的时间

38

用例1
输入
0 9 20 -1 -1 15 7 -1 -1 -1 -1 3 2
输出
38
"""

import collections
# 获取输入
times = list(map(int, input().split()))

# 解法1:(推荐)
def solution():
    maxTime = 0
    dq = collections.deque([(0, times[0])])  # (数组索引，到达节点时间)  
    n = len(times)
    while dq:
        sz = len(dq)
        for _ in range(sz):
            i, time = dq.popleft()
            left = 2*i + 1
            right = 2*i + 2
            left_exist = left < n and times[left] != -1
            right_exist = right < n and times[right] != -1

            if left_exist:
                dq.append((left, time + times[left]))
            if right_exist:
                dq.append((right, time + times[right]))

            # 叶子节点
            if not left_exist and not right_exist:
                maxTime = max(maxTime, time)

    return maxTime

print(solution())

# 解法2
# 二叉树构建(层序遍历)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.time = val


# 处理输入
vals = list(map(int, input().split()))
root = Node(vals[0])
n = len(vals)

dq = collections.deque([(0, root)])
ans = 0
while dq:
    i, node = dq.popleft()
    l = 2*i + 1
    r = 2*i + 2
    if l < n and vals[l] != -1:
        l_node = Node(vals[l])
        l_node.time = node.time + vals[l]
        node.left = l_node
        dq.append((l, l_node))
    if r < n and vals[r] != -1:
        r_node = Node(vals[r])
        r_node.time = node.time + vals[r]
        node.right = r_node
        dq.append((r, r_node))
    # 叶子节点
    if l >= n or (r < n and vals[l] == vals[r] == -1):
        ans = max(ans, node.time)

print(ans)
