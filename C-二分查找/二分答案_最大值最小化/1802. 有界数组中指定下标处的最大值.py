"""
给你三个正整数 n、index 和 maxSum 。你需要构造一个同时满足下述所有条件的数组 nums（下标 从 0 开始 计数）：

nums.length == n
nums[i] 是 正整数 ，其中 0 <= i < n
abs(nums[i] - nums[i+1]) <= 1 ，其中 0 <= i < n-1
nums 中所有元素之和不超过 maxSum
nums[index] 的值被 最大化
返回你所构造的数组中的 nums[index] 。

注意：abs(x) 等于 x 的前提是 x >= 0 ；否则，abs(x) 等于 -x 。

 

示例 1：

输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。
示例 2：

输入：n = 6, index = 1,  maxSum = 10
输出：3
 

提示：

1 <= n <= maxSum <= 10^9
0 <= index < n
"""

# todo 二分查找 + 数学
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # 返回符合条件的nums[index]最大数

        def get(mid: int, cnt: int):
            # 总共有cnt个数，最大数为mid，计算所有数总和
            if mid >= cnt:
                # 1.nums = [2，3], cnt=2, mid=3
                # 左边数为mid - cnt + 1 >= 1, [mid - cnt + 1..mid], 步长为1的等差数列求和
                total = (mid + mid - cnt + 1) * cnt // 2
            else:
                # 2.nums=[1,1,2,3], cnt=4,mid=3
                # 多余1的个数为n-mid, 剩余数是[1..mid]，步长为1的等差数列求和
                total = (mid+1) * mid // 2 + cnt - mid

            return total

        # ans最大化可能的最小值和最大值
        lo = maxSum // n
        hi = maxSum - (n-1)
        ans = lo
        while lo <= hi:
            mid = (lo+hi) // 2
            # nums[0..index]单调递增
            # nums[index..n-1]单调递减
            if get(mid, index+1) + get(mid, n-index) - mid <= maxSum:
                ans = mid
                lo = mid+1
            else:
                hi = mid-1

        return ans
