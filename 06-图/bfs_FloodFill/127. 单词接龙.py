"""
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：
1.每一对相邻的单词只差一个字母。
2.对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
3.sk == endWord

给你两个单词 beginWord 和 endWord 和一个字典 wordList ，
返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。
如果不存在这样的转换序列，返回 0 。


示例 1：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

示例 2：
输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。


提示：
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有字符串 互不相同
"""
import collections
from typing import List



# todo 单源最短路径Dijkstra算法，bfs解法
# leetcode 752.打开转盘锁.py类似
# leetcode 433. 最小基因变化

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，
        # 返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目
        
        # used记录单词是否使用
        used = [False] * len(wordList)
        # 特判
        if endWord not in wordList:
            return 0

        def check_one_diff(word1: str, word2: str):
            # 判断2个长度相同的单词是否只差一个字母
            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1

        # todo dq记录bfs搜索路径单词 + 转换次数
        dq = collections.deque([(beginWord, 1)])
        while dq:
            word, cnt = dq.popleft()
            if word == endWord:
                # 一旦找到目标，马上返回结果
                return cnt

            for i, next_word in enumerate(wordList):
                # todo 通过函数check_one_diff判断两个单词是否相差1个字母
                if not used[i] and check_one_diff(word, next_word):
                    used[i] = True
                    dq.append((next_word, cnt + 1))

        return 0
    
# 写法2: 从 beginWord 开始，通过改变一个字母生成所有可能的后继单词，然后将其添加到搜索队列中
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # word_set 方便bfs查找构造的新单词是否在wordList
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        # dq用来记录bfs遍历路径中单词 + 转换次数
        dq = collections.deque([(beginWord, 1)])
        # used集合用来记录已经遍历过的单词，避免走重复路径
        used = set(beginWord)

        while dq:
            word, step = dq.popleft()

            if word == endWord:
                return step

            for i in range(len(word)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    # todo 构造word转换一次所有可能的新单词
                    new_word = word[:i] + char + word[i + 1:]
                    # 如果new_word在单词集合，并且没有使用过，就添加到dq
                    if new_word in word_set and new_word not in used:
                        dq.append((new_word, step + 1))
                        used.add(new_word)

        return 0





if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(Solution().ladderLength(beginWord, endWord, wordList))  # 5
