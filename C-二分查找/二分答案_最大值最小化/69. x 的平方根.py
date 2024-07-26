"""
给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。



示例 1：

输入：x = 4
输出：2
示例 2：

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。


提示：

0 <= x <= 231 - 1
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        # B-二分查找: 返回x的平方根，下取整
        if x == 0 or x == 1:
            return x
        # 最大值设置为x一半就够了
        lo, hi = 1, x // 2
        while lo < hi:
            # 写完分支以后调整为向上取整
            mid = (lo + hi + 1) // 2
            # if mid ** 2 > x:
            if mid > x / mid:  # 防止整型溢出
                # mid 以及大于 mid 的数一定不是解，下一轮搜索的区间为 [left, mid - 1]
                hi = mid - 1
            else:
                lo = mid
        return lo


class Solution2:
    def mySqrt(self, x: int) -> int:
        # 暴力解法
        if x == 0 or x == 1:
            return x

        for i in range(1, x + 1):
            # 如果 s 平方以后小于 x ，暂时放过；
            # 如果 s 平方以后等于 x ，直接返回 s
            if i == x / i:
                return i
            # 如果 s 平方以后大于 x ，说明 s - 1 是题目要求的，返回 s - 1 。
            elif i > x / i:
                return i - 1
