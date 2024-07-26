"""
给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。

 

示例 1：

输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
输出：16 
解释：这两个单词为 "abcw", "xtfn"。
示例 2：

输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
输出：4 
解释：这两个单词为 "ab", "cd"。
示例 3：

输入：words = ["a","aa","aaa","aaaa"]
输出：0 
解释：不存在这样的两个单词。
 

提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母
"""
from typing import List
import collections
# todo 位掩码, 状态压缩，集合交集运算， 位运算(&, |, <<), 字典

# todo 写法1：用集合的交集运算 &
# 用集合存储每个单词中出现的字母，然后两个集合取交集
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 返回 len(words[i]) * len(words[j]) 的最大值，并且这两个单词不含有公共字母
        # 如果不存在这样的两个单词，返回 0
        ans = 0

        n = len(words)
        for i, word1 in enumerate(words):
            word1_set = set(word1)
            for j, word2 in enumerate(words[i+1:]):
                word2_set = set(word2)
                if not word1_set & word2_set:  # intersection
                    ans = max(ans, len(word1) * len(word2))

        return ans


# todo 写法2：将字符串状压成26位二进制数，以便快速判断是否有重复字符
# 时间复杂度O(N^2) + O(N*M), N为单词数量，M为单词平均长度
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 返回 len(words[i]) * len(words[j]) 的最大值，并且这两个单词不含有公共字母
        # 如果不存在这样的两个单词，返回 0
        
        # todo 将每个字符串用一个二进制数 masks[i] 表示，这个二进制数的每一位表示字符串中是否含有某个字母。
        masks = [0] * len(words)
        # todo 每个单词计算位掩码: 状态压缩,将每个字符串用26位二进制表示
        for s in words:
            for c in s:
                masks[i] |= 1 << (ord(c) - ord("a"))
            
        ans = 0
        for i, s in enumerate(words):
            for j, t in enumerate(words[i+1:]):
                # todo 如果两个字符串没有公共字母，那么这两个字符串对应的二进制数的按位 与 的结果为 0，
                if (masks[i] & masks[j]) == 0:
                    ans = max(ans, len(s) * len(t))
        return ans

# 写法3：位运算优化：对于词频相同（mask值相等）的两字符，只需要保留字符长度大的即可，因此我们可以使用「字典」代替 masks 数组。
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # 返回 len(words[i]) * len(words[j]) 的最大值，并且这两个单词不含有公共字母
        # 如果不存在这样的两个单词，返回 0

        # todo key是单词对应的位掩码，val是单词长度
        mask_dict = collections.Counter()
        ans = 0
        for i, s in enumerate(words):
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord("a"))

            # 位掩码相同，保留字符长度大
            if mask not in mask_dict or mask_dict[mask] < len(s):
                mask_dict[mask] = len(s)
            
        ans = 0
        masks = list(mask_dict.keys())
        for i, mask1 in enumerate(masks):
            for j, mask2 in enumerate(masks[i+1:]):
                # todo 如果两个字符串没有公共字母，那么这两个字符串对应的二进制数的按位 与 的结果为 0，
                if (mask1 & mask2) == 0:
                    ans = max(ans, mask_dict[mask1] * mask_dict[mask2])
        return ans
   
