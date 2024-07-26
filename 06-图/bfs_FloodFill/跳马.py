"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134887408?spm=1001.2014.3001.5502

题目描述
马是象棋（包括中国象棋和国际象棋）中的棋子，走法是每步直一格再斜一格，即先横着或者直者走一格，然后再斜着走一个对角线，可进可退，可越过河界，俗称"马走日"字。

给定 m 行 n 列的棋盘（网格图），棋盘上只有棋子象棋中的棋子“马”，并且每个棋子有等级之分，等级为 k 的马可以跳 1~k 步（走的方式与象棋中“马”的规则一样，不可以超出棋盘位置），问是否能将所有马跳到同一位置，如果存在，输出最少需要的总步数（每匹马的步数相加），不存在则输出-1。

注：允许不同的马在跳的过程中跳到同一位置，坐标为（x,y）的马跳一次可以跳到的坐标为：(x+1, y+2)，(x+1, y-2)，(x+2, y+1)，(x+2, y-1)，(x-1, y+2)，(x-1, y-2)，(x-2, y+1)，(x-2, y-1)，的格点上，但是不可以超出棋盘范围。

输入描述
第一行输入m，n，代表 m 行 n 列的网格图棋盘（1 ≤ m, n ≤ 25）

接下来输入 m 行 n 列的网格图棋盘，如果第 i 行，第 j 列的元素为 "." ，代表此格点没有棋子，如果为数字 k（1 ≤ k ≤ 9），代表此格点存在等级为 k 的“马”

输出描述
输出最少需要的总步数（每匹马的步数相加），不存在则输出-1。

用例1
输入
3 2
..
2.
..
输出
0
说明
只有一匹马，不需要跳动

用例2
输入
3 5
47.48
4744.
7....
输出
17
"""
# todo 考察bfs过程中记录路径

import collections

# 输入
# m 行 n 列的网格图棋盘
rows, cols = map(int, input().split())
# 单元格内容k代表马能跳的最多步骤，‘.’代表空格
grid = [input() for _ in range(rows)]

# 马跳日可以跳的8个方向
offsets = [(1, 2), (1, -2), (2, 1), (2, -1),
           (-1, 2), (-1, -2), (-2, 1), (-2, -1)]


# 输出：是否能将所有马跳到同一位置，如果存在，输出最少需要的总步数（每匹马的步数相加），不存在则输出-1。
# bfs遍历方法1：bfs遍历每个马飞日可以跳到的位置，并更新每个位置所有的最少步骤
# todo 1.记录马走日跳到grid每个位置所用的最少步骤(二位数组转换为一维数组)
steps = [0] * (rows * cols)
# # todo 2.记录马走日可以跳到的所有位置集合，然后通过bfs遍历结果和can_reached_set取交集,来判断所有马可以调到的位置
can_reached_set = set(range(rows*cols))


def bfs(i, j, k, can_reach: set) -> None:
    # bfs查找马走日在k步之内可以跳到的所有位置和所需的最小步骤
    dq = [(i, j, 0)]  # (横坐标，纵坐标，所用步骤)
    while dq and k > 0:
        nxt_dq = []
        for x, y, used_step in dq:
            for ox, oy in offsets:
                nx, ny = x + ox, y + oy
                # 越界
                if not (0 <= nx < rows and 0 <= ny < cols):
                    continue

                # 已经跳过的位置，就不重复跳
                new_idx = nx * cols + ny
                if new_idx in can_reach:
                    continue

                # 记录可以跳到的位置
                can_reach.add(new_idx)
                # 可以跳到的位置所用的最小步骤（累加步骤）
                steps[new_idx] += (used_step + 1)
                # 加入队列，查找下一个可以调到的位置
                nxt_dq.append((nx, ny, used_step + 1))
        k -= 1
        dq = nxt_dq


def main():
    global can_reached_set
    for i in range(rows):
        for j in range(cols):
            val = grid[i][j]
            if val == '.':
                continue

            # 等级为 k 的马可以跳 1~k 步
            k = int(val)
            # todo 二维数组转换为一维数组坐标
            idx = i * cols + j
            can_reach = set([idx])
            # 1.bfs查找马走日可以跳到的所有位置和所需的最小步骤
            bfs(i, j, k, can_reach)

            # todo 2.取2个集合的交集
            can_reached_set = can_reached_set.intersection(can_reach)
            # 2.1 如果交集为0，说明不能将所有马走日调到同一个位置
            if not can_reached_set:
                return -1

    # 2.2 如果交集不为0，查找跳到相同位置所用最少的步骤
    min_step = min([steps[idx] for idx in can_reached_set])
    return min_step


print(main())

"""
3 4
5..5
...7
..8.
"""


# bfs遍历方法2：判断grid每一个单元格是否所有马都能调到(时间复杂度较高)
def bfs2(horses: list, i, j, steps: list):
    for x, y, k in horses:
        q = [(x, y, 0)]
        found = False
        vis = {(x, y)}
        while q and q[0][2] <= k:
            x0, y0, step = q.pop(0)
            if x0 == i and y0 == j:
                found = True
                steps[0] += step
                break

            # 遍历8个方向
            for ox, oy in offsets:
                nx = x0 + ox
                ny = y0 + oy

                # 越界
                if not (0 <= nx < rows and 0 <= ny < cols):
                    continue

                # 已经跳过
                if (nx, ny) in vis:
                    continue

                q.append((nx, ny, step+1))
                vis.add((nx, ny))

        if not found:
            return False

    return True


def main():
    # 1. 先用列表存储所有马所在坐标和可跳步骤k
    horses = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '.':
                horses.append((i, j, int(grid[i][j])))
    # print(horses)

    # 2. 遍历grid每一个坐标，在bfs遍历每一个马,判断该坐标是否所有马都能跳到，并累加跳到该位置的最少步骤
    ans = float('inf')
    for i in range(rows):
        for j in range(cols):
            steps = [0]  # todo 注意：这里step定义为数组，只是为了方便外部函数可以直接修改steps结果
            if bfs2(horses, i, j, steps):
                # print(i,j,steps)
                ans = min(ans, steps[0])

    return ans if ans != float('inf') else -1


print(main())
