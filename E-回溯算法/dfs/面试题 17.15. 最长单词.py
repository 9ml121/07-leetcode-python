"""
给定一组单词words，编写一个程序，找出其中的最长单词，且该单词由这组单词中的其他单词组合而成。若有多个长度相同的结果，返回其中字典序最小的一项，若没有符合要求的单词则返回空字符串。

示例：

输入： ["cat","banana","dog","nana","walk","walker","dogwalker"]
输出： "dogwalker"
解释： "dogwalker"可由"dog"和"walker"组成。
提示：

0 <= len(words) <= 200
1 <= len(words[i]) <= 100
"""

from collections import defaultdict
from typing import List

# todo 方法1：dfs回溯 + 集合(推荐!)
# 参考：C-回溯算法\dfs\79. 单词搜索.py

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 找出 words数组的最长单词，且该单词由这组单词中的其他单词组合而成。
        def dfs(word: str, words_set: set):
            if not word:
                return True

            for i in range(len(word)):
                s = word[:i+1]
                if s in words_set:
                    if dfs(word[i+1:], words_set):
                        return True

            return False

        # words按照元素长度降序，字典序升序
        words.sort(key=lambda x: (-len(x), x))
        # 从前往后遍历words, 一旦查找到当前word满足条件，立刻返回
        for i, w in enumerate(words):
            if dfs(w, set(words[i+1:])):
                return w

        return ''

# 方法2：动态规划(待研究？)
"""
dp[i]为前i个字符最多能划分成几个更短单词
转移方程为
dp[i] = max(dp[j]) + 1 if word[j:i] in vis, j < i

为方便边界处理，dp比单词长一位，并且dp[0]=0
处理完单词后，如果dp[-1]>1，则说明可以划分成多个单词
"""
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x: (len(x), x))
        vis = set()
        ans = ""
        # dp[i] = max(dp[j]) + 1 if word[j:i] in vis, j < i

        for word in words:
            dp = [0] + [-1] * len(word)
            for i in range(1, len(word)+1):
                for j in range(i):
                    if dp[j] != -1 and word[j:i] in vis:
                        dp[i] = max(dp[i], dp[j] + 1)

            if dp[-1] > 1 and len(word) > len(ans):
                ans = word
            vis.add(word)
        return ans  

# 方法3：字典树(待研究？)
class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.isEnd = False

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children[ch]
        node.isEnd = True

    def check(self, word):
        if word == "":
            return True
        node = self
        for i, ch in enumerate(word):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.isEnd and self.check(word[i+1:]):
                return True
        return False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        words.sort(key=lambda x: (len(x), x))
        ans = ""
        for word in words:
            if not word:
                continue
            if trie.check(word):
                if len(word) > len(ans):
                    ans = word
            else:
                trie.insert(word)
        return ans


