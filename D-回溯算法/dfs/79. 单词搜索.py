"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

示例：
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

提示：
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成

进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
"""
from typing import List

# todo 回溯算法
"""
解题思路：
这是一个经典的回溯算法的应用题。可以使用深度优先搜索（DFS）来解决这个问题。
1.首先，遍历整个二维网格，找到与单词的首字母匹配的网格单元格。
2.对于每个匹配的单元格，从该单元格开始进行深度优先搜索。
    在搜索过程中，检查当前单元格是否与单词的下一个字母匹配，如果匹配，则继续搜索该单元格的上、下、左、右四个相邻单元格。
3.在进行深度优先搜索时，需要标记已访问过的单元格，以避免重复使用同一个单元格。
4.如果在深度优先搜索过程中，找到单词的最后一个字母，则说明单词存在于网格中，返回 true。否则，返回 false。
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # 给定一个 m x n 二维字符网格 board 和一个字符串单词 word, 返回word是否在网格中
        # 单词必须按照字母顺序，通过相邻的单元格内的字母构成
        m, n = len(board), len(board[0])
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        vis = [[False] * n for _ in range(m)]

        def dfs(x, y, i=0):
            # (x,y)代表查找网格的开始坐标，i表示当前匹配的word索引，默认都是从word[0]开始
            
            if i == len(word) - 1:
                # 字符串的最后一个字符匹配，即返回 true
                return board[x][y] == word[i]

            if board[x][y] == word[i]:
                # 只要当前考虑的字符能够匹配，就从四面八方继续搜索
                vis[x][y] = True
                for ox, oy in offsets:
                    nx, ny = x + ox, y + oy
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                        # 不越界，且之前没有被访问
                        if dfs(nx, ny, i + 1):
                            return True
                       
                vis[x][y] = False  # 回溯
            return False

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
                
        return False


if __name__ == '__main__':
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    # word = "ABCCED"
    print(Solution().exist(board, word))
