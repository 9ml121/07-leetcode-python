"""
给定一个单词列表 words 和一个整数 k ，返回前 k 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。

 

示例 1：

输入: words = ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。
示例 2：

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。
 

注意：

1 <= words.length <= 500
1 <= words[i] <= 10
words[i] 由小写英文字母组成。
k 的取值范围是 [1, 不同 words[i] 的数量]
 

进阶：尝试以 O(n log k) 时间复杂度和 O(n) 空间复杂度解决。
"""


import collections
from typing import List
import heapq

# 方法1：字典 + 排序


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 字典cnts统计words中各单词出现次数
        cnts = collections.Counter(words)
        # 字典排序:按单词出现频率由高到低排序。如果不同的单词有相同出现频率， 按字典顺序 排序。
        keys = sorted(cnts.keys(), key=lambda word: (-cnts[word], k))
        # print(keys[:k])
        return keys[:k]

# 方法2：字典 + 堆排序
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        max_heap = []
        for word, count in word_count.items():
            heapq.heappush(max_heap, (-count, word))

        result = [heapq.heappop(max_heap)[1] for _ in range(k)]
        return result
    

# 堆写法2：用类封装词和词频，重写运算符
class Word:
    def __init__(self, word, fre):
        self.word = word
        self.fre = fre

    def __lt__(self, other):
        if self.fre != other.fre:
            return self.fre < other.fre
        return self.word > other.word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = collections.Counter(words)
        heap = []

        for word, fre in cnt.items():
            heapq.heappush(heap, Word(word, fre))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(reverse=True)
        return [x.word for x in heap]



