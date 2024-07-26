"""
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。
设计一个算法使得这 m 个子数组各自和的最大值最小。

示例 1：
输入：nums = [7,2,5,10,8], m = 2
输出：18
解释：
一共有四种方法将 nums 分割为 2 个子数组。
其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

示例 2：
输入：nums = [1,2,3,4,5], m = 2
输出：9

示例 3：
输入：nums = [1,4,4], m = 3
输出：4


提示：
1 <= nums.n <= 1000
0 <= nums[i] <= 106
1 <= m <= min(50, nums.n)
"""
from typing import List


# 方法1：B-二分查找
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 子数组各自和的最大值 的最小值为max(nums),k = len(nums)
        lo = max(nums)
        # 子数组各自和的最大值 的最大值为
        hi = sum(nums)  # 也就是k=1
        ans = hi
        while lo <= hi:
            # 从中间开始推：
            midV = lo + (hi - lo) // 2
            if self.canSplit(nums, k, midV):
                # 继续减少midV
                ans = midV
                hi = midV - 1
            else:
                # 增大midv: 子数组和的最大值的最小值越大，数组分法就越多
                lo = midV + 1
        return ans

    # 计算可不可能分k个子数组，子数组各自和的最大值 最小为x
    def canSplit(self, nums, k, x):
        # 已知 k < len(nums)
        cnt = 0
        i = 0
        while i < len(nums):
            tmp = x
            # 尽量把x用完，统计可以分成的数组最少个数cnt，如果cnt > k,说明不可能 ； 否则是可以的
            while i < len(nums) and tmp >= 0:
                if tmp >= nums[i]:
                    tmp -= nums[i]
                else:
                    break
                i += 1

            cnt += 1
        return cnt <= k


# 二分查找写法2
class Solution2:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 最大值最小化问题
        # 1.当k=len(nums),也就是nums每个数都是一个子数组，此时子数组和的最大值最小，为max(nums)
        # 2.当k=1,也就是nums划分为一个子数组，此时子数组和的最大值最大，为sum(nums)
        # 3.当1 < k < len(nums)，子数组各自和的最大值一定介入[max(nums)..sum(nums)]之间，因为nums给的是非负整数

        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            # 计算子数组各自和的最大值为mid时，可以划分的子数组最少个数splits
            splits = self.getSplitCnt(nums, mid)
            if splits > k:
                # 如果splits > k:说明划分子数组个数多了，也就是mid猜小了，mid和mid左边一定不是要求的解
                # 下一轮在[mid+1..hi]搜索
                lo = mid + 1
            else:
                # 如果m<=k, 说明mid可能猜大了，继续查找[lo..mid]有没有更小的子数组和
                hi = mid
        # 循环体退出
        return lo

    def getSplitCnt(self, nums: list, maxItervalSum: int) -> int:
        """计算子数组各自和的最大值为mid时，划分子数组的个数splits
        注意：题目有说是将这个数组分成 m 个非空的“连续”子数组。因此直接遍历nums就可以，一定不能排序打乱原数组顺序！！
        maxItervalSum的取值范围为[max(nums)..sum(nums)]
        """
        # 至少是一个分割
        splits = 1
        # 当前区间的和
        curItervalSum = 0
        for num in nums:
            # 尝试加上当前遍历的这个数，如果加上去超过了「子数组各自的和的最大值」，就不加这个数，另起炉灶
            if curItervalSum + num > maxItervalSum:
                curItervalSum = 0
                splits += 1
            curItervalSum += num
        return splits


# 方法2：动态规划：有点复杂，可以参考官解
class Solution3:
    def splitArray(self, nums: List[int], m: int) -> int:
        length = len(nums)
        # 前缀和，preSum[i] = sum[0..i)
        preSum = [0] * (length + 1)
        # idx     0  1  2  3   4   5
        # nums   [7, 2, 5, 10, 8]
        # preSum [0, 7, 9, 14, 24, 32]
        for i in range(length):
            preSum[i + 1] = preSum[i] + nums[i]

        # 区间 [i..j] 的和 preSum(j + 1) - preSum(i)
        # 1.定义状态
        dp = [[float('inf')] * (m + 1) for _ in range(length)]
        # dp[i][k]表示：将前缀区间 [0, i] 被分成 k 段的各自和的最大值的最小值记为 dp[i][k]，
        # 那么前缀区间 [0, j] （这里 j < i） 被分成 k - 1 段各自和的最大值的最小值为 dp[j][k - 1]。

        # 2.推导状态转移方程
        # dp[i][k]=max(dp[j][k−1],rangeSum(j+1,i))
        # j 的意义是：第 k - 1 个分割的最后一个元素的下标；j 的值需要枚举
        # 这里 rangeSum(j+1,i)表示数组 nums[j + 1..i] 的区间和，
        # 它可以先计算出所有前缀和，然后以 O(1) 的方式计算出区间和。

        # 3.思考初始化
        # 由于要找最小值，初值赋值成为一个不可能达到的很大的值；
        # 分割数为 1 ，即不分割的情况，所有的前缀和就是依次的状态值
        for i in range(length):
            dp[i][1] = preSum[i + 1]

        # 4.思考输出
        # 从分割数为 2 开始递推
        for k in range(2, m + 1):
            # 还未计算出的 i 是从 j 的最小值的下一位开始，因此是 k - 1
            for i in range(k - 1, length):
                # j 表示第 k - 1 个区间的最后一个元素额下标，最小值为 k - 2，最大值为 len - 2（最后一个区间至少有 1 个元素）
                for j in range(k - 2, i):
                    dp[i][k] = min(dp[i][k], max(dp[j][k - 1], preSum[i + 1] - preSum[j + 1]))
        return dp[length - 1][m]


if __name__ == '__main__':
    # nums = [7, 2, 5, 10, 8]
    # k = 2  # 输出18
    nums = [5, 1, 4, 1, 6, 1]
    k = 4  # 输出6
    # print(f(nums, k, 6))
    sol = Solution2()
    print(sol.getSplitCnt(nums, 9))  # 3

