"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135005316?spm=1001.2014.3001.5501

OJ用例
题解 - 任务处理、可以处理的最大任务数 - Hydro

题目描述
在某个项目中有多个任务（用task数组表示）需要你进行处理，其中：

task[i] = [si, ei]
你可以在 si ≤ day ≤ ei 中的任意一天处理该任务，请返回你可以处理的最大任务数。

输入描述
第一行为任务数量 n

1 ≤ n ≤ 100000
后面 n 行表示各个任务的开始时间和终止时间，使用 si，ei 表示

1 ≤ si ≤ ei ≤ 100000
输出描述
输出为一个整数，表示可以处理的最大任务数。

用例1
输入
3
1 1
1 2
1 3
输出
3
"""

import heapq
# todo 考察区间相交, 后悔贪心 + 堆

# 输入
# 第一行为任务数量 n
# n = int(input())
# 后面 n 行表示各个任务的开始时间和终止时间，使用 si，ei 表示
# tasks = [list(map(int, input().split())) for _ in range(n)]

# 测试用例
n = 5
tasks = [[1, 1],
         [1, 3],
         [2, 2],
         [2, 4],
         [3, 3]
         ]

# 输出:为一个整数，表示可以处理的最大任务数。

# 任务先按照开始时间升序排列
tasks.sort(key=lambda x: (x[0]))

# minHeap记录任务结束时间ei
minHeap = []
# cur_time表示当前时间
cur_time = 0 
# ans可以处理的最大任务数
ans = 0

for si, ei in tasks:
    # 1.如果当前任务的开始时间 大于 当前时间，则这2个时间间隔可以处理minHeap中一些紧急任务
    while minHeap and si > cur_time:
        if heapq.heappop(minHeap) >= cur_time:
            # 如果前面任务有结束时间大于等于当前时间，则执行minHeap中结束时间最早的任务
            ans += 1
            cur_time += 1  # 一个时刻只执行一个任务

    # 2.如果当前任务的开始时间 小于等于 当前时间，先不处理这个任务，将该任务结束时间ei推入minHeap
    heapq.heappush(minHeap, ei)
    cur_time = si 

# 收尾处理, 重复之前逻辑
while minHeap:
    if heapq.heappop(minHeap) >= cur_time:
        ans += 1
        cur_time += 1

print(ans)


# 方法2: 优先级队列pq按照(si,ei)升序存储所有任务 =》部分测试用例超时
def main1():
    min_heap = []
    # 1. 先将所有任务按照(si,ei)优先级推入minHeap
    for si, ei in tasks:
        heapq.heappush(min_heap, (si, ei))

    cur_time = 0  # 标记当前开始日期，初始化为最小值
    ans = 0  # 记录最终结果，即处理的最大任务数
    
    # 2. 模拟每次可以优先处理的任务
    while min_heap:
        si, ei = heapq.heappop(min_heap)
        if si > cur_time:
            # 可以直接执行当前任务
            ans += 1
            cur_time = si
        elif si <= cur_time and ei > cur_time:
            # 重新加入优先队列排队
            heapq.heappush(min_heap, (cur_time+1, ei))

    print(ans)
