"""
https://www.acwing.com/problem/content/2/
给你一个可装载重量为 W 的背包和 n 个物品，每个物品有重量和价值两个属性。
每件物品只能使用一次。
其中第 i 个物品的重量为 w[i]，价值为 values[i]，

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

举个简单的例子，输入如下
n = 3, W = 4
w = [2, 1, 3]
values = [4, 2, 3]

算法返回 6，选择前两件物品装进背包，总重量 3 小于 W，可以获得最大价值 6。
题目就是这么简单，一个典型的动态规划问题。这个题目中的物品不可以分割，要么装进包里，要么不装，不能说切成两块装一半。
这就是 0-1 背包这个名词的来历。
"""
from typing import List

'''
        0 1 2 3 4  # 背包容量
0       0 0 0 0 0
2:4     0 0 4 4 4
1:2     0 2          
3:3     0 0           
# 物品重量:价值
'''


def backpack01(W: int, weights: List[int], values: List[int]) -> int:
    N = len(weights)
    # 1.状态有两个，就是「背包的容量」和「可选择的物品」。
    # 2.todo dp[i][w]表示对于前 i 个物品，当前背包的容量为 w，这种情况下可以装的最大价值。
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # 3.第三步，根据「选择」，思考状态转移的逻辑。
    for i in range(1, N + 1):  # 从wt[0],即i=1开始，i代表物品重量和价值的索引
        for w in range(1, W + 1):  # 从w=1开始,w代表背包容量
            # 3.1 选择不装：最大价值为前i-1个商品，容量为w能获得的最大价值
            dp[i][w] = dp[i - 1][w]
            # 3.2 能够装下
            # 可以选择不装：前i-1个商品在当前容量能获得的最大价值
            # 可以选择装入背包：当前商品价值 + 当前容量减去当前商品重量，剩下重量对于前i-1个商品能获得的最大价值(每个商品只能装一次)
            # 取两者价值最大值
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
                # 由于数组索引从 0 开始，而我们定义中的 i 是从 1 开始计数的，
                # 所以 values[i-1] 和 w[i-1] 表示第 i 个物品的价值和重量。

    # 4.返回最大价值
    return dp[N][W]


# 空间优化方法 1：滚动数组
def backpack02(W: int, weights: List[int], values: List[int]) -> int:
    N = len(weights)
    if N == 0:
        return 0
    dp = [[0] * (W + 1) for _ in range(2)]
    # 注意：这里 i 从 1 开始，到 N 结束，N 可以取到
    for i in range(1, N + 1):
        for w in range(W + 1):
            dp[i % 2][w] = dp[(i - 1) % 2][w]
            if weights[i - 1] <= w:
                dp[i % 2][w] = max(dp[i % 2][w], dp[(i - 1) % 2][w - weights[i - 1]] + values[i - 1])

    return dp[N % 2][W]


# 空间优化方法 2：使用一维数组「逆序」填表（难点、重点）
def backpack03(W: int, weights: List[int], values: List[int]) -> int:
    N = len(weights)
    if N == 0:
        return 0
    dp = [0] * (W + 1)

    for i in range(N):
        # 注意：这里[W ..weights[i]]是要都能够取到的
        for j in range(W, weights[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    # print(dp)
    return dp[W]


if __name__ == '__main__':
    # W = 4
    # w = [2, 1, 3]
    # v = [4, 2, 3]

    w = [4, 3, 1, 1]
    v = [300, 200, 150, 200]
    W = 5
    # print(backpack01(W, w, v))  # 6 550
    # print(backpack02(W, w, v))  # 6 550
    print(backpack03(W, w, v))  # 6 550
