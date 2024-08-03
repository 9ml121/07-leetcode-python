"""
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。
请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

示例 1：
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。

示例 2：
输入：nums = [9], target = 3
输出：0


提示：

1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000


进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？
"""
from typing import List

"""
解题思路

常见的背包问题有
1、组合问题。
2、True、False问题。
3、最大最小问题。 
以下题目整理来自大神CyC，github地址： https://leetcode.cn/link/?target=https%3A%2F%2Fgithub.com%2FCyC2018%2FCS-Notes%2Fblob%2Fmaster%2Fnotes%2FLeetcode%20%E9%A2%98%E8%A7%A3%20-%20%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92.md%230-1-%E8%83%8C%E5%8C%85 

我在大神整理的基础上，又做了细分的整理。分为三类。 
1、组合问题： 377. 组合总和 Ⅳ 494. 目标和 518. 零钱兑换 II 
2、True、False问题： 139. 单词拆分 416. 分割等和子集 
3、最大最小问题： 474. 一和零 322. 零钱兑换

# 组合问题公式
dp[i] += dp[i-num]

# True、False问题公式
dp[i] = dp[i] or dp[i-num]

# 最大最小问题公式
dp[i] = min(dp[i], dp[i-num]+1) 或者 dp[i] = max(dp[i], dp[i-num]+1)

以上三组公式是解决对应问题的核心公式。
"""


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i - num < 0:
                    break
                else:
                    dp[i] += dp[i - num]

        return dp[target]
