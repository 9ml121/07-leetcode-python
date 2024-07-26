"""
在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示。
一次 移动 定义为选择 0 与一个相邻的数字（上下左右）进行交换.
最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

给出一个谜板的初始状态 board ，返回最少可以通过多少次移动解开谜板，
如果不能解开谜板，则返回 -1 。

示例 1：
输入：board = [[1,2,3],
              [4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成

示例 2:
输入：board = [[1,2,3],
              [5,4,0]]
输出：-1
解释：没有办法完成谜板

示例 3:
输入：board = [[4,1,2],
              [5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]


提示：
board.length == 2
board[i].length == 3
0 <= board[i][j] <= 5
board[i][j] 中每个值都 不同
"""
import collections
from typing import List

"""
问题描述：
给定一个 2x3 的二维列表 board 表示一个 2x3 的游戏棋盘，其中填有 1 到 5 的数字和一个空格 0。
只有相邻的数字和空格可以进行交换。
目标是将棋盘上的数字重新排列成目标状态 [[1,2,3],[4,5,0]]。

要解决 "773. 滑动谜题"，可以使用广度优先搜索（BFS）算法。下面是一种解题思路和对应的 Python 代码：
1.将初始状态 board 转化为一个字符串 start，将目标状态 [[1,2,3],[4,5,0]] 转化为字符串 target，作为搜索的目标。
2.定义一个队列（可以使用 Python 中的 deque）来存储搜索过程中的状态。
3.定义一个集合（可以使用 Python 中的 set）来存储已经搜索过的状态，以避免重复搜索。
4.将初始状态字符串 start 加入队列和集合中。
5.通过循环遍历队列中的状态，直到队列为空：
    1)从队列中取出一个状态字符串 current。
    2)如果 current 等于目标状态字符串 target，则返回此时的搜索步数。
    3)根据题目给出的操作规则，生成可能的下一个状态字符串。
    4)如果下一个状态字符串不在集合中，将其加入队列和集合中。
6.如果循环结束后仍然没有找到目标状态，则返回 -1，表示无法达到目标状态。
"""


# BFS思路：难点是要将二位列表转换为字符串，方便判断每次遍历结果是否和目标相等
# 同类型题：909. 蛇梯棋.py
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 1. 将2*3的二维数组转换为6位字符串
        # start = ''
        # for i in range(2):
        #     for j in range(3):
        #         num = board[i][j]
        #         start += str(num)
        start = ''.join(str(num) for row in board for num in row)  # 生成器表达式
        # print(start)  # '412503'
        target = '123450'

        # 2. todo 将2*3的二维数组6个单元格可以遍历的方向坐标转换为字符串索引
        # 412
        # 503
        directions = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (3, 5, 1), (4, 2)]
        visitedSet = {start}  # set集合用来记录遍历过的字符串

        # 3. bfs遍历字符串的转换
        dq = collections.deque([(start, 0)])  # (起始状态，移动次数)
        while dq:
            cur_state_str, steps = dq.popleft()
            if cur_state_str == target:
                return steps

            zeroIdx = cur_state_str.index('0')
            neighbours = directions[zeroIdx]
            for neighbourIdx in neighbours:
                new_state = list(cur_state_str)
                new_state[neighbourIdx], new_state[zeroIdx] = new_state[zeroIdx], new_state[neighbourIdx]
                new_state_str = ''.join(new_state)

                if new_state_str not in visitedSet:
                    visitedSet.add(new_state_str)
                    dq.append((new_state_str, steps + 1))
        return -1


if __name__ == '__main__':
    board = [[4, 1, 2],
             [5, 0, 3]]
    print(Solution().slidingPuzzle(board))
