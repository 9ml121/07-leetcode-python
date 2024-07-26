"""
按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，
该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例 1：
输入：n = 4
输出：[[".Q..",
       "...Q",
       "Q...",
       "..Q."],
       ["..Q.",
       "Q...",
       "...Q",
       ".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

示例 2：
输入：n = 1
输出：[["Q"]]


提示：
1 <= n <= 9
"""
from typing import List


# 回溯算法：注意要控制的回溯变量有3个
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []  # 最后返回结果
        colSet = set()  # 已经放置的皇后(row,col)，列坐标col集合
        mainSet = set()  # 已经放置的皇后(row,col)，右对角线位置横row - col 集合
        subSet = set()  # 已经放置的皇后(row,col)，左对角线位置横row + col 集合

        # 将每一行皇后占据的坐标数组 qPosList转换成字符串矩阵 board
        def convert(qPosList: list) -> list:
            board = [''] * n
            for i in range(n):
                rows = ['.'] * n
                rows[qPosList[i]] = 'Q'
                board[i] = ''.join(rows)
            return board

        def dfs(row: int, qPosList: list) -> None:
            # 如果能走到最后一行之后，证明是一个可行解，加入结果集res
            if row == n:
                board = convert(qPosList)
                res.append(board)
                return

            # 尝试每一行放皇后的位置
            for col in range(n):  # 遍历列
                if col not in colSet \
                        and (row - col) not in mainSet \
                        and (row + col) not in subSet:
                    colSet.add(col)
                    mainSet.add(row - col)
                    subSet.add(row + col)
                    qPosList.append(col)
                    dfs(row + 1, qPosList)  # dfs遍历下一行

                    qPosList.pop()
                    colSet.remove(col)
                    mainSet.remove(row - col)
                    subSet.remove(row + col)

        dfs(0, [])
        return res


if __name__ == '__main__':
    n = 4
    print(Solution().solveNQueens(n))
