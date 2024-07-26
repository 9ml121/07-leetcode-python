"""
给你一个 正 整数 n 。

用 even 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的偶数下标的个数。

用 odd 表示在 n 的二进制形式（下标从 0 开始）中值为 1 的奇数下标的个数。

返回整数数组 answer ，其中 answer = [even, odd] 。

 

示例 1：

输入：n = 17
输出：[2,0]
解释：17 的二进制形式是 10001 。 
下标 0 和 下标 4 对应的值为 1 。 
共有 2 个偶数下标，0 个奇数下标。
示例 2：

输入：n = 2
输出：[0,1]
解释：2 的二进制形式是 10 。 
下标 1 对应的值为 1 。 
共有 0 个偶数下标，1 个奇数下标。
 

提示：

1 <= n <= 1000
"""


from typing import List


# todo 方法一：二进制基本操作
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        ans = [0, 0]
        i = 0
        # 不断取最低位，然后右移，直到等于 0 为止，这样可以取到每个比特位。
        while n:
            ans[i] += n & 1
            n >>= 1
            i ^= 1
        return ans


# 方法二：位掩码 + 库函数
# 利用位掩码 0x55555555（二进制的 010101⋯），取出偶数下标比特和奇数下标比特，分别用库函数统计 1 的个数。
# 本题由于 n 范围比较小，取 0x5555 作为位掩码。
#  5 =【101】=> 取偶下标，5 >> 1 = 【010】取奇下标
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        MASK = 0x5555
        return [(n & MASK).bit_count(), (n & (MASK >> 1)).bit_count()]


# 方法 3：转换为字符串解法
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even = odd = 0
        s = bin(n)[2:]
        m = len(s)
        for i, c in enumerate(s):
            if c == '1':
                if (m-1-i) % 2 == 0:
                    even += 1
                else:
                    odd += 1
        return [even, odd]
