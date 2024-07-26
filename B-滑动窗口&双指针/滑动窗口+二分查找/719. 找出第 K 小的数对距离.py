"""
数对 (a,b) 由整数 a 和 b 组成，其数对距离定义为 a 和 b 的绝对差值。

给你一个整数数组 nums 和一个整数 k ，数对由 nums[i] 和 nums[j] 组成且满足 0 <= i < j < nums.length 。
返回 所有数对距离中 第 k 小的数对距离。

 

示例 1：

输入：nums = [1,3,1], k = 1
输出：0
解释：数对和对应的距离如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
距离第 1 小的数对是 (1,1) ，距离为 0 。
示例 2：

输入：nums = [1,1,1], k = 2
输出：0
示例 3：

输入：nums = [1,6,1], k = 3
输出：5
 

提示：
n == nums.length
2 <= n <= 10^4
0 <= nums[i] <= 10^6
1 <= k <= n * (n - 1) / 2
"""

# todo 二分答案 + 滑动窗口


class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        # 返回 所有数对距离中 第 k 小的数对距离。
        nums.sort()
        n = len(nums)

        def count_less_equals(limit:int):
            # 统计距离（数值之差的绝对值）小于等于 limit 的个数
            ans = 0
            l = 0
            for r in range(n):
                # 出
                while nums[r] - nums[l] > limit:
                    l += 1
                    
                # 此时满足 nums[right] - nums[left] <= limit
                # right 与 [left..right - 1] 里的每一个元素的「距离」都小于等于 limit
                # [left..right - 1] 里元素的个数为 right - left
                ans += r - l

            return ans

        # 第k小的数对距离可能的最小值和最大值
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            count = count_less_equals(mid)

            if count < k:
                # 如果小于等于 mid 的个数严格小于 k 个，说明 mid 太小了
                # 下一轮搜索区间为 [mid + 1..right]
                lo = mid + 1
            else:
                # 下一轮搜索区间为 [left..mid]
                # 注意这里要想清楚为什么count>= k, ans可能是mid
                hi = mid

        return lo
    

"""
1.暴力解法
计算所有的数对的距离，时间复杂度 O(N^2)，这里 N是输入数组的长度；
再排序，时间复杂度 O(NlogN)；
最后找到第 k 小的数，时间复杂度：O(1)。题目的意思是相同距离也参与排序，排序以后找到的元素下标是 k−1。
因此，暴力解法总的时间复杂度是：O(N^2 + NlogN + 1) = O(N^2)。


"""