"""
描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个 n 级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

数据范围：1≤n≤40
要求：时间复杂度：O(n) ，空间复杂度： O(1)

输入：
2
返回值：
2
说明：
青蛙要跳上两级台阶有两种跳法，分别是：先跳一级，再跳一级或者直接跳两级。因此答案为2

输入：
7
返回值：
21
"""

"""
分析：
n个台阶，每次可以选择跳1，或者2个台阶，问跳上n层有多少种不同的跳法？
这类问题往往可以用动态规划或者递归来解决。

用递归的时间复杂度一般比动态规划要大一些，这一题要求时间复杂度：O(n) ，空间复杂度： O(1)，所以可以选择动态规划  

解法1：递归
优点:代码简单好写，
缺点：慢，会超时 
时间复杂度：O(2^n) 
空间复杂度：递归栈的空间
"""


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution2:
    def jumpFloor(self, number: int) -> int:
        # write code here
        if number == 1 or number == 2:
            return number
        else:
            return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)


# 测试
# cls = Solution2()
# res = cls.jumpFloor(35)
# print(res)

"""
解法2：用动态规划: 实际上就是斐波拉契数列： 1，2，3，5，8，13
    1。需要把前2步的结果存下来，确定边界值
    2。动态转移方程式：dp[i] = dp[i - 1] + dp[i - 2]
    3. 结果就是dp数组最后一个值
# 时间复杂度：O(n)
# 空间复杂度：O(n)

解法3：
 因为最后结果只依赖上2步计算的结果，所以可以只用3个整数变量存储历史值+当前值
 时间复杂度：O（n） 
 空间复杂度：O（1）
"""


class Solution:
    def jumpFloor(self, number: int) -> int:
        # dp = [0] * (number + 1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range(3, number + 1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[number]

        # 进一步优化：
        a, b = 0, 1  # 上两个值
        curr = 0  # 当前值
        for i in range(1, number + 1):
            curr = a + b
            a = b
            b = curr
            # print(curr)
        return curr


# 测试
cls = Solution()
res = cls.jumpFloor(5)
print(res)
