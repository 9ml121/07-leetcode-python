"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？
返回满足题意的二叉搜索树的种数。

示例 1：
   1         1         2         3         3
    \         \       / \       /         /
     3         2     1   3     2         1
    /           \             /           \
   2             3           1             2
输入：n = 3
输出：5

示例 2：
输入：n = 1
输出：1

提示：
1 <= n <= 19
"""

'''
分析思路：先暴力枚举
1. n=1 ==> res=1
    root=1 l=# r=# 
2. n=2 ==> res=2
    root=1 l=# r=2  
    root=2 l=1 r=# 
3. n=3 ==> res=5
    root=1
        l=# r=2/3 sub=2
    root=2
        l=1 r=3 sub=1
    root=3
        l=1/2 r=# sub=2
通过以上枚举，可以发现有很多重复子问题，结果都是一样的：
    1. 根节点有[1..n]种可能
    2. 左节点因为要小于根节点，假设 root=i, 那么左子树有[1..i-1]种可能
    3. 同样逻辑，右子树有[i+1..n]种可能
典型的 dp 问题。
    1.dp边界分析：因为左右子树可能为空，也就意味着空节点也算一种可能，dp[0]=dp[1]=1
    2.dp[i]定义：以 [1..i]为根节点，能够构建的总数量为 dp[i]
    3.最后求以[1..n]为根节点，能够构建的总数量为 dp[n], 也就是返回 dp[-1]
    4.状态转移方程式：当前根节点可以构建的数量= 左子树可以构建的数量 * 右子树可以构建的数量
                    dp[3] = dp[0] * dp[2] + dp[1] * dp[1] + dp[2] * dp[0]
                ==》 dp[i] = ∑ dp[j] * dp[i - j - 1], 其中 j ∈ [0..i)  
'''


# 方法 1：动态规划解法
class Solution:
    def numTrees(self, n: int) -> int:
        """计算[1..n]组成二叉搜索树的种类数"""
        # dp[i]表示以[1..i]为根节点能构建的二叉搜索树的数量为 dp[i]
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]


# 方法 2：递归解法
# 递归的计算左边可能的数量，右边可能的数量，二者相乘即为当前以值i为root节点的二叉搜索树数量
class Solution2:
    def numTrees(self, n: int) -> int:
        """ 计算闭区间 [1, n] 组成的 BST 个数"""
        memo = {}  # 记忆化搜索树的数量

        def dfs(minV, maxV):
            """返回当前以值i为root节点的二叉搜索树数量"""
            # 边界: 如果只有0，或者1个节点，则可能的子树情况为1种
            if minV > maxV:
                return 1
            if (minV, maxV) in memo:
                return memo[(minV, maxV)]

            cnt = 0
            # todo cnt为什么定义为局部变量而不是全局变量？
            for i in range(minV, maxV + 1):
                left = dfs(minV, i - 1)
                right = dfs(i + 1, maxV)
                cnt += left * right

            memo[(minV, maxV)] = cnt
            return cnt

        return dfs(1, n)


if __name__ == '__main__':
    print(Solution().numTrees(3))
