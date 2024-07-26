"""
有一个背包，背包的最大承重为 W，还有 N 种物品，每种物品有两个属性：重量和价值，每种物品有无限多个。
现在需要选择一些物品装入背包，在不超过背包最大承重的前提下，应该尽量使得装入背包的物品的价值总和最大，求最大价值总和是多少。

输入格式：
    - 第 1 行只有一个整数，表示背包的最大承重；
    - 第 2 行是每种物品重量列表 weights ，使用空格隔开；
    - 第 3 行是第 2 行每种物品对应的价值列表 values，使用空格隔开。

输出格式：
    输出一个整数，表示最大价值总和。

示例：
输入：
7
3 4 2
40 50 30

输出：
100

解释：
背包最大承重为 7，可以选择第 1 种物品 1 件、 第 3 种物品 2 件装入背包，总重量为3+2×2，总价值最大，为 40+30×2=100。

提示：
1 <= W <= 20000；
1 <= N <= 100；
1 <= weights[i] <= 1000​；
1 <= values[i] <= 1000。
"""


# 参考代码 1：这一版代码的时间复杂度很高，存在重复计算。
# 时间复杂度：O(NW^2，这里 N 是背包价值数组的长度， W 是背包的容量，使用了三重循环；
def backpackComplete(W: int, weights: list, values: list) -> int:
    N = len(weights)  # 物品数量
    # dp[i][j] 表示：考虑物品区间 [0..i] 里，不超过背包容量 j，能够获得的最大价值总和，由于包含价值为 0 的计算，所以 + 1
    dp = [[0] * (W + 1) for _ in range(N)]
    # 初始化第一行
    # 当只有 1 个物品的时候，只要当前物品的重量的 整数倍数 的物品的重量总和不超过最大承重，都可以装入背包。
    # 因此初始化的时候需要枚举下标为 0 的物品在当前限制的最大承重下可以装入多少个
    for k in range(W // weights[0] + 1):
        dp[0][weights[0] * k] = values[0] * k

    for i in range(1, N):
        for j in range(W + 1):
            # 多一个 for 循环，枚举下标为 i 的物品可以选择的个数
            for k in range(j // weights[i] + 1):
                dp[i][j] = max(dp[i][j], dp[i - 1][j - k * weights[i]] + k * values[i])

    # print(dp)
    # 输出：二维表格最后一个状态的值。
    return dp[N - 1][W]


# 参考代码2：使用优化的状态转移方程（二维数组）
# 时间复杂度：O(NW，这里 N 是背包价值数组的长度， W 是背包的容量)
def backpackComplete2(W: int, weights: list, values: list) -> int:
    N = len(weights)  # 物品数量
    # dp[i][j] 表示：考虑物品区间 [0..i] 里，不超过背包容量 j，能够获得的最大价值总和
    # 由于包含价值为 0 的计算，所以 + 1
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # 优化
    for i in range(1, N + 1):
        for j in range(W + 1):
            # 至少是上一行抄下来
            dp[i][j] = dp[i - 1][j]
            # 「完全背包」参考当前行的值
            if j >= weights[i - 1]:
                dp[i][j] = max(dp[i][j], dp[i][j - weights[i - 1]] + values[i - 1])
    # print(dp)
    return dp[-1][-1]


# 参考代码 3：优化空间（一维数组）：「正序填表」
def backpackComplete3(W: int, weights: list, values: list) -> int:
    N = len(weights)  # 物品数量
    # dp[j] 表示：不超过背包容量 j，能够获得的最大价值总和
    dp = [0] * (W + 1)

    # 优化空间
    for i in range(1, N + 1):
        # 细节1，j 从 weights[i - 1] 开始遍历
        # 细节2.跟0-1背包不同的是，这里是正序遍历
        for j in range(weights[i - 1], W + 1):
            dp[j] = max(dp[j], dp[j - weights[i - 1]] + values[i - 1])
    # print(dp)
    return dp[-1]


if __name__ == '__main__':
    # 处理输入
    # W = int(input())
    # weights = list(map(int, input().split(" ")))
    # values = list(map(int, input().split(" ")))
    # print(backpackComplete(W, weights, values))

    W = 7
    weights = [3, 4, 2]
    values = [40, 50, 30]
    print(backpackComplete3(W, weights, values))  # 100

"""
W 0  1  2   3   4   5   6   7
[[0, 0, 0,  40, 0,  0,  80, 0],    weight[0] = 3
 [0, 0, 0,  40, 50, 50, 80, 90],   weight[1] = 4
 [0, 0, 30, 40, 60, 70, 90, 100]]  weight[2] = 2
"""
