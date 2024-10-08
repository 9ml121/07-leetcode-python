"""
描述
某商店规定：三个空汽水瓶可以换一瓶汽水，允许向老板借空汽水瓶（但是必须要归还）。
小张手上有n个空汽水瓶，她想知道自己最多可以喝到多少瓶汽水。

数据范围：输入的正整数满足 1≤n≤100

注意：本题存在多组输入。输入的 0 表示输入结束，并不用输出结果。

输入描述：
输入文件最多包含 10 组测试数据，每个数据占一行，仅包含一个正整数 n（ 1<=n<=100 ），表示小张手上的空汽水瓶数。n=0 表示输入结束，你的程序不应当处理这一行。

输出描述：
对于每组测试数据，输出一行，表示最多可以喝的汽水瓶数。如果一瓶也喝不到，输出0。

输入：
3
10
81
0

输出：
1
5
40

说明：
样例 1 解释：用三个空瓶换一瓶汽水，剩一个空瓶无法继续交换
样例 2 解释：用九个空瓶换三瓶汽水，剩四个空瓶再用三个空瓶换一瓶汽水，剩两个空瓶，向老板借一个空瓶再用三个空瓶换一瓶汽水喝完得一个空瓶还给老板
"""


# 解法1：递归 + 备忘录
def solution1(n):
    # 备忘录
    memo = dict()
    def fun(n: int) -> int:
        # 查备忘录,避免重复计算
        if n in memo:
            res = memo[n]

        # 0个或者1个空瓶换不了
        if n == 0 or n == 1:
            res = 0
        # 2个空瓶可以借一个，换1瓶，最后剩下的1个空瓶还掉
        elif n == 2:
            res = 1
        # 3个以上空瓶,递归过程
        else:
            res = fun(n % 3 + n // 3) + (n // 3)

        # 存入备忘录
        memo[n] = res
        # 返回结果
        return res

    # 调试
    print(memo)
    print(fun(n))


# 测试
# solution1(7)

# 解法2：dp
def solution2(n: int):
    n = 7
    dp = [0] * (n + 1)
    # base case
    dp[0] = dp[1] = 0
    dp[2] = 1
    # dp方程式
    for i in range(3, n + 1):
        dp[i] = dp[i % 3 + i // 3] + i // 3
    print(dp[n])
    # print(dp)


# 解法3：找规律
'''
知道这题优秀的解法，我真是裂开了。 
题目描述中有讲到：剩2个空瓶子时，可以先找老板借一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。 
也就是说2个空瓶子即可换一瓶汽水喝，而且喝完之后手里也没有空瓶子。求解时直接把空瓶数除以2，即可得到正解。
'''
n = int(input())
print(n//2)