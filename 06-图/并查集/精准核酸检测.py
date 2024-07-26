""" 
题目描述
为了达到新冠疫情精准防控的需要，为了避免全员核酸检测带来的浪费，需要精准圈定可能被感染的人群。

现在根据传染病流调以及大数据分析，得到了每个人之间在时间、空间上是否存在轨迹交叉。

现在给定一组确诊人员编号（X1,X2,X3,...,Xn），在所有人当中，找出哪些人需要进行核酸检测，输出需要进行核酸检测的人数。（注意：确诊病例自身不需要再做核酸检测）

需要进行核酸检测的人，是病毒传播链条上的所有人员，即有可能通过确诊病例所能传播到的所有人。

例如：A是确诊病例，A和B有接触、B和C有接触、C和D有接触、D和E有接触，那么B\C\D\E都是需要进行核酸检测的人。

输入描述
第一行为总人数 N

第二行为确认病例人员编号（确诊病例人员数量 < N），用逗号分割

第三行开始，为一个 N * N 的矩阵，表示每个人员之间是否有接触，0表示没有接触，1表示有接触。

输出描述
整数：需要做核酸检测的人数

备注
人员编号从0开始
0 < N < 100
用例
输入	
5
1,2
1,1,0,1,0
1,1,0,0,0
0,0,1,0,1
1,0,0,1,0
0,0,1,0,1
输出	3
说明	
编号为1、2号的人员，为确诊病例。

1号和0号有接触，0号和3号有接触。

2号和4号有接触。

所以，需要做核酸检测的人是0号、3号、4号，总计3人需要进行核酸检测。

4
0,3
1,0,0,0
0,1,1,0
0,1,1,1
0,0,1,1

6
3,4,5
1,0,0,1,1,0
0,1,0,0,0,1
0,0,1,0,1,1
1,0,0,1,0,1
1,0,1,0,1,1
0,1,1,1,1,1
"""

import collections
n = int(input())
confirmed = set(map(int, input().split(',')))
grid = []
for i in range(n):
    lines = list(map(int, input().split(',')))
    grid.append(lines)


# 方法1：bfs解法
def bfs():
    flags = [False] * n
    for idx in confirmed:
        flags[idx] = True

    cnt = 0
    dq = collections.deque(list(confirmed))
    while dq:
        i = dq.popleft()
        for j in range(n):
            if grid[i][j] == 1 and not flags[j]:
                flags[j] = True
                cnt += 1
                dq.append(j)
    return cnt
# print(bfs())

# 方法2：并查集
def unionFind():
    fa = list(range(n))

    def find(x):
        if x != fa[x]:
            fa[x] = find(fa[x])
        return fa[x]
    
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            # todo 这里尤其注意：是要讲x或者y的根节点的父节点指向另外一个节点的根节点
            fa[root_y] = root_x

    for i in range(n):
        for j in range(i+1, n):
            if grid[i][j] == 1:
                union(i, j)
    # print(fa)
    fa_confirmed = set()
    for i in confirmed:
        fa_confirmed.add(fa[i])

    cnt = 0
    for i in range(n):
        if fa[i] in fa_confirmed:
            cnt += 1

    return cnt - len(confirmed)
    

print(unionFind())