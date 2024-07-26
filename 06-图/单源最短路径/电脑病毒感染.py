"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134386911

题目描述
一个局域网内有很多台电脑，分别标注为 0 ~ N-1 的数字。相连接的电脑距离不一样，所以感染时间不一样，感染时间用 t 表示。

其中网络内一台电脑被病毒感染，求其感染网络内所有的电脑最少需要多长时间。如果最后有电脑不会感染，则返回-1。

给定一个数组 times 表示一台电脑把相邻电脑感染所用的时间。

如图：path[i] = {i, j, t} 表示：电脑 i->j，电脑 i 上的病毒感染 j，需要时间 t。

输入描述
4
3
2 1 1
2 3 1
3 4 1
2
输出描述
2
用例1
输入
4
3
2 1 1
2 3 1
3 4 1
2
输出
2
说明
第一个参数：局域网内电脑个数N，1 ≤ N ≤ 200；

第二个参数：总共多少条网络连接

第三个 2 1 1 表示2->1时间为1

第六行：表示病毒最开始所在电脑号2
"""

import collections
import heapq

# 单源最短路径（有向图）
n = int(input())
line_sz = int(input())
lines = [list(map(int, input().split())) for _ in range(line_sz)]
# print(lines)
start = int(input())

# 解法
# 1.构建连接图
graph = collections.defaultdict(list)
for u, v, w in lines:
    graph[u].append((w, v))

# 2.初始化到达节点i的最短路径数组(注意：按照示例是从1到n)
dist = [float('inf')] * (n+1)
dist[start] = 0

# 3.优先队列实现bfs
pq = [(dist[start], start)]
while pq:
    _, u = heapq.heappop(pq)
    for w, v in graph[u]:
        if w + dist[u] < dist[v]:
            dist[v] = w + dist[u]
            heapq.heappush(pq, (dist[v], v))

# 4.求其感染网络内所有的电脑最少需要多长时间
ans = max(dist[1:])
print(-1 if ans == float('inf') else ans)
