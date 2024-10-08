"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），
返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。
在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，
因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。
因此，在 示例 3 中，输入表示有符号整数 -3。


示例 1：
输入：n = 00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

示例 2：
输入：n = 00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

示例 3：
输入：n = 11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。

提示：
输入必须是长度为 32 的 二进制串 。

进阶：
如果多次调用这个函数，你将如何优化你的算法？
"""


# todo 方法 1：调用二进制库函数
class Solution1:
    def hammingWeight(self, n: int) -> int:
        # 返回整数n其二进制表达式中数字位数为 '1' 的个数
        return n.bit_count()

    def hammingWeight(self, n: int) -> int:
        # 二进制字符串是以 "0b" 开头,如果统计 0 需要在最后结果-1
        return bin(n).count('1')


# TODO 方法 2： n & 1得到二进制末尾是否为 1， 再进行移位操作
class Solution2:
    def hammingWeight(self, n: int) -> int:
        # 返回整数n其二进制表达式中数字位数为 '1' 的个数 (注意，n是无符号整数， 因此不用考虑负数！)
        ans = 0
        while n:
            # 1. 使用 n & 1得到二进制末尾是否为 1；
            ans += n & 1
            # 2. 把 n右移 1 位，直至结束。
            n >>= 1
        return ans


# todo 方法 3：n & (n−1) 消除二进制末尾的 1
# 231. 2 的幂.py
"""
思路及解法:
todo n & (n−1)，其运算结果恰为把 n 的二进制位中的最低位的 1 变为 0 之后的结果。
如：6 & (6−1) = 4
6 = '110', 
6-1 = '101'
6 & (6−1) = '100'

4 = '100' # 运算结果 4 即为把 6 的二进制位中的最低位的 1 变为 0 之后的结果。
4-1 = '011'
4 & (4-1) = '000'

0 = '000' # 运算结果0 即为把 4 的二进制位中的最低位的 1 变为 0 之后的结果。

这样我们可以利用这个位运算的性质加速我们的检查过程，
在实际代码中，我们不断让当前的 n 与 n−1 做与运算，直到 n 变为 0 即可。
因为每次运算会使得 n 的最低位的 1 被翻转，因此运算次数就等于 n 的二进制位中 1 的个数。

复杂度分析
时间复杂度：O(k)，k 为 n 的二进制长度。
空间复杂度：O(1)。
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        # 返回整数n其二进制表达式中数字位数为 '1' 的个数
        # todo n & (n - 1) 可以把 n 的二进制位中的最低位的 1 变为 0
        # 所以可以用一个循环不停地消除 1 同时计数，直到 n 变成 0 为止。
        ans = 0
        while n != 0:
            n &= (n - 1)
            ans += 1
        return ans


if __name__ == '__main__':
    n = 0b11111111111111111111111111111101
    print(Solution().hammingWeight(n))
