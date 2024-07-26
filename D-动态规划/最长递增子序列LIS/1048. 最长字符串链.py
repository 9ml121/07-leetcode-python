"""
给出一个单词数组 words ，其中每个单词都由小写英文字母组成。

如果我们可以 不改变其他字符的顺序 ，在 wordA 的任何地方添加 恰好一个 字母使其变成 wordB ，那么我们认为 wordA 是 wordB 的 前身 。

例如，"abc" 是 "abac" 的 前身 ，而 "cba" 不是 "bcad" 的 前身
词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word1 是 word2 的前身，word2 是 word3 的前身，依此类推。一个单词通常是 k == 1 的 单词链 。

从给定单词列表 words 中选择单词组成词链，返回 词链的 最长可能长度 。


示例 1：

输入：words = ["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 ["a","ba","bda","bdca"]
示例 2:

输入：words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
输出：5
解释：所有的单词都可以放入单词链 ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].
示例 3:

输入：words = ["abcd","dbqca"]
输出：1
解释：字链["abcd"]是最长的字链之一。
["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变了。


提示：

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] 仅由小写英文字母组成。
"""
from typing import List

"""
排序 + 动态规划 + 字典
时间复杂度：O(n×m×(logn+m))，其中 n 表示字符串数组的长度，m 表示每个字符串的平均长度。
首选对字符串数组进行排序，需要的时间为 O(n×m×logn)，
然后遍历每个字符串，并对每个字符串都生成其「前身」字符串，需要的时间为 O(n×m^2)，因此总的时间复杂度为 O(n×m×(logn+m))。
"""
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # 按照长度降序排列
        words.sort(key=len)

        # dp[word]代表words中每个word能够构成的最长字符串链个数
        dp = {}
        maxLen = 0

        for word in words:
            dp[word] = 1
            for i in range(len(word)):
                #  枚举去掉 word[i]
                tmp = word[:i] + word[i + 1:]
                if tmp in dp:
                    dp[word] = max(dp[word], dp[tmp] + 1)

            maxLen = max(maxLen, dp[word])

        return maxLen
