"""
城市的 天际线 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 由这些建筑物形成的 天际线 。

每个建筑物的几何信息由数组 buildings 表示，其中三元组 buildings[i] = [lefti, righti, heighti] 表示：

lefti 是第 i 座建筑物左边缘的 x 坐标。
righti 是第 i 座建筑物右边缘的 x 坐标。
heighti 是第 i 座建筑物的高度。
你可以假设所有的建筑都是完美的长方形，在高度为 0 的绝对平坦的表面上。

天际线 应该表示为由 “关键点” 组成的列表，格式 [[x1,y1],[x2,y2],...] ，并按 x 坐标 进行 排序 。
关键点是水平线段的左端点。列表中最后一个点是最右侧建筑物的终点，y 坐标始终为 0 ，仅用于标记天际线的终点。
此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

注意：输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；
三条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...]



示例 1：


输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
解释：
图 A 显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
示例 2：

输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]


提示：

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildings 按 lefti 非递减排序
"""
import collections
import heapq
from typing import List

import sortedcontainers

"""
解题思路： 
这道题可以使用扫描线算法来解决。具体步骤如下： 
1. 首先，将每个建筑物的左边缘和右边缘点以及高度存储在一个列表中。 
2. 对于每个建筑物，将左边缘点和高度存储为负数，右边缘点和高度存储为正数，这样可以区分左边缘和右边缘。 
3. 对列表进行排序，排序规则为：首先按照横坐标进行排序，如果横坐标相同，则按照以下规则排序： 
   - 如果是左边缘点，则按照高度从大到小排序； 
   - 如果是右边缘点，则按照高度从小到大排序。 
4. 创建一个最大堆（Max Heap），用于存储当前的高度。 
5. 遍历排序后的列表，对于每个点，如果是左边缘点，则将其高度加入堆中；如果是右边缘点，则将其高度从堆中移除。 
6. 如果当前的高度与堆中的最大高度不同，则说明出现了天际线的拐点，将当前点的横坐标和堆中的最大高度加入结果列表。 
7. 最后，返回结果列表即为天际线图。 
"""

import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 将每个建筑的左右边界点拆分成两个元组，一个表示左边界，一个表示右边界
        points = []
        for left, right, height in buildings:
            points.append((left, -height))  # 左边界的高度取负数，表示是起点
            points.append((right, height))  # 右边界的高度表示是终点
        # 按照横坐标进行排序
        points.sort()
        # 初始化堆，用来维护当前的最大高度,初始化最大高度为 0
        max_heap = [0]
        # 初始化结果列表，用于存储关键点
        result = []

        # 遍历所有边界点
        for x, height in points:
            # 如果是起点，将高度加入堆中
            if height < 0:
                heapq.heappush(max_heap, height)
            # 如果是终点，将对应的起点高度从堆中移除
            else:
                # 注意：heap.remove(-height)操作的时间复杂度是O(N)
                max_heap.remove(-height)
                # 重新构建堆
                heapq.heapify(max_heap)
            # 获取当前最大高度
            curr_max_height = -max_heap[0]
            # 如果结果列表为空，或者当前最大高度与之前的最大高度不同，说明是关键点
            if len(result) == 0 or curr_max_height != result[-1][1]:
                result.append([x, curr_max_height])
        return result


"""
上述解法中的heap.remove(-height)操作的时间复杂度是O(N)，可以通过优化来减少时间复杂度。 
 
一种优化方法是使用一个额外的数据结构来记录每个高度在堆中的索引，
例如使用字典（dictionary）来实现。
这样，在需要移除高度时，可以直接通过索引来删除，而不需要遍历整个堆。 
"""


class Solution2:
    def getSkyline(self, buildings):
        # 第 1 步：预处理
        points = []
        for left, right, height in buildings:
            # 负号表示左边高度的转折点
            points.append((left, -height))
            points.append((right, height))
        # 第 2 步：按照横坐标排序，横坐标相同的时候，高度高的在前面
        # points.sort(key=lambda x: (x[0], -x[1]))
        points.sort(key=lambda x: (x[0], x[1]))
        # 第 3 步：扫描一遍动态计算出结果
        maxHeap = [0]  # 这是一个大顶堆
        # 哈希表，记录「延迟删除」的元素，key 为元素，value 为需要删除的次数
        delayed = {}
        # 最开始的时候，需要产生高度差，所以需要加上一个高度为 0，宽度为 0 的矩形
        # 为了计算高度差，需要保存之前最高的高度
        maxHeight = 0
        res = []
        for x, height in points:
            if height < 0:
                # 说明此时是「从下到上」，纵坐标参与选拔最大值，请见「规则 1」
                heapq.heappush(maxHeap, height)
            else:
                # 不是真的删除 buildingPoint[1]，把它放进 delayed，等到堆顶元素是 buildingPoint[1] 的时候，才真的删除
                delayed[height] = delayed.get(height, 0) + 1
            # 如果堆顶元素在延迟删除集合中，才真正删除，这一步可能执行多次，所以放在 while 中
            # while (true) 都是可以的，因为 maxHeap 一定不会为空
            while maxHeap and -maxHeap[0] in delayed:
                delayed[-maxHeap[0]] -= 1
                if delayed[-maxHeap[0]] == 0:
                    del delayed[-maxHeap[0]]
                heapq.heappop(maxHeap)
            curMaxHeight = -maxHeap[0]
            # 有高度差，才有关键点出现
            if curMaxHeight != maxHeight:
                # 正在扫过的左端点的值
                res.append([x, curMaxHeight])
                # 当前高度成为计算高度差的标准
                maxHeight = curMaxHeight
        return res


"""
这段代码使用 sortedcontainers.SortedDict 来维护当前活动建筑物的高度信息，并根据建筑物的边界点来更新活动建筑物集合。
在遍历过程中，根据当前最高建筑物的高度是否与前一个高度不同，来判断是否出现了天际线上的关键点。最后返回天际线上的关键点列表。
"""


# 方法2：平衡二叉搜索树
class Solution3:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 将所有的建筑物边界点提取出来，并按照横坐标进行排序
        points = []
        for left, right, height in buildings:
            points.append((left, -height))  # 左边界点的高度取负值，表示进入建筑物
            points.append((right, height))  # 右边界点的高度表示离开建筑物
        points.sort()
        # 使用 SortedDict 存储当前活动建筑物的高度信息
        active_buildings = sortedcontainers.SortedDict()
        active_buildings[0] = 1  # 添加一个高度为0的虚拟建筑物，用于初始化
        # 遍历所有的边界点，更新当前的活动建筑物集合，并记录天际线上的关键点
        skyline = []
        prev_height = 0
        for x, height in points:
            if height < 0:
                # 进入建筑物，将其高度加入活动建筑物集合
                height = -height
                active_buildings[height] = active_buildings.get(height, 0) + 1
            else:
                # 离开建筑物，将其高度从活动建筑物集合中删除
                active_buildings[height] -= 1
                if active_buildings[height] == 0:
                    del active_buildings[height]
            # 当前最高建筑物的高度即为活动建筑物集合的最后一个键
            curr_height = active_buildings.iloc[-1]
            # 如果当前高度与前一个高度不同，说明出现了天际线上的关键点
            if curr_height != prev_height:
                skyline.append([x, curr_height])
                prev_height = curr_height
        return skyline


if __name__ == '__main__':
    # buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    # 输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    buildings = [[0, 2, 3], [2, 5, 3]]
    # 输出：[[0,3],[5,0]]
    # buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3], [2, 3, 1], [2, 3, 2], [2, 3, 3]]
    # [[1,3],[3,0]]
    print(Solution2().getSkyline(buildings))
