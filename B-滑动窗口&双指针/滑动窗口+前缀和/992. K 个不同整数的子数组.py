"""
给定一个正整数数组 nums和一个整数 k，返回 nums 中 「好子数组」 的数目。

如果 nums 的某个子数组中不同整数的个数恰好为 k，则称 nums 的这个连续、不一定不同的子数组为 「好子数组 」。

例如，[1,2,3,1,2] 中有 3 个不同的整数：1，2，以及 3。
子数组 是数组的 连续 部分。

 

示例 1：
输入：nums = [1,2,1,2,3], k = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

示例 2：
输入：nums = [1,2,1,3,4], k = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
 

提示：

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""
import collections

# todo 方法1：不定长滑窗 + 前缀和思想, exactK = atMostK(k) - atMostK(k - 1)
# 类似： A-滑动窗口&双指针\滑动窗口\计数问题\795. 区间子数组个数.py
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        # 返回nums中子数组中不同元素个数正好为k的子数组数量

        def atMostK(k: int)-> int:
            # 返回nums不同元素个数最多为k的子数组数量
            res = 0
            # todo [l..r]窗口内不同元素个数<=k
            freq = collections.Counter()

            l = 0
            for r,  x in enumerate(nums):
                # 入
                if freq[x] == 0:
                    k -= 1
                freq[x] += 1

                # 出
                while k < 0:
                    freq[nums[l]] -= 1
                    if freq[nums[l]] == 0:
                        k += 1
                    l += 1

                # 更新ans, 以nums[r]结尾的子数组个数为r-l+1
                res += r-l+1
            return res

        # todo 转化：恰好 k 个不同整数的子数组 = 最多 k 个不同整数的子数组 - 最多 k-1 个不同整数的子数组。
        # 这样转化是因为，最多 k 个不同整数的子数组，最多问题我们已经有了处理相关问题的经验了
        return atMostK(k) - atMostK(k-1)
