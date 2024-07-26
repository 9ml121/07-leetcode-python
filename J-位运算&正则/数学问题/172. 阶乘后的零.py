"""
给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1


示例 1：
输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0

示例 2：
输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0

示例 3：
输入：n = 0
输出：0


提示：
0 <= n <= 10^4


进阶：你可以设计并实现对数时间复杂度的算法来解决此问题吗？
"""






# todo 数论
"""返回 n! 结果中尾随零的数量, 设计并实现对数时间复杂度的算法来解决此问题
https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/easy/172.factorial-trailing-zeroes
通过观察，我们发现如果想要结果末尾是 0，必须是分解质因数之后，2 和 5 相乘才行， 同时因数分解之后发现 5 的个数远小于 2，
因此我们只需要求解这 n 数字分解质因数之后 一共有多少个 5 即可.

我们的结果并不是直接 f(n) = n/5, 比如 n 为 30， 25 中是有两个 5 的。类似，n 为 150，会有 7 个这样的数字。
其中 f(n) = n/5 其实仅表示分解出的质因数仅包含一个 5 的个数。而我们的答案是质 因数中所有的 5 。
因此等价于 f(n) = n/5 + n/25 + n/125 + ... + n/5^k  (5^k 表示 质因数中有 k 个 5 的个数)
据此得出转移方程：f(n) = n/5 + n/5^2 + n/5^3 + n/5^4 + n/5^5+..
"""

class Solution:
    # 循环写法
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n >= 5:
            n //= 5
            count += n

        return count

    # 递归写法
    def trailingZeroes2(self, n: int) -> int:
        if n == 0:
            return 0
        return n // 5 + self.trailingZeroes(n // 5)