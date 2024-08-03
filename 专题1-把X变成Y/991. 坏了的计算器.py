"""
在显示着数字 startValue 的坏计算器上，我们可以执行以下两种操作：

双倍（Double）：将显示屏上的数字乘 2；
递减（Decrement）：将显示屏上的数字减 1 。
给定两个整数 startValue 和 target 。返回显示数字 target 所需的最小操作数。



示例 1：

输入：startValue = 2, target = 3
输出：2
解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}.
示例 2：

输入：startValue = 5, target = 8
输出：2
解释：先递减，再双倍 {5 -> 4 -> 8}.
示例 3：

输入：startValue = 3, target = 10
输出：3
解释：先双倍，然后递减，再双倍 {3 -> 6 -> 5 -> 10}.


提示：

1 <= startValue, target <= 109
"""


# 逆向思维:对 startValue 执行乘 2 或 减 1 操作，等价于对 target 执行除 2（当 target 是偶数时）或者加 1 操作。
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # 当 target 大于 startValue 时，如果它是奇数，我们执行加法操作，否则执行除法操作。
        # 之后，我们需要执行 startValue - target 次加法操作以得到 startValue
        ans = 0
        while target > startValue:
            ans += 1
            if target % 2:
                target += 1
            else:
                target //= 2

        return ans + startValue - target
