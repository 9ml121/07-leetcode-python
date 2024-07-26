"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。

完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。

示例 1：
输入：n = 12
输出：3
解释：12 = 4 + 4 + 4

示例 2：
输入：n = 13
输出：2
解释：13 = 4 + 9

提示：
1 <= n <= 10^4
"""
import collections
import math

"""
                「力扣」第 279 题	            完全背包问题
物品	             完全平方数：0、1、4、9、16	    每一个物品
物品的个数	     每个数可以重复使用	        每个物品的使用不限次数
限制	             总和 恰好等于 n    	        所有物品的体积（重量）之和不超过背包重量
目标	             使用的完全平方数的个数最少	    所有物品的价值最大

"""


# 方法 1：完全背包（空间优化）
class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] 表示正整数 i 最少需要的完全平方数个数。
        # 初始值赋值为不可能达到的一个最大数 n+1。
        # 根据四平方定理，也可以设置为 4
        dp = [n + 1] * (n + 1)
        # dp[0] = 0 的合理性：表达式 1 + dp[i - j * j] = 1 ，表示它自己就是一个完全平方式，所以结果是 0
        dp[0] = 0

        # 递推开始，一个一个求，自底向上
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1

        # print(dp)
        return dp[n]


# 方法 1：完全背包（性能优化）
class Solution1:
    def numSquares(self, n: int) -> int:
        # 初始值赋值为不可能达到的一个最大数 n+1。
        dp = [n + 1] * (n + 1)
        dp[0] = 0

        # n = 13
        # 外层循环：从[1..n最大平方跟]开始遍历
        for i in range(1, int(math.sqrt(n)) + 1):  # 1,2,3 => 1,4,9
            # 内存循环：从i的平方开始更新
            for j in range(i * i, n + 1):
                dp[j] = min(dp[j], dp[j - i * i] + 1)
            # print(dp)
            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            # [0, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4,  5,  3,  4]
            # [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2,  3,  3,  2]
        return dp[-1]


# 方法 2：广度优先遍历
class Solution2:
    def numSquares(self, n: int) -> int:
        dq = collections.deque([n])
        visited = [False] * (n + 1)
        visited[0] = True

        step = 1
        while dq:
            level_size = len(dq)
            for _ in range(level_size):
                top = dq.popleft()

                i = 1
                while i * i <= top:
                    remain = top - i * i
                    if remain == 0:
                        return step
                    if not visited[remain]:
                        dq.append(remain)
                        visited[remain] = True
                    i += 1
            step += 1


# 方法 3：自顶向下递归
# 略


if __name__ == '__main__':
    n = 13
    print(Solution1().numSquares(n))  # 2
