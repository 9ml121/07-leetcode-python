''"""
给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。


示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
示例 2：

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1


提示：

1 <= envelopes.length <= 10^5
envelopes[i].length == 2
1 <= wi, hi <= 10^5
"""
import bisect
from typing import List


# 方法 1：暴力动态规划：超时O(N^2)
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 先对宽度升序，再对高度降序排列
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)
        n = len(envelopes)
        dp = [1] * n

        for i in range(1, n):
            for j in reversed(range(i)):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # print(dp)
        return max(dp)


"""
方法二：维护单增序列
思路
    更换想法，对方法二中最长上升子序列问题的求解做优化，不再维护长度为 O(N)的 dp 数组，改为维护一条最长递增序列。

状态定义:
    dp[i] 表示长度为 i+1 的最长上升子序列，第 i 位的最小值。

状态转移:
    1.同方法二，首先对整个数组按照宽度由小到大排序，排序同时，对于宽度相同的项，根据高度由大到小排序。
    2.排序完毕后，提取出所有的h，形成一个新的数组。对新的数组执行“最长上升子序列”问题的求解:
    3.遍历 [0,n) 区间，对每一个值 x ，判断 x 在单增序列 dp 中的位置，做以下判断：
        - 当 dp 中仅存在某值满足 y>x ：使用 x 替换该值 y
        - 当 dp 中存在多值满足 yt>y2>y1>x ：使用 x 替换符合条件的最小值 y1 
        - 当 dp 中不存在值满足 y>x：将 x 添加到 dp 数组最末端

为什么可以这样做？：假设当前 dp 队列为1, 3, 6。 这翻译过来是：
    1. 存在一条上升子序列，长度为1，且以1为结尾；
    2. 存在一条上升子序列，长度为2，且以3为结尾；
    3. 存在一条上升子序列，长度为3，且以6为结尾。
假设此时来了个新的值4，显然的，可以在长度为2且末尾为3的那条上升子序列后，再添加一个4，形成一条长度为3，且以4为结尾的上升子序列。 
同时更新 dp 队列变成1,3,4。这是因为同样是长度为3，以6为结尾后，想继续扩充，新增的数字至少为7；而以4为结尾时，新增数字仅需至少为5即可。

额外需要注意的是：dp 的结果，不一定就是一条存在的上升子序列：仍然以1,3,6为例，假设此时新增的数字为2，则 dpdpdp 更新为1,2,6。
但实际上并不存在一条子序列，满足1,2,6。
1,2,6仅可翻译为：
    1.存在一条上升子序列，长度为1，且以1为结尾；
    2.存在一条上升子序列，长度为2，且以2为结尾；
    3.存在一条上升子序列，长度为3，且以6为结尾。

比起方法1，这个方法其实优化了很多，远不是 O(N^2) 的复杂度，而是 O(N∗len(dp))
但是假如一开始给定的就是一个层层套娃的合法序列，那么最差时间复杂度仍然能达到O(N^2)
"""


class Solution2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [env[1] for env in envelopes]
        n = len(heights)
        # 预开空间,初始值为排序后第一个信封的高度
        dp = [heights[0]]

        # 计算最长上升子序列
        for i in range(1, n):
            # 搜索合适的更新位置
            j = 0
            while j < len(dp):
                # 需要注意，只要不小于当前大小，即可更新
                if dp[j] >= heights[i]:
                    dp[j] = heights[i]
                    break
                j += 1

            # 如果整个dp列表中，不含有比当前h大的值，则扩展dp列表
            if j == len(dp):
                dp.append(heights[i])

        return len(dp)


# 动态规划 + 二分查找：时间复杂度优化到O(Nlog(N))
# 实际上就是耐心排序问题
class Solution3:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 先对宽度 w 进行升序排序，如果遇到 w 相同的情况，则按照高度 h 降序排序。
        # 之后把所有的 h 作为一个数组，在这个数组上计算 LIS 的长度就是答案。
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        # print(envelopes)

        # dp[i] 表示长度为 i+1 的最长上升子序列，第 i 位的最小值。
        dp = []

        for envelope in envelopes:
            idx = bisect.bisect_left(dp, envelope[1])
            if idx == len(dp):
                dp.append(envelope[1])
            else:
                dp[idx] = envelope[1]

        # print(dp)
        return len(dp)


class Solution4:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # 先按左值升序，如果左值相同，按照右值降序
        envelopes.sort(key=lambda env: (env[0], -env[1]))
        # 对高度数组寻找 LIS
        heights = [env[1] for env in envelopes]

        n = len(heights)
        # todo 注意：这里dp[i]代表长度为i的牌堆最后一个值
        dp = [heights[0]]

        for i in range(n):
            h = heights[i]  # 信封高度，要发的牌,跟堆顶值比较
            # 按照耐心排序，查找当前位置LIS
            left = 0
            right = len(dp)
            # 寻找左边界的二分查找  7891234
            # 左闭右开，找tails中第一个大于h的值
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            # tails中没有找到比h大的，另加一个堆
            if left == len(dp):
                dp.append(h)
            else:
                # 把这张牌放到对应的牌堆顶
                dp[left] = h

        # print(dp)
        return len(dp)
