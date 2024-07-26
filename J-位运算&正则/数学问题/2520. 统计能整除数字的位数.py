"""
给你一个整数 num ，返回 num 中能整除 num 的数位的数目。
如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。

示例 1：
输入：num = 7
输出：1
解释：7 被自己整除，因此答案是 1 。

示例 2：
输入：num = 121
输出：2
解释：121 可以被 1 整除，但无法被 2 整除。由于 1 出现两次，所以返回 2 。

示例 3：
输入：num = 1248

输出：4
解释：1248 可以被它每一位上的数字整除，因此答案是 4 。


提示：
1 <= num <= 10^9
num 的数位中不含 0
"""


# 枚举数位问题
class Solution:
    # 方法 1：将整数转换为字符串
    def countDigits2(self, num: int) -> int:
        s = str(num)
        res = 0
        for i in range(len(s)):
            digit = int(s[i])
            if num % digit == 0:
                res += 1
        return res

        # return sum(num % int(i) == 0 for i in str(num))  # 简单写法

    # 方法 2：数学运算(推荐！！)
    def countDigits(self, num: int) -> int:
        res = 0
        n = num
        while n > 0:  # n = 121
            digit = n % 10  # 1 ==> 2 ==> 1(从低位到高位)
            if num % digit == 0:
                res += 1

            # res += n % (num % 10) == 0  # 简单写法
            n //= 10  # 121 ==> 12 ==> 1  ==> 0
        return res
