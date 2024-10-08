"""
机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令：

-2：向左转 90 度
-1：向右转 90 度
1 <= x <= 9：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物。

第 i 个障碍物位于网格点  (obstacles[i][0], obstacles[i][1])

如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。

返回从原点到机器人的最大欧式距离的平方。

 

示例 1：

输入: commands = [4,-1,3], obstacles = []
输出: 25
解释: 机器人将会到达 (3, 4)
示例 2：

输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出: 65
解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
 

提示：

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
答案保证小于 2 ^ 31
"""


from typing import List

# 参考
# https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/easy/874.walking-robot-simulation#si-lu
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 返回机器人距离原点的 最大欧式距离 的 平方
        ans = 0
        # 初始位置
        pos = [0, 0]
        # todo 初始方向，面向北方，角度设为 90
        dir = 90
        # todo 将 obstacles 转换为集合，方便 O(1)时间查找坐标
        obstacles = set(map(tuple, obstacles))

        # 模拟机器人行走
        for num in commands:
            if num == -1:  # 右转 90
                dir = (dir + 90) % 360
            elif num == -2:  # 左转 90
                dir = (dir + 270) % 360
            else:
                # 向前移动 num个单位
                if dir == 90:
                    # 向上
                    i = 1
                    while i <= num and (pos[0], pos[1]+1) not in obstacles:
                        i += 1
                        pos[1] += 1
                elif dir == 180:
                    # 向右
                    i = 1
                    while i <= num and (pos[0]+1, pos[1]) not in obstacles:
                        i += 1
                        pos[0] += 1
                elif dir == 270:
                    # 向下
                    i = 1
                    while i <= num and (pos[0], pos[1]-1) not in obstacles:
                        i += 1
                        pos[1] -= 1
                else:
                    # 向左
                    i = 1
                    while i <= num and (pos[0]-1, pos[1]) not in obstacles:
                        i += 1
                        pos[0] -= 1
                # 更新 ans
                ans = max(ans, pos[0]**2 + pos[1]**2)

        return ans
