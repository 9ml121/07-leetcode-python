"""
给你一个下标从 0 开始的整数数组 nums ，你必须将数组划分为一个或多个 连续 子数组。

如果获得的这些子数组中每个都能满足下述条件 之一 ，则可以称其为数组的一种 有效 划分：
子数组 恰 由 2 个相等元素组成，例如，子数组 [2,2] 。
子数组 恰 由 3 个相等元素组成，例如，子数组 [4,4,4] 。
子数组 恰 由 3 个连续递增元素组成，并且相邻元素之间的差值为 1 。例如，子数组 [3,4,5] ，但是子数组 [1,3,5] 不符合要求。
如果数组 至少 存在一种有效划分，返回 true ，否则，返回 false 。

 

示例 1：

输入：nums = [4,4,4,5,6]
输出：true
解释：数组可以划分成子数组 [4,4] 和 [4,5,6] 。
这是一种有效划分，所以返回 true 。
示例 2：

输入：nums = [1,1,1,2]
输出：false
解释：该数组不存在有效划分。
 

提示：

2 <= nums.length <= 105
1 <= nums[i] <= 106
"""


"""
todo §6.1 判定能否划分
一般定义 𝑓[𝑖] 表示长为 𝑖 的前缀 𝑎[:𝑖] 能否划分。
枚举最后一个子数组的左端点 L，从 f[L] 转移到 f[i]，并考虑 a[L:j] 是否满足要求。
● 2369. 检查数组是否存在有效划分 1780
● 139. 单词拆分

# 思路
如何想出状态定义？
    如果 nums 的最后两个数相等，那么去掉这两个数，问题变成剩下 n−2 个数能否有效划分。
    如果 nums 的最后三个数相等，那么去掉这三个数，问题变成剩下 n−3 个数能否有效划分。
    如果 nums 的最后三个数是连续递增的，那么去掉这三个数，问题变成剩下 n−3 个数能否有效划分。
我们要解决的问题都形如「nums 的前 i 个数能否有效划分」。

于是定义 f[0]=true，f[i+1] 表示能否有效划分 nums[0] 到 nums[i]。

根据有效划分的定义，有

f[i+1]= ∨
    f[i−1] ∧ nums[i]=nums[i−1],i>0
    f[i−2] ∧ nums[i]=nums[i−1]=nums[i−2],i>1
    f[i−2] ∧ nums[i]=nums[i−1]+1=nums[i−2]+2,i>1
 
答案为 f[n]。

作者：灵茶山艾府
链接：https://leetcode.cn/problems/check-if-there-is-a-valid-partition-for-the-array/solutions/1728735/by-endlesscheng-8y73/
"""

class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        # 判断数组 nums是否可以按照规则有效划分
        n = len(nums)
        # 定义 f[0]=true，f[i+1] 表示能否有效划分 nums[0] 到 nums[i]。
        f = [True] + [False] * n

        for i, x in enumerate(nums):
            if i >= 1 and f[i-1] and nums[i-1] == x or \
                    i >= 2 and f[i-2] and (nums[i-2] == nums[i-1] == x or nums[i-2] == nums[i-1]-1 == x-2):
                f[i+1] = True

        # print(f)
        return f[-1]
