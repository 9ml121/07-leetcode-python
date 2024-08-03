"""
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。



示例 1：
输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

示例 2：
输入：n = 3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
示例 3：

输入：n = 4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3


提示：
0 <= n <= 30
"""


# 方法1：递归 时间复杂度：O(2^n) 空间复杂度：O(1)
# 0112358
def fib1(n: int) -> int:
    # 0 <= n <= 30
    # base case
    if n == 0 or n == 1:
        return n
    # recursion
    return fib1(n - 1) + fib1(n - 2)


# 方法2、带备忘录的递归解法： 备忘录一般使用字典或数组
# 0112358
memo = {}


def fib2(n: int) -> int:
    # 1.base case
    if n == 0 or n == 1:
        return n
    # 2.查备忘录,避免重复计算
    else:
        res = fib2(n - 1) + fib2(n - 2)

    # 3.记到备忘录
    memo[n] = n if n == 0 or n == 1 else res
    return memo[n]


# 方法3：dp: 时间复杂度：O(n)  空间复杂度：O(n)
# 0112358
def fib3(n: int):
    if n == 0: return n
    # 定义dp
    dp = [0] * (n + 1)

    for i in range(n + 1):
        # base case
        if i == 0 or i == 1:
            dp[i] = i
        # 状态转移
        elif i >= 2:
            dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# 方法3优化空间复杂度：因为dp状态转移方程式只用到前面2个数，所以只需要记录前2个数即可，空间复杂度可降到0(1)
def fib4(n: int):
    # base case
    if n == 0 or n == 1:
        return n
    # 分别代表 dp[i - 1] 和 dp[i - 2]
    pre = 1
    prepre = 0
    for i in range(2, n + 1):
        # 01 12358  # dp[i] = dp[i - 1] + dp[i - 2];
        cur = pre + prepre
        # 滚动更新
        prepre = pre
        pre = cur
    return pre


if __name__ == '__main__':
    print(fib1(4))
    print(fib2(4))
    print(fib3(4))
    print(fib4(4))
