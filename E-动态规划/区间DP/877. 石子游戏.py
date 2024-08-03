"""
Alice 和 Bob 用几堆石子在做游戏。一共有偶数堆石子，排成一行；每堆都有 正 整数颗石子，数目为 piles[i] 。
游戏以谁手中的石子最多来决出胜负。石子的 总数 是 奇数 ，所以没有平局。
Alice 和 Bob 轮流进行，Alice 先开始 。 每回合，玩家从行的 开始 或 结束 处取走整堆石头。
这种情况一直持续到没有更多的石子堆为止，此时手中 石子最多 的玩家 获胜 。

假设 Alice 和 Bob 都发挥出最佳水平，当 Alice 赢得比赛时返回 true ，当 Bob 赢得比赛时返回 false 。


示例 1：
输入：piles = [5,3,4,5]
输出：true
解释：
Alice 先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果 Bob 拿走前 3 颗，那么剩下的是 [4,5]，Alice 拿走后 5 颗赢得 10 分。
如果 Bob 拿走后 5 颗，那么剩下的是 [3,4]，Alice 拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对 Alice 来说是一个胜利的举动，所以返回 true 。

示例 2：
输入：piles = [3,7,2,3]
输出：true


提示：
2 <= piles.length <= 500
piles.length 是 偶数
1 <= piles[i] <= 500
sum(piles[i]) 是 奇数
"""
from typing import List

# todo 区间dp
# 类似：486. 预测赢家 完全一样
# 方法1：动态规划

# dp 遍历方法1：先按照左端点i从下往上， 再按照右端点j从左往右 (倒序遍历)
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # 状态 dp[i][j] 定义：区间 piles[i..j] 内先手可以获得的相对分数；
        dp = [[0] * n for _ in range(n)]

        # 状态转移方程：dp[i][j] = max(nums[i] - dp[i + 1, j] , nums[j] - dp[i, j - 1])
        # 在计算状态的时候，一定要保证左边一格和下边一格的值先计算出来。
        # 只遍历矩阵对角线左上半边
        for i in range(n - 1, -1, -1):
            # 与486题不同的是,这里初始化为任意值都可以
            dp[i][i] = piles[i]
            for j in range(i + 1, n):  # 正下方 ， 正左边
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
        
        
        return dp[0][n - 1] > 0


# dp 遍历方法2：先按照右端点j从小到大，在按照左端点i从左到右（斜着遍历）
class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        # 状态 dp[i][j] 定义：区间 piles[i..j] 内先手可以获得的相对分数；
        dp = [[0] * n for _ in range(n)]

        # 状态转移方程：dp[i][j] = max(nums[i] - dp[i + 1, j] , nums[j] - dp[i, j - 1])
        # 在计算状态的时候，一定要保证左边一格和下边一格的值先计算出来。
        # 只遍历矩阵对角线左上半边
        for j in range(n):
            dp[j][j] = piles[j]
            for i in range(j):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][n - 1] > 0


# 方法2：dfs + memo
# 当前自己做出选择的时候，得分为正，留给对方做选择的时候，相对于自己而言，得分为负。
class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        memo = [[-float('inf')] * n for _ in range(n)]

        def dfs(i: int, j: int):
            if i == j:
                return piles[i]
            if memo[i][j] != -float('inf'):
                return memo[i][j]
            chooseLeft = piles[i] - dfs(i + 1, j)
            chooseRight = piles[j] - dfs(i, j - 1)
            res = max(chooseLeft, chooseRight)
            memo[i][j] = res
            return res

        return dfs(0, n - 1) > 0


"""
方法 2：数学方法
这里给出感性的理解，不是严谨的证明。
1.题目说，Alex 总是先手，所以 Alex 总能赢得 2 堆石子时候的游戏。
  这是因为「石子的总数是奇数」，2 堆的时候，Alex 拿较多的那一堆石子让自己获胜；
2.题目又说，石子堆的总数是偶数，所以可以得知 Alex 总可以赢得 4 堆石子时候的游戏。
总之，「为石子的总数是奇数」和「石子堆的总数是偶数」和 Alex 是先手，是 Alex 必胜（没有平局）的必要条件。

"""


class Solution3:
    def predictTheWinner(self, nums: List[int]) -> bool:
        """
        数学解法 —— 博弈论
        ①堆数为偶数 = > 下标为奇数的石子堆数A == 下标为偶数的石子堆数B
        ②石子总和为奇数 = > A中所有石子的总和 != B中所有石子的总和
        ③先手 = > 每一轮拿到的石子堆的下标都和第一轮下标的奇偶性一致
        所以先手玩家只要计算下标为奇数的所有石子堆中石子的总和和下表为偶数的总和，就可以“先下手为强”了
        """
        return True


"""
这是一道博弈论的动态规划问题，同时也是一个区间 dp 问题。
需要注意的是：不管是「动态规划」还是「记忆化递归」，我们这里定义的都是「相对分数」，这种定义是可以推广开来的。
「相对分数」的意思是，我作为先手，得分是正分，而队手得分与我而言是负分。
动态规划在状态转移的过程中，每一步考虑「相对分数」最大，即综合了「正分」和「负分」的结果得出最佳选择。

极小化极大，是博弈论的内容，大概的意思是 我要利润最大化，必须让对方的利润最小；
最大值极小化，是二分查找和动态规划的内容，意思是在所有可能的方案中选一个最大值，看哪一种方案能够使得这个最大值最小：「力扣」第 410 题。

思路分析：每一轮玩家从行的开始或结束处取走整堆石头，决定了这个问题的无后效性，因此可以使用「动态规划」求解。

观察上面的记忆化数组 memo，是一个表格，并且状态转移方程比较容易看出：在拿左边石子堆和右边石子堆中做出对当前最好的选择。
1. 状态 dp[i][j] 定义：区间 piles[i..j] 内先手可以获得的相对分数；
2. 状态转移方程：dp[i][j] = max(nums[i] - dp[i + 1, j] , nums[j] - dp[i, j - 1]) 。
因此，在计算状态的时候，一定要保证左边一格和下边一格的值先计算出来。

说明：
1. i 是区间左边界的下标，j 是区间右边界的下标；
2. 图中黄色部分不填，没有意义。
于是有以下两种填表顺序：
"""

if __name__ == '__main__':
    piles = [5, 3, 4, 5]
    print(Solution().stoneGame(piles))
    # print(Solution1().stoneGame(piles))
    # print(Solution2().stoneGame(piles))
