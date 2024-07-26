"""
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

你必须设计并实现线性时间复杂度的算法且使用常数级空间来解决此问题。



示例 1：
输入：nums = [2,2,3,2]
输出：3

示例 2：
输入：nums = [0,1,0,1,0,1,99]
输出：99


提示：
1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次
"""
import collections
from typing import List


# 方法1：利用哈希字典，空间复杂度为O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # nums除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
        freq = collections.Counter(nums)
        return [num for num, occ in freq.items() if occ == 1][0]


# todo 方法2：位运算和计数
"""
https://leetcode.cn/problems/single-number-ii/solutions/2482832/dai-ni-yi-bu-bu-tui-dao-chu-wei-yun-suan-wnwy/
暴力思路
设只出现一次的那个数为 x。用二进制思考：
- 如果 x 的某个比特是 0，由于其余数字都出现了 3 次，所以 nums 的所有元素在这个比特位上的 1 的个数是 3 的倍数。
- 如果 x 的某个比特是 1，由于其余数字都出现了 3 次，所以 nums 的所有元素在这个比特位上的 1 的个数除 3 余 1。
这启发我们统计每个比特位上有多少个 1。下图比较了 136. 只出现一次的数字 与本题的异同：
136.只出现一次的数字    137.只出现一次的数字二
nums = [6,6,3]       nums = [6,6,6,3]
                     110
110                  110
110                  110
011                  011
----累加每个比特位     ----累加每个比特位
231                  341
----模2              ----模3
011                  011

由于异或运算本质上是在每个比特位上做模2加法，所以136题可以用异或解决
137题则需要统计每个比特位的1的个数，或者用位运算实现模3加法
"""



class Solution2:
    # 空间复杂度O(N)
    def singleNumber(self, nums: List[int]) -> int:
        # nums除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。
        # 使用一个长度为32的数组 count，统计数组中所有数字在每个位上出现的次数。
        count = [0] * 32

        # 遍历数组 nums，对于每个数字，更新 count 数组的相应位上的计数。
        for num in nums:
            for i in range(32):
                count[i] += num & 1  # num & 1：结果是num二进制最后一位
                num >>= 1

        # 对 count 数组的每个位上的计数进行取余操作（对3取余）,构建出只出现一次数字的二进制表示。
        ans = 0
        for i in range(32):
            ans |= (count[i] % 3) << i  # 恢复第 i 位的值到 ans

        # 将二进制表示转换为十进制
        if ans >= 2 ** 31:  # 负数的处理
            ans -= 2 ** 32

        return ans


    # 空间复杂度O(1)
    def singleNumber2(self, nums: List[int]) -> int:
        ans = 0
        for i in range(31):
            cnt = sum((x >> i) & 1 for x in nums)
            ans |= cnt % 3 << i
        
        cnt = sum(x >> 31 & 1 for x in nums)
        return ans - (cnt % 3 << 31)  # 符号位
