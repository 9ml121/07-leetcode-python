"""
现有一台饮水机，可以制备冷水、温水和热水。每秒钟，可以装满 2 杯 不同 类型的水或者 1 杯任意类型的水。

给你一个下标从 0 开始、长度为 3 的整数数组 amount ，其中 amount[0]、amount[1] 和 amount[2] 分别表示需要装满冷水、温水和热水的杯子数量。返回装满所有杯子所需的 最少 秒数。

 

示例 1：

输入：amount = [1,4,2]
输出：4
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯温水。
第 2 秒：装满一杯温水和一杯热水。
第 3 秒：装满一杯温水和一杯热水。
第 4 秒：装满一杯温水。
可以证明最少需要 4 秒才能装满所有杯子。
示例 2：

输入：amount = [5,4,4]
输出：7
解释：下面给出一种方案：
第 1 秒：装满一杯冷水和一杯热水。
第 2 秒：装满一杯冷水和一杯温水。
第 3 秒：装满一杯冷水和一杯温水。
第 4 秒：装满一杯温水和一杯热水。
第 5 秒：装满一杯冷水和一杯热水。
第 6 秒：装满一杯冷水和一杯温水。
第 7 秒：装满一杯热水。
示例 3：

输入：amount = [5,0,0]
输出：5
解释：每秒装满一杯冷水。
 

提示：

amount.length == 3
0 <= amount[i] <= 100
"""

import math
from typing import List

# 方法1：贪心 + 递归
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # 返回装满所有杯子所需的 最少 秒数。
        # 每次递归先排序amount, 保证后面可以取数量最多的杯子
        amount.sort()

        if amount[1] == 0:
            # 只剩一个杯子有水
            return amount[2]
        else:
            # 至少有2个杯子有水，每次选择数量最多的2个杯子装水
            amount[1] -= 1
            amount[2] -= 1
            # 递归进入下一轮
            return self.fillCups(amount) + 1

# 方法2 贪心 + 数学归纳法
# 排序amount, 假设三种类型杯子数量从少到多分别为a, b, c
# 1.如果a + b <= c, 每次选择c，都至少可以带一个a或者b, 总花费时间是c
# 2.如果a + b > c, 每次选择c, 都至少可以带一个a或者b, 花费时间为c, 最后还剩a+b-c个杯子（x）
#   如果x为偶数，剩余花费时间为x//2
#   如果x为奇数，剩余花费时间为x//2 + 1

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # 返回装满所有杯子所需的 最少 秒数。
        amount.sort()
        a, b, c = amount
        if a + b <= c:
            return c
        else:
            return c + math.ceil((a+b-c)/2)
