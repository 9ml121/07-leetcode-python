"""
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 遵循如下规则：
1.数字 1-9 在每一行只能出现一次。
2.数字 1-9 在每一列只能出现一次。
3.数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）

数独部分空格内已填入了数字，空白格用 '.' 表示。

示例 1：
输入：board =[["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],
      ["6","7","2","1","9","5","3","4","8"],
      ["1","9","8","3","4","2","5","6","7"],
      ["8","5","9","7","6","1","4","2","3"],
      ["4","2","6","8","5","3","7","9","1"],
      ["7","1","3","9","2","4","8","5","6"],
      ["9","6","1","5","3","7","2","8","4"],
      ["2","8","7","4","1","9","6","3","5"],
      ["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：

提示：
board.length == 9
board[i].length == 9
board[i][j] 是一位数字或者 '.'
题目数据 保证 输入数独仅有一个解
"""
from typing import List

'''
解数独思路：
类似人的思考方式去尝试，行，列，还有 3*3 的方格内数字是 1~9 不能重复。
我们尝试填充，如果发现重复了，那么擦除重新进行新一轮的尝试，直到把整个数组填充完成。

算法步骤:
1。数独首先行，列，还有 3*3 的方格内数字是 1~9 不能重复。
2。声明布尔数组，表明行列中某个数字是否被使用了， 被用过视为 true，没用过为 false。
3。初始化布尔数组，表明哪些数字已经被使用过了。
4。尝试去填充数组，只要行，列， 还有 3*3 的方格内 出现已经被使用过的数字，我们就不填充，否则尝试填充。
5。如果填充失败，那么我们需要回溯。将原来尝试填充的地方改回来。
6。递归直到数独被填充完成。
'''


# 回溯算法思路：用到了 3 个布尔数组做标记和回溯
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 1.todo  1.三个布尔数组arr[i][j]表示行, 列, 还有 3*3 的方格的数字是否被使用过
        # rowUsed[i][j]表示下标为i行，数字j是否用过
        rowUsed = [[False] * 10 for _ in range(9)]
        # colUsed[i][j]表示下标为i列，数字j是否用过
        colUsed = [[False] * 10 for _ in range(9)]
        # boxUsed[i][j][k]表示单元格(x, y)所在的小方格i=x//3, j==y//3， 数字k是否用过
        boxUsed = [[[False] * 10 for _ in range(3)] for _ in range(3)]

        # 步骤 1：同 N 皇后问题，先遍历棋盘一次，然后每一行，每一列在 row col cell 里占住位置
        for row in range(9):
            for col in range(9):
                num = ord(board[row][col]) - ord('0')  # todo 2.计算2个整数字符串差值小技巧
                if 1 <= num <= 9:
                    rowUsed[row][num] = True
                    colUsed[col][num] = True
                    boxUsed[row // 3][col // 3][num] = True

        # 由于存在唯一解，搜索到一个解就可以退出了，递归函数的返回值为是否搜索到一个解
        def dfs(row, col) -> bool:
            # 递归终止条件 1：全部填完
            if row == 9:
                return True

            # 对 '.' 尝试从 1 填到 9
            if board[row][col] == '.':
                for num in range(1, 10):
                    # 如果行、列、box 任意一个已经填了 num, 则尝试下一个数字
                    if rowUsed[row][num] or colUsed[col][num] or boxUsed[row // 3][col // 3][num]:
                        continue
                    # 填写当前字符，并且对应 row、col、box 占位
                    board[row][col] = str(num)
                    rowUsed[row][num] = True
                    colUsed[col][num] = True
                    boxUsed[row // 3][col // 3][num] = True

                    # 题目保证只有唯一解，继续填写下一格
                    # ①row + (col + 1) // 9: 表示如果 col 已经在一列的末尾（此时 col = 8），跳转到下一行
                    # ②(col + 1) % 9: 表示当 col = 8 时，col + 1 重置到 0
                    if dfs(row + (col + 1) // 9, (col + 1) % 9):  # todo 3.跳转下一列和下一行的小技巧
                        return True

                    # 重置变量
                    rowUsed[row][num] = False
                    colUsed[col][num] = False
                    boxUsed[row // 3][col // 3][num] = False
                    board[row][col] = '.'
            else:
                # 填写下一格和 ① 一样
                return dfs(row + (col + 1) // 9, (col + 1) % 9)
            # 递归终止条件 2：全部尝试过以后，返回 false
            return False

        # 步骤 2：进行一次深度优先遍历，尝试所有的可能性
        dfs(0, 0)


if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    cls = Solution()
    cls.solveSudoku(board)
    print(board)
