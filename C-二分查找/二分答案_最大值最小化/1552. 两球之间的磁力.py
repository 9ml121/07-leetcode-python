"""
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。
Rick 有 n 个空的篮子，第 i 个篮子的位置在 position[i] ，Morty 想把 m 个球放到这些篮子里，使得任意两球间 最小磁力 最大。
已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。

给你一个整数数组 position 和一个整数 m ，请你返回最大化的最小磁力。

示例 1
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。
示例 2：

输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。


提示：

n == position.n
2 <= n <= 10^5
1 <= position[i] <= 10^9
所有 position 中的整数 互不相同 。
2 <= m <= position.n

"""
from typing import List

# todo B-二分查找：最小值最大化问题
"""
题目解析 ：本题是最小值最大化问题，可以使用二分法求解。
本题描述中说
已知两个球如果分别位于 x 和 y ，那么它们之间的磁力为 |x - y| 。
则可以得出，磁力 = 距离，即距离越大，磁力越大。
假设：
    放置方式1的两两相邻球之间的磁力的最小值为a
    放置方式2的两两相邻球之间的磁力的最小值为b
    ...
    放置方式X的两两相邻球之间的磁力的最小值为x
那么本题的题解就是 max(a, b, ..., x)。即求最大的最小磁力。
本题如果用求组合的策略来求解最大的最小磁力的话，则会超时。最佳策略是用二分

由于题目已经给定了n个篮子的位置position，我们将position进行升序，则可得出：
    两球之间的磁力最大值 = position[n-1] - postion[0]
    而两球之间的磁力至少为1。

1.本题中磁力就是距离，因此我们就有了两球之间距离的最小值min：1，和最大值max：position[n-1] - postion[0]
2.接下来就可以用二分策略，求得一个中间值mid = (min + max) / 2，然后将mid值作为两球之间的最小间距dis，
3.如果有放置策略可以满足所有两两相邻球之间的距离都大于等于dis，则dis就是本题的一个可能解。

具体检查是否满足的逻辑如下：
a.首先，我们肯定可以放下第一个球，且第一个球的最佳放置位置就是position[0]。
    我们记录：最新放球位置 curPos = position[0]
            已放置球个数 count = 1
b.接下来，我们从 i = 1 开始遍历，到 i = n - 1结束：
- 如果position[i] - curPos >= dis，则说明将下一个球放到position[i]位置，可以满足最小间距dis的条件，此时count++，且更新curPos = position[i]
- 如果position[i] - curPos < dis，则说明下一个球不能放到position[i]位置，此时我们只能 i ++ 

c.遍历结束时：
如果count >= m，
    则说明m个球都能够在满足两两之间最小间距dis的情况下放到n个篮子中，此时dis就是一个可能解，但不一定时最优解，
    我们记录此时的dis后，尝试增大二分范围左边界，即min = mid + 1后，继续求中间值mid
如果count < m，
    则说明m个球不能在满足两两之间最小间距dis的情况下放到n个篮子中，则说明当前dis大了，我们应该缩小dis，
    即减少二分范围的右边界，即max = mid - 1，继续求中间mid
"""


class Solution:
    # 求能放下m个球最大间距
    def maxDistance(self, position: List[int], m: int) -> int:
        # 排序
        position.sort()

        # 两球距离的最小值，最大值
        minDis = 1
        maxDis = position[-1] - position[0]

        # 二分查找能放下m个球的最大相邻距离
        ans = 0
        while minDis <= maxDis:
            # 从中间距离开始尝试
            mid = (maxDis + minDis) // 2
            if self.check(position, m, mid):
                ans = mid
                minDis = mid + 1
            else:
                maxDis = mid - 1

        return ans

    # 检查两球距离为dis时，在position中能够放下m个球
    def check(self, position, m, dis):
        count = 1
        curPos = position[0]  # 第一个肯定能放下
        for i in range(1, len(position)):
            if position[i] >= curPos + dis:
                count += 1
                curPos = position[i]
            if count >= m:
                return True
        return False


cls = Solution()
positions = [79, 74, 57, 22]
m = 4
print(cls.maxDistance(positions, m))
