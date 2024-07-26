"""
你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 n 份兼职工作，每份工作预计从 startTime[i] 开始到 endTime[i] 结束，报酬为 profit[i]。

给你一份兼职工作表，包含开始时间 startTime，结束时间 endTime 和预计报酬 profit 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 X 结束，那么你可以立刻进行在时间 X 开始的下一份工作。

 

示例 1：
输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作， 
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。

示例 2：
输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。 
共获得报酬 150 = 20 + 70 + 60。

示例 3：
输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6
 

提示：

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""
from bisect import bisect_left
from typing import List


# todo §6.4 不相交区间
# 方法2: 动态规划 + 二分查找优化
# 相似题目：1751. 最多可以参加的会议数目 II
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 按照工作结束时间升序
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])


        # 定义 f[i] 表示按照结束时间排序后的前 i 个工作的最大报酬，用「选或不选」分类讨论
        # 不选第 i 个工作：f[i]=f[i−1]；
        # 选第 i 个工作：f[i] = f[j]+profit[i]，其中 j 是最大的满足 endTime[j]≤startTime[i] 的 j，不存在时为 −1。
        # 由于结束时间是有序的，j 可以用二分查找计算出来
        n = len(jobs)
        f = [0] * n
        f[0] = jobs[0][2]

        def bin_search(jobs:list, i:int):
            # 右端二分查找
            left, right = 0, i - 1
            while left <= right:
                mid = (left + right) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    if jobs[mid + 1][1] <= jobs[i][0]:
                        left = mid + 1
                    else:
                        return mid
                else:
                    right = mid - 1
            return -1
        
        for i in range(1, n):
            # 找到在当前工作开始之前结束的工作中报酬最大的那份工作
            j = bin_search(jobs, i)
            if j >= 0:
                f[i] = max(f[i-1], f[j] + jobs[i][2])
            else:
                f[i] = max(f[i-1], jobs[i][2])

        # print(dp)
        return f[-1]

# 更简洁写法
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))  # 按照结束时间排序
        f = [0] * (len(jobs) + 1)
        for i, (_, st, p) in enumerate(jobs):
            j = bisect_left(jobs, (st + 1,), hi=i)  # hi=i 表示二分上界为 i（默认为 n）
            # 状态转移中，为什么是 j 不是 j+1：上面算的是 > st，-1 后得到 <= st，但由于还要 +1，抵消了
            f[i + 1] = max(f[i], f[j] + p)
        return f[-1]
    

# 方法1: 只用区间dp(部分超时)
class Solution1:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # 1.按照结束时间升序
        n = len(startTime)
        jobs = [(startTime[i], endTime[i], profit[i]) for i in range(n)]
        jobs.sort(key=lambda x: x[1])

        # 2.dp[i]代表jobs下标为i的截止时间工作可以获得的最大收益
        dp = [0] * n
        dp[0] = jobs[0][2]
        for i in range(1, n):
            # 3.找到在当前工作开始之前结束的工作中报酬最大的那份工作
            st, et, p = jobs[i]
            j = i-1
            while j >= 0 and jobs[j][1] > st:
                j -= 1
            if j >= 0:
                dp[i] = max(dp[i-1], dp[j] + p)
            else:
                dp[i] = max(dp[i-1], p)

        # print(dp)
        return dp[-1]
