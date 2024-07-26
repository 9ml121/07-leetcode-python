"""
有一堆石头，用整数数组 stones 表示。其中 stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：

如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。



示例 1：

输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。
示例 2：

输入：stones = [31,26,33,21,40]
输出：5


提示：

1 <= stones.length <= 30
1 <= stones[i] <= 100
"""
from typing import List

"""
思路分析：
本题的关键字是「选出 任意两块石头」中的「任意」（区别于 1046. 最后一块石头的重量）；
「粉碎的可能结果」的规则可以概括为：两块石头粉碎以后得到的石头的重量为两块石头重量的差的绝对值；

其实当前问题和 494. 目标和 一样，只不过目标为「添加了正号和负号以后的和的最小值」。
该问题与 494. 目标和 的等价性说明如下：

假设两块石头的重量分别为 a 和 b（这里假设 a > b），粉碎以后得到的石头的重量为 a - b；
假设第 3 块石头的重量为 c，它与上一步得到的石头的重量为 c - (a - b) = c - a + b，这里假设 c > a - b；
可以依次推理下去，因此当前问题可以转化为给所有的石头加上正负号以后得到的和的最小值。
根据
    pos + neg = sum
和
    pos - neg = target
这里 target 为最后得到的石头的重量。

两式相加，得 2 * sum(所有添加正号的数) = sum + target，整理得：
target = 2 * sum(所有添加正号的数) - sum 
题目要求的是 target 最小值。上式中 sum 是固定值，等价于求解 sum(所有添加正号的数) 的最小值，它的值是 0 吗？不是。这是因为根据题意，必需保证 target > 0。即：
2 * sum(所有添加正号的数) - sum >= 0 即 2 * sum(所有添加正号的数) >= sum，
这一点相当于什么都没有说，这是因为根据题意 sum(所有添加正号的数) >= sum(所有添加负号的数)。

上面的分析说明：我们将两个式子相加，虽然减少了不确定的变量，不能得到约束条件。为此，我们尝试将两个等式相减，得
2 * sum(所有添加负号的数) = sum - target
得 target = sum - 2 * sum(所有添加负号的数)，又由于 target >= 0，可得 sum(所有添加负号的数) <= sum / 2。

这是 限制条件，因此该问题是一个「0-1 背包问题」：让我们从输入数组中找出一些数，每个数只能使用一次，并且这些数的和不能超过 sum / 2，并且它们的「和」最大，
这样才能使得 target = sum - 2 * sum(所有添加负号的数) 的值最小。

我们建议大家自己归纳这个问题的「状态设计」「状态转移方程」「初始化」「输出」。对于它们的描述作为注释放在「参考代码 1」中。
"""


# 方法1：
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 求剩余石头的最小重量，可以转换为取i个石头，使其和最接近sum(stones)//2，
        sumV = sum(stones)
        target = sumV // 2
        n = len(stones)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        # dp[i][j] 表示：从输入数组的前缀区间 [0..i] 里取出一部分元素，并且和小于等于 j 的最大值

        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if stones[i - 1] <= j:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - stones[i - 1]] + stones[i-1])

        print(dp)
        return sumV - 2 * dp[n][target]


# 思路2：chatgpt
class Solution2:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 求剩余石头的最小重量，可以转换为取i个石头，使其和最接近sum(stones)//2，
        target = sum(stones) // 2
        n = len(stones)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # dp[i][j] 表示是否能在前 i 个石头中选择一些石头，使得它们的总重量恰好为 j
        dp[0][0] = True

        for i in range(1, n + 1):
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if stones[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - stones[i - 1]]

        # print(dp)
        for j in range(target, -1, -1):
            if dp[n][j]:
                return sum(stones) - j * 2


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]  # 1
    print(Solution().lastStoneWeightII(stones))
    # print(Solution2().lastStoneWeightII(stones))
