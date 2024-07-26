"""
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有 piles[i] 根香蕉。警卫已经离开了，将在 h 小时后回来。
珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。
珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。
返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。



示例 1：
输入：piles = [3,6,7,11], h = 8
输出：4

示例 2：
输入：piles = [30,11,23,4,20], h = 5
输出：30

示例 3：
输入：piles = [30,11,23,4,20], h = 6
输出：23


提示：
1 <= piles.n <= 104
piles.n <= h <= 109
1 <= piles[i] <= 109
"""
import math
from typing import List


# todo 经典二分查找应用：最大值最小化问题， 二分答案
# 二分查找写法1(推荐！)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 计算在h小时内吃完piles所有香蕉的最小速度k

        # k的最小值和最大值
        # k为piles最大值，每小时都可以吃1堆，用时最少(len(piles)小时)， h>=n
        hi = max(piles)
        # 题目说k为整数，最小值为1
        lo = 1

        def check(k: int):
            # 判断吃香蕉的速度为k根/小时，能否在h小时吃完
            cost = sum(math.ceil(pile / k) for pile in piles)
            return cost <= h

        # 二分答案k,并判断是否可以在h小时吃完
        while lo < hi:
            mid = (lo+hi) >> 1
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        
        # 搜索左边界，结果返回lo
        return lo

# 二分查找写法2
class Solution2:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 计算在h小时内吃完piles所有香蕉的最小速度k

        # 最小k的最大值是max(piles),即每小时都能吃一堆。最终len(piles)小时可以吃完
        # 最小值为1，即每小时吃1根。
        hi = max(piles)
        lo = 1

        ans = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            # 计算速度为mid， 吃完所有香蕉花费的时间
            cost = sum(math.ceil(pile / mid) for pile in piles)

            if cost <= h:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans


if __name__ == '__main__':
    piles = [30, 11, 23, 4, 20]
    h = 6  # 输出：23
    sol = Solution2()
    print(sol.minEatingSpeed(piles, h))  # 16
