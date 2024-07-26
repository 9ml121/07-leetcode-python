"""
在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一 的。

 

示例 1:

输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
示例 2:

输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
 

提示:

gas.length == n
cost.length == n
1 <= n <= 105
0 <= gas[i], cost[i] <= 104

"""
from typing import List

# 方法1：暴力解法：超时


class Solution1:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # 依次尝试每个点作为起点，然后判断剩余油量能不能走完环形数组n个位置
        for i in range(n):
            remain = gas[i] - cost[i]
            if remain >= 0:
                flag = True
                for j in range(i+1, i+n):
                    j %= n
                    remain += gas[j] - cost[j]
                    if remain < 0:
                        flag = False
                        break
                if flag:
                    return i
        return -1


# 方法2：发现一些隐藏较深的规律，从而减少一些冗余的计算（图像算法）
# 判断这个环形数组中是否能够找到一个起点 start，使得从这个起点开始的累加和一直大于等于 0。
# 参考：https://labuladong.online/algo/frequency-interview/gas-station-greedy/#%E5%9B%BE%E5%83%8F%E8%A7%A3%E6%B3%95
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        # 相当于图像中的坐标点和最低点
        remain = 0
        min_sum = 0
        start = 0
        for i in range(n):
            remain += gas[i] - cost[i]
            if remain < min_sum:
                # 经过第 i 个站点后，使 sum 到达新低
                # 所以站点 i + 1 就是最低点（起点）
                min_sum = remain
                start = i + 1
        if remain < 0:
            return -1
        
        return start if start < n else -1


# 方法3： 贪心算法
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        remain = 0
        for i in range(n):
            remain += gas[i] - cost[i]
        # 规律一：最后剩余油量为0, 无论从哪里出发，就无法通过环形数组
        if remain < 0:
            return -1
        
        # 规律二：如果最后剩余油量大于0,可能存在一个起点可以走完全程
        # 记录起点
        start = 0
        # 记录从start到当前点剩余油量
        sub_sum = 0
        for i in range(n):
            sub_sum += gas[i] - cost[i]
            if sub_sum < 0:
                # todo 从start到i之间的任何点作为起点，都无法通过环形数组
                # 起点start只能是从i下一点开始
                start = i + 1
                sub_sum = 0
        
        return start if start < n else -1
        
        