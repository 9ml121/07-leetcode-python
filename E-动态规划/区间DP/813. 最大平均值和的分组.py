"""
给定数组 nums 和一个整数 k 。我们将给定的数组 nums 分成 最多 k 个非空子数组，且数组内部是连续的 。
分数 由每个子数组内的平均值的总和构成。
注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。

返回我们所能得到的最大 分数 是多少。
答案误差在 10-6 内被视为是正确的。

示例 1:
输入: nums = [9,1,2,3,9], k = 3
输出: 20.00000
解释:
nums 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
我们也可以把 nums 分成[9, 1], [2], [3, 9].
这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.

示例 2:
输入: nums = [1,2,3,4,5,6,7], k = 4
输出: 20.50000


提示:
1 <= nums.length <= 100
1 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
from typing import List

# todo 区间dp + 前缀和
#  类似 410.分割数组的最大值copy.py

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        # 划分份数越多，平均值之和越大，因此想要取得最大值必然是恰好划分成 k 段
        n = len(nums)
        # dp[i][j]: nums下标[0..i-1]区间内分为j段得到的最大平均值总和
        dp = [[0.0] * (k + 1) for _ in range(n + 1)]
        pre_sum = [0] * (n + 1)

        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
            # 分割为1个子数组
            dp[i][1] = pre_sum[i] / i
        

        for i in range(2, n + 1):  # i代表nums下标[0..i-1]
            for j in range(2, min(i, k) + 1):  # j代表分割的子数组个数,从2开始，最多min(i, k)个
                for t in range(j - 1, i):  # 枚举最后一个子数组的起点索引
                    arrAvg = (pre_sum[i] - pre_sum[t]) / (i - t)  # nums[t+1..i)区间平均值
                    dp[i][j] = max(dp[i][j], dp[t][j - 1] + arrAvg)
        
        # print(dp)
        return dp[n][k]


if __name__ == '__main__':
    nums = [9, 1, 2, 3, 9]
    k = 3  # 20
    print(Solution().largestSumOfAverages(nums, k))
