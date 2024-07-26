"""
在一条单行道上，有 n 辆车开往同一目的地。目的地是几英里以外的 target 。

给定两个整数数组 position 和 speed ，长度都是 n ，其中 position[i] 是第 i 辆车的位置， speed[i] 是第 i 辆车的速度(单位是英里/小时)。

一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车 以相同的速度 紧接着行驶。此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。

车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。

即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。

返回到达目的地的 车队数量 。

 

示例 1：

输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
输出：3
解释：
从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。
示例 2:

输入: target = 10, position = [3], speed = [3]
输出: 1
解释: 只有一辆车，因此只有一个车队。
示例 3:

输入: target = 100, position = [0,2,4], speed = [4,2,1]
输出: 1
解释:
以0(速度4)和2(速度2)出发的车辆组成车队，在4点相遇。舰队以2的速度前进。
然后，车队(速度2)和以4(速度1)出发的汽车组成一个车队，在6点相遇。舰队以1的速度前进，直到到达目标。
 

提示：

n == position.length == speed.length
1 <= n <= 105
0 < target <= 106
0 <= position[i] < target
position 中每个值都 不同
0 < speed[i] <= 106
"""
from typing import List

# todo 排序 + 栈
"""
分析
我们首先对这些车辆按照它们的起始位置降序排序，并且用 (target - position) / speed 计算出每辆车在不受其余车的影响时，行驶到终点需要的时间。
对于相邻的两辆车 S 和 F，F 的起始位置大于 S，如果 S 行驶到终点需要的时间小于等于 F，那么 S 一定会在终点前追上 F 并形成车队。
这是因为在追上 F 之前，S 的行驶速度并不会减小，而 F 却有可能因为追上前面的车辆而速度减小，因此 S 总能在终点前追上 F。

算法
将车辆按照起始位置降序排序后，我们顺序扫描这些车辆。
1. 如果相邻的两辆车，前者比后者行驶到终点需要的时间短，那么后者永远追不上前者，即从后者开始的若干辆车辆会组成一个新的车队；
2. 如果前者不比后者行驶到终点需要的时间短，那么后者可以在终点前追上前者，并和前者形成车队。
    此时我们将后者到达终点的时间置为前者到达终点的时间。
"""

# 写法1：
class Solution(object):
    def carFleet(self, target, position, speed):
        # 返回到达目的地的 车队数量 。
        ans = 0
        # cars按照车辆开始位置升序排列
        cars = sorted(zip(position, speed))
        # times表示开始位置从后往前， 每辆车跑到终点花费的时间
        # todo 注意：后面直接把times当成栈使用
        times = [float(target - p) / s for p, s in cars]
        
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]:
                # 后面车追不上lead
                ans += 1 
            else:
                # 后面车可以追上lead, 最后花费时间就是lead
                times[-1] = lead 
                
        # 返回结果加上最后一个到达车队
        return ans + 1 

# 写法2
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 返回到达目的地的 车队数量 。
        ans = 0
        # 按照车辆初始位置，升序排列
        cars = sorted(zip(position, speed))
        n = len(cars)
        # 计算每辆车到达终点时间
        times = [(target - p)/s for p, s in cars]

        front_time = 0  # 记录前面一辆车到达终点的时间
        # 倒序遍历,从最靠近终点的车往出发点看
        for i in range(n-1, -1, -1):
            cur_time = times[i]
            if front_time < cur_time:
                # 1.如果前车比后一辆车到达终点的耗时短，那么后车一定追不上，所以前车独立为一个车队
                front_time = cur_time
                ans += 1
            
            # 2.如果前车比后一辆车到达终点的耗时长或者一样，后车会追上前车，并以前车同样的耗时一起到达终点
            # 也就是front_time保持不变
            
        return ans
