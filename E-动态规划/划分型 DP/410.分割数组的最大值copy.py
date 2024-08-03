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
0 <= nums[i] <= 10^6
1 <= m <= min(50, nums.n)
"""
from typing import List

# todo 二分查找 | 动态规划

# todo 方法1：二分答案（推荐！）
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 将数组nums分割为k个子数组，求各种分割方式中各个子数组中的最大值的最小值
        n = len(nums)
        # 1.当k=n, 也就是nums每个数都是一个子数组，此时子数组和的最大值最小，为max(nums)
        lo = max(nums)
        # 2.当k=1,也就是nums划分为一个子数组，此时子数组和的最大值最大，为sum(nums)
        hi = sum(nums)
        
        def getSplitCnt(limit: int) -> int:
            """计算子数组各自和的最大值为limit时，划分子数组的个数splits"""
            splits = 1  # 至少是一个分割
            cur_sum = 0  # 当前区间的和
            for num in nums:
                # 尝试加上当前遍历的这个数，如果加上去超过了「子数组各自的和的最大值」，就不加这个数，另起炉灶
                if cur_sum + num > limit:
                    cur_sum = 0
                    splits += 1
                cur_sum += num

            return splits
        
        # 3.当1 < k < n，子数组各自和的最大值一定介入[lo..hi]之间
        while lo < hi:
            mid = (lo + hi) >> 1
            # 计算子数组各自和的最大值为mid时，可以划分的子数组最少个数splits
            splits = getSplitCnt(mid)
            if splits > k:
                # 1.划分子数组个数多了，也就是mid猜小了，mid和mid左边一定不是要求的解
                # 下一轮在[mid+1..hi]搜索
                lo = mid + 1
            else:
                # 2.如果splits <= k, 说明mid可能猜大了，继续查找[lo..mid]有没有更小的子数组和
                hi = mid
        
        return lo


# todo 方法2: 区间dp + 前缀和
"""
§6.3 约束划分个数
将数组分成（恰好/至多）𝑘 个连续子数组，计算与这些子数组有关的最优值。
一般定义 𝑓[𝑖][𝑗] 表示将长为 𝑗 的前缀a[:j] 分成 𝑖 个连续子数组所得到的最优解。
枚举最后一个子数组的左端点 𝐿，从 𝑓[𝑖−1][𝐿]转移到 𝑓[𝑖][𝑗]，并考虑 𝑎[𝐿:𝑗] 对最优解的影响。
"""
class Solution2:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 将数组nums分割为k个子数组，求各种分割方式中各个子数组中的最大值的最小值
        n = len(nums)
        # todo dp[i][j] 表示下标[0..i]分割成 j 个非空连续子数组所得到的子数组中的最大值的最小值。
        dp = [[float('inf')] * (k + 1) for _ in range(n)]

        pre_sum = [0] * (n + 1)  # 前缀和数组,pre_sum[i]代表nums[i+1]之前的元素和
        for i in range(n):
            pre_sum[i + 1] = pre_sum[i] + nums[i]
            # 下标[0..i]分割成 1 个非空连续子数组
            dp[i][1] = pre_sum[i + 1]

        for i in range(1, n):  # 从子数组[0..1],枚举到[0..n-1]
            for j in range(2, min(i + 1, k) + 1):  # 分割子数组数,从2个开始，最多min(k, i+1)个
                for t in range(j - 2, i):  # t枚举最后一个子数组的起点
                    max_val = max(dp[t][j - 1], pre_sum[i + 1] - pre_sum[t + 1])
                    dp[i][j] = min(dp[i][j], max_val)

        return dp[n - 1][k]




# 二分答案写法2
class Solution3:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 将数组nums分割为k个子数组，求各种分割方式中各个子数组中的最大值的最小值
        n = len(nums)
        # 1.当k=n, 也就是nums每个数都是一个子数组，此时子数组和的最大值最小，为max(nums)
        lo = max(nums)
        # 2.当k=1,也就是nums划分为一个子数组，此时子数组和的最大值最大，为sum(nums)
        hi = sum(nums)
        
        # 判断可不可能将nums分为k个子数组，使得子数组各自和都<=limit
        def canSplit(k:int, limit:int)->bool:
            # 每次分割都尽量把limit用完，最后判断k=0的时候nums还有没有剩余元素
            i = 0
            while i < n:
                if k == 0:
                    return False
        
                tmp = limit
                while i < n and tmp >= nums[i]:
                    tmp -= nums[i]
                    i += 1
                k -= 1
            return True

        # 3.当1 < k < len(nums)，子数组各自和的最大值一定介入[max(nums)..sum(nums)]之间，因为nums给的是非负整数
        while lo < hi:
            mid = (lo + hi) >> 1
            if self.canSplit(nums, k, mid):
                hi = mid  # 继续减少midV
            else:
                # 增大mid: 子数组和的最大值的最小值越大，数组分法就越多
                lo = mid + 1
        return lo

# dp + 不用前缀和:超时
class Solution4:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # dp[i][j] 表示将数组的前 i 个元素分割成 j 个非空连续子数组所得到的子数组中的最大值的最小值。
        dp = [[float('inf')] * (k + 1) for _ in range(n)]
        # 初始化：如果 j == 1，表示当前位置只需分割为一个子数组，即整个数组作为一个子数组，此时 dp[i][j] 的值为当前位置前面所有元素的和
        dp[0][1] = nums[0]
        for i in range(1, n):
            dp[i][1] = dp[i - 1][1] + nums[i]

        for i in range(1, n):  # i代表数组的前 i 个元素
            for j in range(2, min(i + 2, k + 1)):  # j代表分割的子数组个数
                for t in range(j - 2, i):  # 分成2段以上，k枚举最后一段的分割点
                    # 将数组的前 t 个元素分割为 j-1 个子数组，
                    # 将位置 t+1 到位置 i 的元素作为第 j 个子数组。
                    # 计算这2个数组的最大值 max_val
                    max_val = max(dp[t][j - 1], sum(nums[t + 1:i + 1]))
                    # 更新 dp[i][j] 的值为所有 max_val 中的最小值。
                    dp[i][j] = min(dp[i][j], max_val)
        # 最终，dp[n-1][m] 即为分割数组的最大值的最小值，其中 n 是数组 nums 的长度。
        return dp[n - 1][k]


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    k = 2  # 输出18
    # nums = [5, 1, 4, 1, 6, 1]
    # k = 4  # 输出6
    print(Solution().splitArray(nums, k))
    print(Solution2().splitArray(nums, k))
    print(Solution3().splitArray(nums, k))
    print(Solution4().splitArray(nums, k))
