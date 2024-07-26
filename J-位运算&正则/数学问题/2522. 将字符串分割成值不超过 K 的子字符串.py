"""
给你一个字符串 s ，它每一位都是 1 到 9 之间的数字组成，同时给你一个整数 k 。

如果一个字符串 s 的分割满足以下条件，我们称它是一个 好 分割：

s 中每个数位 恰好 属于一个子字符串。
每个子字符串的值都小于等于 k 。
请你返回 s 所有的 好 分割中，子字符串的 最少 数目。如果不存在 s 的 好 分割，返回 -1 。

注意：

一个字符串的 值 是这个字符串对应的整数。比方说，"123" 的值为 123 ，"1" 的值是 1 。
子字符串 是字符串中一段连续的字符序列。


示例 1：

输入：s = "165462", k = 60
输出：4
解释：我们将字符串分割成子字符串 "16" ，"54" ，"6" 和 "2" 。每个子字符串的值都小于等于 k = 60 。
不存在小于 4 个子字符串的好分割。
示例 2：

输入：s = "238182", k = 5
输出：-1
解释：这个字符串不存在好分割。


提示：

1 <= s.length <= 105
s[i] 是 '1' 到 '9' 之间的数字。
1 <= k <= 109
"""


# 方法 1：动态规划
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:

        n = len(s)
        dp = [1] * (n + 1)
        dp[0] = 0

        lenK = len(str(k))

        for j in range(lenK, n + 1):  # [1..n]
            i = j - lenK + 1
            sub_num = int(s[i - 1:j])
            if sub_num > k:
                if lenK == 1:
                    return -1
                dp[j] = dp[i] + 1
            else:
                dp[j] = dp[i - 1] + 1

        # print(dp)
        return dp[n]


# 方法2：贪心(推荐！！)
# 思考：第一个字符串应该划分在哪？
# 如果给后面留下的字符串越短，答案显然不会变大，因此第一个字符串越长越好。
class Solution2:
    def minimumPartition(self, s: str, k: int) -> int:
        ans = 1
        x = 0
        for v in map(int, s):  # s = "165462", k = 60
            if v > k:
                return -1
            x = x * 10 + v
            if x > k:
                ans += 1
                x = v
        return ans
