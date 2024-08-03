"""
给定一个正整数 n ，你可以做如下操作：

如果 n 是偶数，则用 n / 2替换 n 。
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。
返回 n 变为 1 所需的 最小替换次数 。



示例 1：

输入：n = 8
输出：3
解释：8 -> 4 -> 2 -> 1
示例 2：

输入：n = 7
输出：4
解释：7 -> 8 -> 4 -> 2 -> 1
或 7 -> 6 -> 3 -> 2 -> 1
示例 3：

输入：n = 4
输出：2


提示：

1 <= n <= 231 - 1
"""
from functools import cache


# 方法 1：专题1-把X变成Y
class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        if n % 2 == 0:
            return self.integerReplacement(n // 2) + 1
        else:
            return min(self.integerReplacement(n // 2), self.integerReplacement(n // 2 + 1)) + 2


# 方法 2：贪心
class Solution2:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            # 1.当 n 为偶数时，我们只有唯一的方法将 n 替换为 n//2
            if n % 2 == 0:
                ans += 1
                n //= 2

            # 2.当 n 为奇数时，n 除以 4 的余数要么为 1，要么为 3
            elif n % 4 == 1:
                # 2.1 如果为 1，我们可以断定，应该将 n 变成(n-1)//2
                ans += 2
                n //= 2
            else:
                # 2.2 如果为 3，我们可以断定，应该将 n 变成(n+1)//2, 但是要把 n=3除外
                if n == 3:
                    ans += 2
                    n = 1
                else:
                    ans += 2
                    n = n // 2 + 1
        return ans
