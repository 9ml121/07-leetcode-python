"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134719131?spm=1001.2014.3001.5502

OJ用例
https://hydro.ac/d/HWOD2023/p/OD359/solution

题目描述
现有N个任务需要处理，同一时间只能处理一个任务，处理每个任务所需要的时间固定为1。

每个任务都有最晚处理时间限制和积分值，在最晚处理时间点之前处理完成任务才可获得对应的积分奖励。

可用于处理任务的时间有限，请问在有限的时间内，可获得的最多积分。

输入描述
第一行为一个数 N，表示有 N 个任务
1 ≤ N ≤ 100

第二行为一个数 T，表示可用于处理任务的时间
1 ≤ T ≤ 100
接下来 N 行，每行两个空格分隔的整数（SLA 和 V），SLA 表示任务的最晚处理时间，V 表示任务对应的积分。

1 ≤ SLA ≤ 100
0 ≤ V ≤ 100000
输出描述
可获得的最多积分

用例1
输入
4
3
1 2
1 3
1 4
1 5
输出
5
说明
虽然有3个单位的时间用于处理任务，可是所有任务在时刻1之后都无效。 所以在第1个时间单位内，选择处理有5个积分的任务。1-3时无任务处理。

用例2
输入
4
3
1 2
1 3
1 4
3 5
输出
9
说明
第1个时间单位内，处理任务3，获得4个积分

第2个时间单位内，处理任务4，获得5个积分

第3个时间单位内，无任务可处理

共获得9个积分
"""

# todo 考察后悔贪心 + 优先队列
# 获取输入
# 第一行为一个数 N，表示有 N 个任务
import heapq


n = int(input())
# 第二行为一个数 T，表示可用于处理任务的时间
t = int(input())
# 接下来 N 行，每行两个空格分隔的整数（SLA 和 V），SLA 表示任务的最晚处理时间，V 表示任务对应的积分。
items = [list(map(int, input().split())) for _ in range(n)]
# print(items)

# 方法1: 数据量不大，1 ≤ N ≤ 100，暴力双循环
def main1():
    items.sort(key=lambda x: (-x[1], x[0]))
    # print(items)

    used = [False] * (t+1)
    cnt = 0
    ans = 0
    for sla, v in items:
        for i in range(min(sla, t), 0, -1):
            if not used[i]:
                used[i] = True
                ans += v
                break

    # print(used)
    print(ans)

# 方法2: 贪心(后悔)=》优先队列实现
# 类似题型：
# 07-优先队列&堆/贪心+堆/工单调度策略.py
# 07-优先队列&堆/贪心+堆/1705. 吃苹果的最大数目.py
# 07-优先队列&堆/贪心+堆/630. 课程表 III.py

def main():
    # 1. items按照sla升序排列
    items.sort(key=lambda x: x[0])
    # print(items)

    # 2.最小堆保存已完成任务的积分，如果后面遇到更大积分，替换掉堆中最小积分
    pq = []
    # 当前时间,初始化为0
    cur_time = 0
    for sla, v in items:
        # 如果sla在当前时间之后，先直接推入堆，如果后面遇到积分更大的，在代替掉
        if sla > cur_time:
            heapq.heappush(pq, v)
            cur_time += 1
        else:
            if v > pq[0]:
                # heapq.heappop(pq)
                # heapq.heappush(pq, v)
                heapq.heapreplace(pq, v)
            else:
                continue
        # print(pq)

    # 3.在时间t内可以获得的最大积分，就是堆中最大的t个数之和
    ans = heapq.nlargest(t, pq)
    return sum(ans)


print(main())
