"""
当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。
给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。

示例 1:
输入: n = 10
输出: 9

示例 2:
输入: n = 1234
输出: 1234

示例 3:
输入: n = 332
输出: 299

提示:
0 <= n <= 10^9
"""


# 方法 1：贪心 + 数学
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        size = len(str(n))
        if size <= 1:
            return n

        # 1332  1203  1032
        pre_digit = n % 10
        res = pre_digit
        # 从低位到高位遍历
        for i in range(1, size):
            cur_digit = (n // 10 ** i) % 10
            if cur_digit > pre_digit:
                res = cur_digit * (10 ** i) - 1
                pre_digit = cur_digit - 1
            else:
                res += cur_digit * (10 ** i)
                pre_digit = cur_digit

        return res


# 写法 2：
class Solution1:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # 将数字先转换为字符串，再转换为数字数组
        arr = list(map(int, str(n)))
        size = len(arr)
        # print(arr)  # [1,3,3,2]
        i = 1
        while i < size and arr[i - 1] <= arr[i]:
            i += 1

        # n本身就是单调递增
        if i == size:
            return n

        # 此时来到了第一个满足 arr[i - 1] > arr[i] 的位置
        # 再往回找，来到一连串等于下降起始位置的第一个数位，让它减 1，特殊用例：333218 -> 29999
        while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1

        arr[i] -= 1
        for j in range(i + 1, size):
            arr[j] = 9

        return int(''.join(map(str, arr)))


if __name__ == '__main__':
    n = 1332
    print(Solution1().monotoneIncreasingDigits(n))
