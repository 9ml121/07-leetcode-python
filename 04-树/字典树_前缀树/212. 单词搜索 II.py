"""
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。


示例 1：
输入：board = [["o","a","a","n"],
              ["e","t","a","e"],
              ["i","h","k","r"],
              ["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
输出：["eat","oath"]

示例 2：
输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]


提示：

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] 是一个小写英文字母
1 <= words.length <= 3 * 10^4
1 <= words[i].length <= 10
words[i] 由小写英文字母组成
words 中的所有字符串互不相同
"""
import collections
from typing import List


# 字典树 + 回溯
class Trie:
    def __init__(self) -> None:
        self.children = collections.defaultdict(Trie)  # 默认字典，key是26个字母，val是Trie对象
        self.word = ""  # 不为空代表是一个完整的单词

    def addWord(self, word: str) -> None:
        node = self
        for c in word:
            node = node.children[c]
        node.word = word

    def __repr__(self) -> str:
        return f"Trie(children={list(self.children.keys())}, word={self.word})"


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 先根据words构建字典树
        root = Trie()
        for word in words:
            root.addWord(word)

        # 回溯算法查找在board存在的完整单词
        rows, cols = len(board), len(board[0])
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def inArea(i, j):
            return 0 <= i < rows and 0 <= j < cols

        res = []
        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j, node: Trie):
            # 判断当前单元格是否在 Trie 中
            c = board[i][j]
            if c not in node.children:
                return

            # 更新当前节点
            node = node.children[c]
            # 判断当前节点是否形成单词
            if node.word:
                # print(node.word)
                res.append(node.word)
                node.word = ""  # 避免重复添加单词
                # return  # 注意：这里不能马上返回，因为后面可能还有完整单词

            # 标记当前单元格已访问
            visited[i][j] = True

            # 回溯访问当前单元格的上、下、左、右四个方向的相邻单元格
            for ox, oy in offsets:
                newX, newY = i + ox, j + oy
                if inArea(newX, newY) and not visited[newX][newY]:
                    dfs(newX, newY, node)

            # 恢复当前单元格的状态
            visited[i][j] = False

        # 遍历board中每个单元格
        for i in range(rows):
            for j in range(cols):
                # if board[i][j] in root.children:
                dfs(i, j, root)

        return res


if __name__ == '__main__':
    board = [["o", "a", "a", "n"],
             ["e", "t", "a", "e"],
             ["i", "h", "k", "r"],
             ["i", "f", "l", "v"]]
    words = ["oath", "pea", "eat", "rain"]  # ["eat","oath"]
    print(Solution().findWords(board, words))
