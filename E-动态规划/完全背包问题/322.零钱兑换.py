"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。
你可以认为每种硬币的数量是无限的。

示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1

示例 2：
输入：coins = [2], amount = 3
输出：-1

示例 3：
输入：coins = [1], amount = 0
输出：0


提示：
1 <= coins.n <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""
import collections
from typing import List

'''
转换成为「完全背包问题」：
1.可以将问题转换成为恰好装入容量为 amount 的背包，
  注意：这里的 amount 视为容量、体积，理解成「完全背包」中的「限制条件」；
2.可以选择物品就是题目给出的硬币，「你可以认为每种硬币的数量是无限的」决定了这是一个「完全背包问题」；
3.标准的「完全背包问题」问的是「总价值最大」，「总价值」是「目标」，
  本题问的是使用的「硬币总数」最少，「硬币总数」是「目标」，最优子结构类似；
4.由于要找最小值，因此初始化的时候可以将状态的值赋值成为一个不可能的较大值，这里选择 amount + 1。

套用「完全背包问题」的模型，参考代码如下:
'''


# 方法1：完全背包写法1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        # dp[i]表示当目标金额为 i 时，至少需要硬币数量
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        # 先遍历金额，在遍历硬币
        for w in range(1, amount+1):
            for coin in coins:
                if w < coin:
                    break

                if w >= coin and dp[w-coin] != float('inf'):
                    dp[w] = min(dp[w], dp[w-coin] + 1)
                    
        
        # print(dp)
        return dp[-1] if dp[-1] != float('inf') else -1



# 方法1：完全背包写法2
class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i]表示当目标金额为 i 时，至少需要硬币数量
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # 先遍历硬币，在遍历金额
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i - coin] + 1, dp[i])
                    
        # 如果结果是初始值，则表示没有找到解。
        return -1 if dp[amount] == float('inf') else dp[amount]


# 方法2：自顶向下--递归dfs + 备忘录
class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 备忘录
        memo = dict()

        def dfs(n):
            # 查备忘录，避免重复计算
            if n in memo:
                return memo[n]
            # base case
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('INF')
            for coin in coins:
                # 计算子问题的结果
                subproblem = dfs(n - coin)
                if subproblem != -1:
                    res = min(res, 1 + subproblem)

            # 把计算结果存入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dfs(amount)


# 方法 3：BFS
class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # 使用的数据结构是队列；
        dq = collections.deque([amount])
        # 在图结构中的遍历，由于有环的存在，需要使用布尔数组或者哈希表 visited 记录图中结点是否访问过；
        visited = [False] * (amount + 1)
        visited[0] = True
        # 排序是为了加快广度优先遍历过程中，对硬币面值的遍历，起到剪枝的效果
        coins.sort()

        step = 1
        while dq:
            level_size = len(dq)
            for _ in range(level_size):
                money = dq.popleft()
                for coin in coins:
                    remain = money - coin
                    if remain == 0:
                        return step
                    if remain < 0:
                        # 由于 coins 升序排序，后面的面值会越来越大，后面的硬币就不用再看了
                        break
                    if not visited[remain]:
                        dq.append(remain)
                        # 添加到队列的时候，就应该立即设置为 true，否则还会发生重复访问
                        visited[remain] = True
            step += 1

        # 进入队列的顶点都出队，都没有看到 0，表示凑不出当前面值
        return -1


# 拓展 =》贪心算法
"""
下面我们给出「贪心选择性质」成立的解释，为了突出直观，我们不使用严谨的数学证明。
由于候选纸币（硬币）的面值为 [1, 2, 5, 10, 20, 50, 100]，这样的数列有如下性质：
1.首先，一定有 1，这样可以保证对任意一种金额都存在找零钱方案；
2.其次，较大面值的纸币（硬币），一定可以等价地替换成为比它面值更小的纸币（硬币）的组合；
3.更重要的是：较大面值的纸币（硬币）的面值一定 大于等于 它 2 倍比它面值 小一点 的纸币（硬币）的面值，例如：
    100=2×50、
    50=2×20+10、
    20=2×10、
    10=2×5、
    5=2×2+1、
    2=2×1。
以上的 3 点性质决定了，如果我们可以使用较小的金额的纸币（硬币）的组合替换一张较大的纸币（硬币），
我们一定要这样做，才会让最后兑换的纸币（硬币）数量最少。
"""

if __name__ == '__main__':
    cls = Solution()
    coins = [1, 2, 3]
    amount = 6
    # coins = [1]
    # amount = 0
    # coins = [7, 4, 2]
    # amount = 3
    # coins = [186, 419, 83, 408]
    # amount = 6249
    print(cls.coinChange(coins, amount))
