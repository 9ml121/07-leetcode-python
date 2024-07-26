"""
汽车从起点出发驶向目的地，该目的地位于出发位置东面 target 英里处。

沿途有加油站，用数组 stations 表示。其中 stations[i] = [positioni, fueli] 表示第 i 个加油站位于出发位置东面 positioni 英里处，并且有 fueli 升汽油。

假设汽车油箱的容量是无限的，其中最初有 startFuel 升燃料。它每行驶 1 英里就会用掉 1 升汽油。当汽车到达加油站时，它可能停下来加油，将所有汽油从加油站转移到汽车中。

为了到达目的地，汽车所必要的最低加油次数是多少？如果无法到达目的地，则返回 -1 。

注意：如果汽车到达加油站时剩余燃料为 0，它仍然可以在那里加油。如果汽车到达目的地时剩余燃料为 0，仍然认为它已经到达目的地。

 

示例 1：

输入：target = 1, startFuel = 1, stations = []
输出：0
解释：可以在不加油的情况下到达目的地。
示例 2：

输入：target = 100, startFuel = 1, stations = [[10,100]]
输出：-1
解释：无法抵达目的地，甚至无法到达第一个加油站。
示例 3：

输入：target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
输出：2
解释：
出发时有 10 升燃料。
开车来到距起点 10 英里处的加油站，消耗 10 升燃料。将汽油从 0 升加到 60 升。
然后，从 10 英里处的加油站开到 60 英里处的加油站（消耗 50 升燃料），
并将汽油从 10 升加到 50 升。然后开车抵达目的地。
沿途在两个加油站停靠，所以返回 2 。
 

提示：

1 <= target, startFuel <= 109
0 <= stations.length <= 500
1 <= positioni < positioni+1 < target
1 <= fueli < 109
"""

import heapq
from typing import List


# 方法1：贪心 + 堆（最大堆）
"""
思路
题目要求我们计算最低的加油次数，因此我们需要每次加油都尽可能加最多的油才能保证单次加油走的更远并且加油次数最少。

因此我们维护一个优先队列（最大堆），每次路过加油站先不加油，将加油站的油量放入最大堆中，
当油量不够走到下一个加油站时，我们选择加堆中最多的油（也就是堆顶元素），直到他能够走到下一个加油站或者目的地target；

当堆为空仍然无法到达时，表示无法到达目的地，返回-1，
否则返回加油的次数。
"""
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:  
        # 大顶堆：保存经过的加油站的油量
        maxHeap = []
        # cur_pos代表当前能走的最远距离, 初始化为startFuel
        cur_pos = startFuel
        # ans代表加油次数
        ans = 0
        # idx代表当前加油站索引
        idx = 0
        while cur_pos < target:
            # 把当前油量路程上的加油站情况都放进堆里面
            while idx < len(stations) and stations[idx][0] <= cur_pos:
                # 能走到的加油站,都加入大根堆
                heapq.heappush(maxHeap, -stations[idx][1])
                idx += 1

            # 加了上次最大油以后，有几种可能
            # 1. 能到->外层循环出,返回ans；
            if cur_pos < target:
                if not maxHeap:
                    # 2. 到不了,没油可加-> 不可能到达，返回-1；
                    return -1
                else:
                    # 3. 到不了,有油可以加->加最远路中没加的最大油(maxHeap)，结果+1，外层继续判断
                    cur_pos += - heapq.heappop(maxHeap)
                    ans += 1

        return ans

# 写法2
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # 大顶堆：保存经过的加油站的油量
        maxHeap = []
        # cur_pos代表当前能走的最远距离, 初始化为startFuel
        cur_pos = startFuel
        # ans代表加油次数
        ans = 0
        
        for pos, fuel in stations + [[target, 0]]:
            while cur_pos < pos:
                if not maxHeap:
                    return -1
                else:
                    cur_pos += -heapq.heappop(maxHeap)
                    ans += 1
            heapq.heappush(maxHeap, -fuel)
        
        return ans
        
# 方法2： 动态规划:时间复杂度比优先队列要高一点
"""
由于能否到达目的地是由油量决定的，我们可以维护一个dp,dp[i]表示加i次油可以走的最大路程,并且dp[i]是由dp[i-1]决定的。
初始时dp[0] = startFuel,表示不加油能走的最大路程
我们每次路过一个加油站就动态的更新dp[i](i <= 路过的加油站)，
然后遍历dp，找到第一个大于等于target的i即为答案，若不存在，返回-1。
"""


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        # dp[i]表示加i次油可以走的最大路程,并且dp[i]是由dp[i-1]决定的
        dp = [0] * (n+1)
        dp[0] = startFuel
        
        # 遍历加油站
        for i in range(n):
            pos, fuel = stations[i]
            for j in range(i, -1, -1):
                # 必须能到达此加油站才能更新dp[j+1]
                if dp[j] >= pos:
                    # 判断加j+1次油（也就是加了j次+当前路过的这次油量）
                    dp[j+1] = max(dp[j+1], dp[j] + fuel)
                    
        # 找到第一个大于等于target的i, 就是最少加油次数
        for i in range(n+1):
            if dp[i] >= target:
                return i
        return -1
            

