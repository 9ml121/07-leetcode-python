"""
假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 perm（下标从 1 开始），只要满足下述条件 之一 ，该数组就是一个 优美的排列 ：

perm[i] 能够被 i 整除
i 能够被 perm[i] 整除
给你一个整数 n ，返回可以构造的 优美排列 的 数量 。

 

示例 1：

输入：n = 2
输出：2
解释：
第 1 个优美的排列是 [1,2]：
    - perm[1] = 1 能被 i = 1 整除
    - perm[2] = 2 能被 i = 2 整除
第 2 个优美的排列是 [2,1]:
    - perm[1] = 2 能被 i = 1 整除
    - i = 2 能被 perm[2] = 1 整除
示例 2：

输入：n = 1
输出：1
 

提示：

1 <= n <= 15
"""

from collections import defaultdict
from functools import cache


# todo 基础解法：全排列/回溯，时间复杂度：O(n!)

class Solution:
    def countArrangement(self, n: int) -> int:
        # 1.预处理每个位置的符合条件的数有哪些
        dic = defaultdict(list)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i % j == 0 or j % i == 0:
                    dic[i].append(j)

        # print(matched)

        # 2.used数组/集合 标记哪些数被使用过,依次尝试向位置1->n填数
        used = set()

        def dfs(i: int = 1) -> int:
            if i == n+1:
                return 1

            res = 0
            for x in dic[i]:
                if x not in used:
                    used.add(x)
                    res += dfs(i+1)
                    used.remove(x)
            return res

        return dfs()


# todo 进阶解法：状态压缩 + 动态规划，时间复杂度：O(n×2^n)
# 1.用一个位数为 n 的二进制数 mask 表示排列中的数被选取的情况。
# 2.若 mask 中的第 i 位为 1（从 0 开始编号），则数 i+1 已经被选取，否则就还未被选取
# 3.n 中 1 的个数 m 代表前 m 位已放置
# 例如：二进制 100110 共三个1，代表排列的前三位已放置数字，三个1分别在二进制第 1、2、5位置上(从右侧开始，从0开始计数）, 所以 2、3、6三个数字被选取
# 综合起来就是表示：2 3 6 这三个数字被放到了排列的前三位，三个数字完美排列方式未知，通过枚举 mask 进行计算

class Solution:
    def countArrangement(self, n: int) -> int:
        # 用来存储中间结果，f[6] = f[000110] = 数字2、3在前两位时的完美排列数量
        f = [0] * (1 << n)
        f[0] = 1
        
        # 通过 mask 进行枚举，最终目的是为了得到二进制 mask = (11..11)n 时，总的完美排列数
        for mask in range(1, 1 << n):
            # i 代表排列的前i位已放置数字,枚举1->n是否可以放到第 i 位（i 从 1 开始）
            i = mask.bit_count()
            # 遍历 mask 的每一位，仍以 mask = 100110 为例，此 mask 代表 2 3 6三个数字在排列的前三位
            # 求三个数字 2 3 6 的完美排列方式，则先确定2 3 6哪些数字能放到第三位，然后累加另外两个数字的完美排列数量来获得
            # 2 3 6，第三位可以为 6，则 f[100110] += f[000110] (2、3在前两位时的完美排列数量)
            # 2 3 6，第三位可以为 3，则 f[100110] += f[100010] (2、6在前两位时的完美排列数量)
            for j in range(1, n+1):
                # mask>>(j-1) & 1 用来判断 mask 第 j 位是否为 1，如果为 1，说明第 j 个数字被选取
                # 也可以写成 mask & (1<<(j-1))
                # (j % i == 0 or i % j == 0) 判断被选取的数字 j 能否放到位置 i 上
                # 即：先从被选取的数字中找到能放到最高位 i 的数字，然后将剩余 i-1 个数字的完美排列方式累加到f[mask]中
                if mask >> (j-1) & 1 and (j % i == 0 or i % j == 0):
                    # mask ^ (1 << (j-1)) 将 mask 第 j 位设置为 0
                    f[mask] += f[mask ^ (1 << (j-1))]

        return f[(1 << n) - 1]


# todo 递归解法
class Solution:
    def countArrangement(self, n: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(s: int) -> int:
            # 定义 dfs(S) 表示在可以选的数字集合为 S 的情况下，可以构造的优美排列的数量
            if s == 0:
                return 1
            
            res = 0
            #  i 等于集合 S 的大小
            i = s.bit_count()
            for j in range(1, n + 1):
                if s >> (j - 1) & 1 and (i % j == 0 or j % i == 0):
                    res += dfs(s ^ (1 << (j - 1)))
            return res
        
        return dfs((1 << n) - 1)


"""
暴力做法是枚举所有排列，对每个排列计算和题目有关的值，时间复杂度（通常来说）是O(n⋅n!)。可以解决 𝑛≤10 的问题。
状压 DP 可以把时间复杂度（通常来说）优化至 O(n⋅2^n)。可以解决 𝑛≤20 的问题。
"""