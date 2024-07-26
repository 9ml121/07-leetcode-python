"""
给你两个长度相同的字符串，s 和 t。

将 s 中的第 i 个字符变到 t 中的第 i 个字符需要 |s[i] - t[i]| 的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是 maxCost。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 s 的子字符串转化为它在 t 中对应的子字符串，则返回可以转化的最大长度。

如果 s 中没有子字符串可以转化成 t 中对应的子字符串，则返回 0。

 

示例 1：

输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
示例 2：

输入：s = "abcd", t = "cdef", maxCost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。
示例 3：

输入：s = "abcd", t = "acde", maxCost = 0
输出：1
解释：a -> a, cost = 0，字符串未发生变化，所以最大长度为 1。
 

提示：

1 <= s.length, t.length <= 10^5
0 <= maxCost <= 10^6
s 和 t 都只含小写英文字母。
"""

# todo 不固定长度滑窗


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # 返回s的子字符转化为t中对应位置子字符，不超过最大预算maxCost，可以转化的最大长度
        ans = 0
        # [l..r]子数组转化预算不超过maxCost
        cost = 0  # 当前窗口转化预算

        l = 0
        for r in range(len(s)):
            # 入
            cost += abs(ord(s[r]) - ord(t[r]))

            # 出
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            # 更新ans
            ans = max(ans, r-l+1)

        return ans
