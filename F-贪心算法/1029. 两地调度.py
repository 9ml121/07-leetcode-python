"""
公司计划面试 2n 人。给你一个数组 costs ，其中 costs[i] = [aCosti, bCosti] 。第 i 人飞往 a 市的费用为 aCosti ，飞往 b 市的费用为 bCosti 。

返回将每个人都飞到 a 、b 中某座城市的最低费用，要求每个城市都有 n 人抵达。



示例 1：

输入：costs = [[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 a 市，费用为 10。
第二个人去 a 市，费用为 30。
第三个人去 b 市，费用为 50。
第四个人去 b 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。
示例 2：

输入：costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
输出：1859
示例 3：

输入：costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
输出：3086


提示：

2 * n == costs.length
2 <= costs.length <= 100
costs.length 为偶数
1 <= aCosti, bCosti <= 1000
"""
from typing import List

# 方法 1：贪心算法
"""
公司首先将这 2N 个人全都安排飞往 B 市，再选出 N 个人改变它们的行程，让他们飞往 A 市。
如果选择改变一个人的行程，那么公司将会额外付出 price_A - price_B 的费用，这个费用可正可负。
如果数组 costs 「按照城市 A - 城市 B 差值升序排序」，那么排好序的数组前半部分应该去城市 A，后半部分应该去城市 B。
"""


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        # print(costs)  # [[30, 200], [10, 20], [30, 20], [400, 50]]

        min_cost = 0
        n = len(costs)
        for i in range(n):
            if i < n // 2:
                min_cost += costs[i][0]
            else:
                min_cost += costs[i][1]

        return min_cost
