"""
给定一个二进制数组 nums ，如果最多可以翻转一个 0 ，则返回数组中连续 1 的最大个数。


示例 1：
输入：nums = [1,0,1,1,0]
输出：4
解释：翻转第一个 0 可以得到最长的连续 1。
     当翻转以后，最大连续 1 的个数为 4。
     
示例 2:
输入：nums = [1,0,1,1,0,1]
输出：4


提示:
1 <= nums.length <= 105
nums[i] 不是 0 就是 1.


进阶：如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？
"""
from typing import List

# todo 方法 1：不固定长度滑窗(最优解)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # nums只包含0,1 ，最多可以翻转一个 0，返回数组中连续 1 的最大个数
        ans = 1
        # todo 循环不变量：[l..r]这个滑窗内最多只能有一个 0
        # zero记录滑窗nums[i..j]内0的个数，如果大于1，需要不断左移窗口
        zero = 0

        # 使用 l 和 r 两个指针来表示窗口的左右边界。
        l = 0  
        for r, num in enumerate(nums):
            # 入
            if num == 0:
                zero += 1

            # 出:当窗口内的 0 的个数大于 1 时，移动 l 指针，缩小窗口
            while zero > 1:
                if nums[l] == 0:
                    zero -= 1
                l += 1

            # 更新ans:每次移动 r 指针时，更新最大连续 1 的个数
            ans = max(ans, r - l + 1)

        # 返回最大连续 1 的个数
        return ans
    
    


# 方法 2：前后缀分解，dp => 不能解决：输入的数字是作为 无限流 逐个输入
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # nums只包含0,1 ，最多可以翻转一个 0，返回数组中连续 1 的最大个数
        n = len(nums)
        # 预处理 pre[i] 表示nums以 i 结尾往前延伸最大连续 1 的个数(不含 i)
        pre = [0] * (n+1)
        for i, c in enumerate(nums):
            if c == 1:
                pre[i+1] = pre[i] + 1

        # 预处理 suf[i] 数组表示以 i 开头往后延伸最大连续 1 的个数（包括 i)
        suf = [0] * (n+1)
        for i in range(n-1, -1, -1):
            if nums[i] == 1:
                suf[i] = suf[i+1] + 1

        # 1.如果 nums没有 0
        ans = max(pre)
        # 2.枚举每个 0 的位置，把这个位置变成 1 ，统计它能把前后连成的最多的 1 的个数
        for i, c in enumerate(nums):
            if c == 0:
                ans = max(ans, pre[i]+suf[i+1]+1)

        return ans
