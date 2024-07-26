"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。
返回符合要求的 最少分割次数 。

示例 1：
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

示例 2：
输入：s = "a"
输出：0

示例 3：
输入：s = "ab"
输出：1


提示：
1 <= s.length <= 2000
s 仅由小写英文字母组成
"""

# todo 计算划分个数
"""
计算最少（最多）可以划分出的子数组个数、划分方案数等。
一般定义 𝑓[𝑖]表示长为 𝑖的前缀 𝑎[:𝑖] 在题目约束下，分割出的最少（最多）子数组个数（或者定义成分割方案数）。
枚举最后一个子数组的左端点 𝐿，从 𝑓[𝐿]转移到 𝑓[𝑖]，并考虑 𝑎[𝐿:𝑗] 对最优解的影响。
"""

# dp方法1：dp遍历时，判断是否为回文字符串，并同时更新最小分割次数
class Solution:
    def minCut(self, s: str) -> int:
        # 将 s 分割成回文子串的最小分割次数
        n = len(s)

        # todo 1.dp_check[i][j]用来判断s[i..j]是否为回文串，「力扣」第 5 题：最长回文子串
        dp_check = [[False] * n for _ in range(n)]

        # todo 2.dp_minCut[i] 表示s[0..i] 分割成若干个回文子串所需要最小分割次数。
        # 状态转移方程式: dp[i] = min([dp[j] + 1 for j in range(i) if s[j + 1, i] 是回文])
        dp_minCut = [i for i in range(n)]

        # todo3 先升序遍历列，再升序遍历行，按照列进行填值
        for j in range(n):
            for i in range(j+1):  # 注意这里i要遍历到j, 因为dp_minCut是要参考对角线坐标值
                if s[i] == s[j] and (j - i + 1 <= 3 or dp_check[i + 1][j - 1]):
                    dp_check[i][j] = True

                    # 这里dp_minCut[j]是滚动更新的, 找最小切割次数
                    if i == 0:
                        # s[0..j]是回文串，最小切割次数为0
                        dp_minCut[j] = 0
                    else:
                        # i >= 1, 当前位置切割次数是在dp_minCut[i - 1]基础上+1
                        dp_minCut[j] = min(dp_minCut[j], dp_minCut[i - 1] + 1)

        return dp_minCut[-1]


# dp方法2：分2步遍历
class Solution2:
    def minCut(self, s: str) -> int:
        # 将 s 分割成回文子串的最小分割次数
        n = len(s)

        # 1.先判断s[i..j]是否为回文串，得到一个预处理的动态规划数组dp_check
        dp_check = [[False] * n for _ in range(n)]

        # 先升序遍历列，再升序遍历行，按照列进行填值
        for j in range(n):
            for i in range(j+1):
                dp_check[i][j] = (s[i] == s[j]) and (
                    j - i + 1 <= 3 or dp_check[i + 1][j - 1])

        # 2.再判断最小分割次数 abaab  abca
        # dp[i]表示前缀子串 s[0..i]的最少分割次数，初始化为每个位置最大分割次数
        dp_minCut = [i for i in range(n)]

        for i in range(n):
            if dp_check[0][i]:
                dp_minCut[i] = 0
                continue
            
            # 枚举分割点
            dp_minCut[i] = min([dp_minCut[j] + 1 for j in range(i)
                                if dp_check[j + 1][i]])

        return dp_minCut[-1]



if __name__ == '__main__':
    s = 'abba'
    s2 = 'aabab'
    print(Solution().minCut(s2))
    print(Solution2().minCut(s2))
