"""
n 个灯泡排成一行，编号从 1 到 n 。最初，所有灯泡都关闭。每天 只打开一个 灯泡，直到 n 天后所有灯泡都打开。

给你一个长度为 n 的灯泡数组 blubs ，其中 bulbs[i] = x 意味着在第 (i+1) 天，我们会把在位置 x 的灯泡打开，其中 i 从 0 开始，x 从 1 开始。

给你一个整数 k ，请返回恰好有两个打开的灯泡，且它们中间 正好 有 k 个 全部关闭的 灯泡的 最小的天数 。如果不存在这种情况，返回 -1 。

 

示例 1：

输入：
bulbs = [1,3,2]，k = 1
输出：2
解释：
第一天 bulbs[0] = 1，打开第一个灯泡 [1,0,0]
第二天 bulbs[1] = 3，打开第三个灯泡 [1,0,1]
第三天 bulbs[2] = 2，打开第二个灯泡 [1,1,1]
返回2，因为在第二天，两个打开的灯泡之间恰好有一个关闭的灯泡。
示例 2：

输入：bulbs = [1,2,3]，k = 1
输出：-1
 

提示：

n == bulbs.length
1 <= n <= 2 * 104
1 <= bulbs[i] <= n
bulbs 是一个由从 1 到 n 的数字构成的排列
0 <= k <= 2 * 104
"""

from math import inf

# todo 方法1：定长滑窗 + 滑窗内的元素都比l和r两端元素大(推荐！)
# [3,9,2,8,1,6,10,5,4,7]     bulbs
#   0 1 2 3 4 5 6  7 8 9 10  idx
# [-1,5,3,1,9,8,6,10,4,2,7]  days
class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        # 返回恰好有两个打开的灯泡，且它们中间 正好 有 k 个 全部关闭的 灯泡的 最小的天数
        # todo 符合条件的情形：一个长度为k+2的窗口。内部的天数均大于window[L]和window[R]
        n = len(bulbs)
        ans = inf

        # days[x]=i: 表示第x号灯泡会在第i天打开
        days = [-1] * (n+1)
        for i, x in enumerate(bulbs):
            days[x] = i+1
        # print(days)
        
        # l, r分别表示中间间隔k个灯泡的左右灯泡编号
        l = 1
        r = l + k + 1
        while r <= n:
            ok = True  # ok的情形为：窗口内灯泡打开的天数，比LR两端都要大
            for x in range(l+1, r):
                if days[x] < max(days[l], days[r]):
                    ok = False
                    l = x
                    r = l+k+1
                    break

            if ok:
                # 注意：题目是要找符合条件的最小天数
                ans = min(ans, max(days[l], days[r]))
                l = r
                r = l+k+1

        return -1 if ans == inf else ans


# 方法2：有序集合set： sortedcontainers.SortedSet()
# 让我们按开灯的顺序添加灯。当每一盏灯开灯时，我们会检查它的邻居，看他们是否能满足当前的条件。

class Solution:
    def kEmptySlots(self, bulbs: list[int], k: int) -> int:
        # 返回恰好有两个打开的灯泡，且它们中间 正好 有 k 个 全部关闭的 灯泡的 最小的天数
        from sortedcontainers import SortedSet
        # todo 有序集合active，会按照打开的灯编号从小到大排列
        active = SortedSet()
        cnt = 0  # cnt表示有序集合大小，也就是当前天数
        
        for i, x in enumerate(bulbs):
            # 按开灯的时间顺序添加灯。添加一盏灯时，二分查找当前灯是在第几天打开的
            active.add(x)
            cnt += 1
            pos = active.bisect_left(x)
            
            # 如果前一天或者后一天打开的灯编号和当前灯编号间隔k盏灯，证明当前天数i+1是满足条件的最小天数
            if pos != cnt - 1:
                x_next = active[pos + 1]
                if x_next - x == k + 1:
                    return i + 1

            if pos != 0:
                x_pre = active[pos - 1]
                if x - x_pre == k + 1:
                    return i + 1
        return -1


