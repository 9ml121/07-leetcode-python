"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/135050003?spm=1001.2014.3001.5502

OJ用例
题解 - 查找一个有向网络的头节点和尾节点 - Hydro

题目描述
给定一个有向图，图中可能包含有环，图使用二维矩阵表示，每一行的第一列表示起始节点，第二列表示终止节点，如 [0, 1] 表示从 0 到 1 的路径。

每个节点用正整数表示。

求这个数据的首节点与尾节点，题目给的用例会是一个首节点，但可能存在多个尾节点。同时图中可能含有环。如果图中含有环，返回 [-1]。

说明：入度为0是首节点，出度为0是尾节点。

image

输入描述
第一行为后续输入的键值对数量N（N ≥ 0）

第二行为2N个数字。每两个为一个起点，一个终点，如：

输出描述
输出一行头节点和尾节点。如果有多个尾节点，按从大到小的顺序输出。

备注
如果图有环，输出为 -1
所有输入均合法，不会出现不配对的数据
用例1
输入
4
0 1 0 2 1 2 2 3
输出
0 3
用例2
输入
2
0 1 0 2
输出
0 1 2
"""

# todo 考察拓扑排序，类似：F-图论/拓扑排序/207. 课程表.py
"""
了解拓扑排序后，我们就可以按照拓扑排序的思路不停剥离图中入度为0的点，每当剥离一个入度为0的点A，我们都需要做如下判断：
    A点如果没有后继点，则说明A点的出度为0，因此A点为尾节点
    A点如果有后继点，则A点的所有后继点的入度-1，如果后继点中-1后出现新的入度为0的节点，则加入度0点的队列，等待下次剥离
"""
import collections

# 输入
# 后续输入键值对数量
n = int(input())
# 2n个数组，起点-》终点
relations = list(map(int, input().split()))
# print(relations)

# 输出：一个头节点，多个尾节点（从大到小），有换输出-1
head = None
tails = []

in_degrees = collections.defaultdict(int)
out_degrees = collections.defaultdict(set)
for i in range(0, n*2, 2):
    u = relations[i]
    v = relations[i+1]
    in_degrees[v] += 1
    in_degrees[u] = in_degrees.get(u, 0)
    out_degrees[u].add(v)


def main():
    # dq保存入度节点变为0的节点
    dq = []
    # cnt记录已被剥去的点个数，如果图中存在环，则必然最终count < len(in_degrees)
    cnt = 0
    for u in in_degrees:
        if in_degrees[u] == 0:
            # 只有1个头节点
            dq.append(u)
            head = u
            break
    
    # bfs遍历找入度节点数为0的节点
    while dq:
        new_dq = []
        for u in dq:
            cnt += 1
            # 判断是否为尾节点
            if not out_degrees[u]:
                tails.append(u)
                continue

            for v in out_degrees[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    new_dq.append(v)

        dq = new_dq

    # 判断是否有环
    if cnt == len(in_degrees):
        tails.sort()  # 测试用例是从小到大
        tails.insert(0, head)
        return ' '.join(map(str, tails))
    else:
        return -1


print(main())
