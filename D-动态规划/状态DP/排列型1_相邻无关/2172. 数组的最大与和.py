"""
给你一个长度为 n 的整数数组 nums 和一个整数 numSlots ，满足2 * numSlots >= n 。总共有 numSlots 个篮子，编号为 1 到 numSlots 。

你需要把所有 n 个整数分到这些篮子中，且每个篮子 至多 有 2 个整数。一种分配方案的 与和 定义为每个数与它所在篮子编号的 按位与运算 结果之和。

比方说，将数字 [1, 3] 放入篮子 1 中，[4, 6] 放入篮子 2 中，这个方案的与和为 (1 AND 1) + (3 AND 1) + (4 AND 2) + (6 AND 2) = 1 + 1 + 0 + 2 = 4 。
请你返回将 nums 中所有数放入 numSlots 个篮子中的最大与和。

 

示例 1：

输入：nums = [1,2,3,4,5,6], numSlots = 3
输出：9
解释：一个可行的方案是 [1, 4] 放入篮子 1 中，[2, 6] 放入篮子 2 中，[3, 5] 放入篮子 3 中。
最大与和为 (1 AND 1) + (4 AND 1) + (2 AND 2) + (6 AND 2) + (3 AND 3) + (5 AND 3) = 1 + 0 + 2 + 2 + 3 + 1 = 9 。
示例 2：

输入：nums = [1,3,10,4,7,1], numSlots = 9
输出：24
解释：一个可行的方案是 [1, 1] 放入篮子 1 中，[3] 放入篮子 3 中，[4] 放入篮子 4 中，[7] 放入篮子 7 中，[10] 放入篮子 9 中。
最大与和为 (1 AND 1) + (1 AND 1) + (3 AND 3) + (4 AND 4) + (7 AND 7) + (10 AND 9) = 1 + 1 + 3 + 4 + 7 + 8 = 24 。
注意，篮子 2 ，5 ，6 和 8 是空的，这是允许的。
 

提示：

n == nums.length
1 <= numSlots <= 9
1 <= n <= 2 * numSlots
1 <= nums[i] <= 15
"""


from typing import List


"""
1.转换一下：视作有 2⋅numSlots 个篮子，每个篮子至多可以放 1 个整数
2.用二进制数 mask 表示这 2⋅numSlots 个篮子中放了数字的篮子集合，
  其中 mask 从低到高的第 i 位为 1 表示第 i 个篮子放了数字，为 0 表示第 i 个篮子为空。
3.设 mask 的二进制中的 1 的个数为 c
  定义f[mask] 表示将 nums 的前 c 个数字放到篮子中，且放了数字的篮子集合为 mask 时的最大与和。
  初始值 f[0]=0。
4.考虑将 nums[c] 放到一个空篮子时的状态转移方程（下标从 0 开始，此时 nums[c] 还没被放入篮中），
  我们可以枚举 mask 中的 0，即空篮子的位置 i，该空篮子对应的编号为i//2 + 1
5.设 nums 的长度为 n，最后答案为 max(f)。

代码实现时需要注意，若 c≥n 则 f[mask] 无法转移，需要跳过。
相似题目：1879. 两个数组最小的异或值之和.py
"""
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        f = [0] * (1 << (numSlots * 2))

        for mask, fi in enumerate(f):
            c = mask.bit_count()
            if c >= len(nums):
                continue
            for i in range(numSlots * 2):
                if mask & (1 << i) == 0:  # 枚举空篮子 i
                    s = mask | (1 << i)
                    f[s] = max(f[s], fi + (nums[c] & (i//2 + 1)))

        return max(f)
