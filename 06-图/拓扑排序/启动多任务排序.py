"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135268369?spm=1001.2014.3001.5501

OJ用例
题解 - 启动多任务排序 - Hydro

题目描述
一个应用启动时，会有多个初始化任务需要执行，并且任务之间有依赖关系，例如A任务依赖B任务，那么必须在B任务执行完成之后，才能开始执行A任务。

现在给出多条任务依赖关系的规则，请输入任务的顺序执行序列，规则采用贪婪策略，即一个任务如果没有依赖的任务，则立刻开始执行，如果同时有多个任务要执行，则根据任务名称字母顺序排序。

例如：B任务依赖A任务，C任务依赖A任务，D任务依赖B任务和C任务，同时，D任务还依赖E任务。那么执行任务的顺序由先到后是：

A任务，E任务，B任务，C任务，D任务

这里A和E任务都是没有依赖的，立即执行。

输入描述
输入参数每个元素都表示任意两个任务之间的依赖关系，输入参数中符号"->"表示依赖方向，例如：

A->B：表示A依赖B

多个依赖之间用单个空格分隔

输出描述
输出排序后的启动任务列表，多个任务之间用单个空格分隔

用例1
输入
A->B C->B
输出
B A C
"""

"""
题目解析
todo 拓扑排序  参考：F-图论/拓扑排序/207. 课程表.py
本题没有说明循环依赖的情况该如何处理，因此我认为本题没有循环依赖的情况。实际考试需要注意下
"""


# 输入
# a->b: a依赖b
import collections
relations = list(map(lambda x: x.split('->'), input().split()))
print(relations)  # [['A', 'B'], ['C', 'B']]

# 输出：排序后的启动任务列表
ans = []

# 入度：统计每个节点的前置节点个数
in_degrees = collections.defaultdict(int)
# 出度：统计每个节点的后置节点集合
out_degrees = collections.defaultdict(set)

# 初始化入度和出度表
for a, b in relations:
    in_degrees[a] += 1
    in_degrees[b] = in_degrees.get(b, 0)
    out_degrees[b].add(a)

# dq保存入度节点个数为0的
dq = []
for task in in_degrees:
    if in_degrees[task] == 0:
        dq.append(task)

# bfs遍历找入度节点数为0的节点
while dq:
    dq.sort()
    new_dq = []
    for task in dq:
        # 结果列表依次添加入度节点为0的节点
        ans.append(task)
        for nxt in out_degrees[task]:
            in_degrees[nxt] -= 1
            if in_degrees[nxt] == 0:
                new_dq.append(nxt)
    dq = new_dq
print(' '.join(ans))
