"""
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。



示例 1：
输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。

示例 2：
输入：x = 3, y = 1
输出：1


提示：
0 <= x, y <= 2^31 - 1
"""

# todo 二进制 ^ 异或运算

# 内置位计数功能
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # 两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。
        # 也就是x,y代表的二进制进行 异或 运算，最后结果二进制中1的个数就是答案
        return format(x ^ y, 'b').count('1')


class Solution1:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        tmp = x ^ y  # 亦或运算，二进制相同为0，不同为1

        # 统计整数tmp二进制中位1的个数： leetcode 191题
        while tmp:
            res += tmp & 1
            tmp >>= 1
        return res


class Solution2:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        tmp = x ^ y  # 亦或运算，二进制相同为0，不同为1

        # 统计整数tmp二进制中位1的个数： leetcode 191题
        while tmp != 0:
            tmp &= (tmp - 1)
            res += 1
        return res
