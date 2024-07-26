"""
给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。

字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。

例如， “ace” 是 “abcde” 的子序列。
 

示例 1:

输入: s = "abcde", words = ["a","bb","acd","ace"]
输出: 3
解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
Example 2:

输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
输出: 2
 

提示:

1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
words[i]和 s 都只由小写字母组成。
"""




from bisect import bisect_right
from collections import defaultdict, deque
from typing import List

# 暴力搜索：分别查找words中每个单词是不是s子序列，时间复杂度len(words) * len(s), 肯定超时

# todo 方法1：多指针，分桶(推荐！)
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # 返回  words[i] 中是s的子序列的单词个数
        # “ace” 是 “abcde” 的子序列
        ans = 0

        # 字典key是26个字母，val是以该字母开头的单词队列（分桶）
        chars_dict = defaultdict(deque)
        for word in words:
            chars_dict[word[0]].append(word)

        # print(chars_dict)
        # 依次遍历s中每个字符，查找dict中以该字符开头的单词列表，进行bfs搜索
        for c in s:
            # dq代表字典里面以s当前字符c开头的单词队列
            dq = chars_dict[c]
            for _ in range(len(dq)):  # 注意：这里不能用while dq, 因为字典在实时更新
                word = dq.popleft()
                if len(word) == 1:
                    # 该单词已经完全匹配
                    ans += 1
                else:
                    # 去掉word首字母，将剩余单词再次放入字典对应队列
                    key = word[1]
                    word2 = word[1:]
                    chars_dict[key].append(word2)
        return ans

# 方法1：空间优化：实际上，每个桶可以只存储单词的下标 i 以及该单词当前匹配到的位置 j，这样可以节省空间。

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(deque)
        for i, w in enumerate(words):
            d[w[0]].append((i, 0))
            
        ans = 0
        for c in s:
            for _ in range(len(d[c])):
                i, j = d[c].popleft()
                j += 1
                if j == len(words[i]):
                    ans += 1
                else:
                    d[words[i][j]].append((i, j))
        return ans




# 方法2：二分查找（待研究？）

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        pos = defaultdict(list)
        for i, c in enumerate(s):
            pos[c].append(i)

        ans = len(words)
        for w in words:
            if len(w) > len(s):
                ans -= 1
                continue

            p = -1
            for c in w:
                ps = pos[c]
                j = bisect_right(ps, p)
                if j == len(ps):
                    ans -= 1
                    break
                p = ps[j]
        return ans
