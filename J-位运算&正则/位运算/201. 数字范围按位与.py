"""
给你两个整数 left 和 right ，表示区间 [left, right] ，返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。


示例 1：
输入：left = 5, right = 7
输出：4

示例 2：
输入：left = 0, right = 0
输出：0

示例 3：
输入：left = 1, right = 2147483647
输出：0


提示：
0 <= left <= right <= 2^31 - 1
"""


# 方法1：按照 n & (n-1) 来消除n最末尾的1
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）
        while left < right:
            right &= (right - 1)  # 消除right最末尾的1

        return right


# 方法2：求出两个给定数字的二进制字符串的公共前缀，这里给出的第一个方法是采用位移操作
class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）
        shift = 0
        # 计算两个二进制字符串的公共前缀
        while left < right:  # left = right 递归终止
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
