"""
请你将一些箱子装在 一辆卡车 上。给你一个二维数组 boxTypes ，其中 boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi] ：

numberOfBoxesi 是类型 i 的箱子的数量。
numberOfUnitsPerBoxi 是类型 i 每个箱子可以装载的单元数量。
整数 truckSize 表示卡车上可以装载 箱子 的 最大数量 。只要箱子数量不超过 truckSize ，你就可以选择任意箱子装到卡车上。

返回卡车可以装载 单元 的 最大 总数。



示例 1：

输入：boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
输出：8
解释：箱子的情况如下：
- 1 个第一类的箱子，里面含 3 个单元。
- 2 个第二类的箱子，每个里面含 2 个单元。
- 3 个第三类的箱子，每个里面含 1 个单元。
可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8
示例 2：

输入：boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
输出：91


提示：

1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106
"""
from typing import List

"""
思路分析：这道问题在的题场景下像极了「0-1 背包问题」，但是与「0-1 背包问题」不同的是：
当前问题可以使用「贪心策略」，原因是这些箱子的差别仅仅在于「每个箱子可以装载的单位不同」，每使用一个箱子，对于限制的消耗都为 1。

「贪心算法」的直觉：
1.由于这些箱子的差别仅仅在于「每个箱子可以装载的单位不同」，而且每使用一个箱子，对于 truckSize 的消耗都为 1。
2.因此我们可以 优先选择装载的单元数量多的箱子，用完以后，然后选择装载的单元数量第二多的箱子，依次这样进行下去。
"""


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 每次先挑转载量最大的那个
        boxTypes.sort(key=lambda x: -x[1])
        n = len(boxTypes)
        res = 0

        for size, capacity in boxTypes:
            if truckSize >= size:
                res += capacity * size
                truckSize -= size
            else:
                res += capacity * truckSize
                break
        return res
