"""
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
1 <= envelopes.n <= 105
envelopes[i].n == 2
1 <= wi, hi <= 105
"""
from typing import List


# todo 动态规划 + 耐心排序  300题最长递增子序列变种题

def maxEnvelopes(envs: List[List[int]]) -> int:
    # 在300题的基础上，变成找二维数组最长自增子序列
    # 比如：23 56 64 67 71
    # 题目要求信封宽和高都比另一个大时，才能套娃。
    # 先对数组左值升序排列，这样问题就变成找右值最长递增子序列问题了。
    # 但是存在一个问题，就是左值相等的情况。是用右值较大的，还是较小的来排？比如上面的64，67
    # 看右值：3 6 4 7 1，如果用4，就会过滤掉前面的6，但是6和后面的7是能组成连续递增的。
    # 所以，在左值相等的情况下，应该是用右值较大的来继续最长递增序列

    envs.sort(key= lambda env: (env[0], -env[1]))  # 先按左值升序，如果左值相同，按照右值降序
    heights = [env[1] for env in envs]  # 对高度数组寻找 LIS
    n = len(envs)
    tails = [0] * n  # todo 注意：这里tails[i]代表长度为i的牌堆最后一个值
    piles = 0  # 牌堆数，初始值为0, 也是我们最后要找的LIS

    for i in range(n):
        h = heights[i]  # 信封高度，要发的牌,跟堆顶值比较
        # 按照耐心排序，查找当前位置LIS
        left = 0
        right = piles
        # 寻找左边界的二分查找  7891234
        while left < right:  # 左闭右开，找tails中第一个大于h的值
            mid = (left+right)//2
            if tails[mid] < h:
                left = mid + 1
            elif tails[mid] >= h:
                right = mid

        if left == piles:  # tails中没有找到比h大的，另加一个堆
            piles += 1
        # 把这张牌放到对应的牌堆顶
        tails[left] = h

    return piles






















