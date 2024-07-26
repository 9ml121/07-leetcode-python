"""
给你一个字符串 s ，请你返回满足以下条件且出现次数最大的 任意 子串的出现次数：

子串中不同字母的数目必须小于等于 maxLetters 。
子串的长度必须大于等于 minSize 且小于等于 maxSize 。
 

示例 1：

输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。
示例 2：

输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。
示例 3：

输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3
示例 4：

输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0
 

提示：

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s 只包含小写英文字母。
"""


from collections import Counter

# todo 方法2：枚举（可行性优化）
# 时间复杂度：O(NS)，其中 N 是字符串的长度，S 是 minSize 和 maxSize 的数量级,在本题中为 26
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # 返回满足以下条件且出现次数最大的 任意 子串的出现次数:
        # - 子串中不同字母的数目必须小于等于 maxLetters
        # - 子串的长度必须大于等于 minSize 且小于等于 maxSize
        n = len(s)
        ans = 0
        # freq代表符合条件子串的出现次数, ans代表符合条件子串最多出现次数
        freq = Counter()
        ans = 0

        # 枚举每个子串可以的开始位置
        for i in range(n-minSize+1):
            # todo 如果一个子串在字符串中出现了k次，那么这个子串的子串至少也出现了k次
            # 所以这里只需要枚举所有长度为 minSize 的字符串即可，这个次数一定大于等于s[i:i+maxSize]
            cur = s[i:i+minSize]
            chars = set(cur)
            if len(chars) <= maxLetters:
                freq[cur] += 1
                ans = max(ans, freq[cur])

        return ans


# 方法一：枚举
# 时间复杂度：O(NS^2)，其中 N 是字符串的长度，S 是 minSize 和 maxSize 的数量级，在本题中为 26
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        freq = Counter()
        ans = 0
        
        # 枚举每个子串的开始位置
        for i in range(n):
            # 枚举所有长度在 minSize 与 maxSize 之间的字符串，
            # 选出其中字母数量小于等于的 maxLetters 的字符串并进行频数统计
            chars = set()
            cur = ""
            for j in range(i, min(n, i + maxSize)):
                chars.add(s[j])
                if len(chars) > maxLetters:
                    break
                cur += s[j]
                if j - i + 1 >= minSize:
                    freq[cur] += 1
                    ans = max(ans, freq[cur])
        return ans
