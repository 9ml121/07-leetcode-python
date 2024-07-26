"""
题目描述
某银行将客户分为了若干个优先级， 1 级最高， 5 级最低，当你需要在银行办理业务时，优先级高的人随时可以插队到优先级低的人的前面。
现在给出一个人员到来和银行办理业务的时间序列，请你在每次银行办理业务时输出客户的编号。
如果同时有多位优先级相同且最高的客户，则按照先来后到的顺序办理。

输入描述
输入第一行是一个正整数 n ,表示输入的序列中的事件数量。(1 ≤ n ≤ 500)
接下来有 n 行，每行第一个字符为 a 或 p 。
当字符为 a 时，后面会有两个的正整数 num 和 x ,表示到来的客户编号为 num ,优先级为 x ;
当字符为 p 时，表示当前优先级最高的客户去办理业务。

输出描述
输出包含若干行，对于每个 p ， 输出一行，仅包含一个正整数 num , 表示办理业务的客户编号。

用例
输入	
4
a 1 3
a 2 2
a 3 2
p
输出	2
说明	无
"""
from queue import PriorityQueue
import heapq


# 输入
# n = int(input())
# items = [input().split() for _ in range(n)]

# 测试数据
n = 4
items = [['a', '1', '3'], ['a', '2', '2'], ['a', '3', '2'], ['p']]

# 输出：对于每个 p ， 输出一行，仅包含一个正整数 num , 表示办理业务的客户编号
# 小根堆存储（优先级，客户编号）
# 优先级：1 级最高， 5 级最低，如果同时有多位优先级相同且最高的客户，则按照先来后到的顺序办理
minHeap = []

for i, item in enumerate(items):
    if item[0] == 'a':
        num = item[1] # 客户编号
        x = item[2]   # 优先级
        heapq.heappush(minHeap, (x, num))
    elif item[0] == 'p':
        _, cid = heapq.heappop(minHeap)
        print(cid)


