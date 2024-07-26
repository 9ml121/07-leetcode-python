"""
题目描述
2XXX年，人类通过对火星的大气进行宜居改造分析，使得火星已在理论上具备人类宜居的条件；
由于技术原因，无法一次性将火星大气全部改造，只能通过局部处理形式；

假设将火星待改造的区域为row * column的网格，每个网格有3个值，宜居区、可改造区、死亡区，使用YES、NO、NA代替，
    YES表示该网格已经完成大气改造，
    NO表示该网格未进行改造，后期可进行改造，
    NA表示死亡区，不作为判断是否改造完的宜居，无法穿过；

初始化下，该区域可能存在多个宜居区，并目每个宜居区能同时在每个大阳日单位向上下左右四个方向的相邻格子进行扩散，自动将4个方向相邻的真空区改造成宜居区；
请计算这个待改造区域的网格中，可改造区是否能全部成宜居区，如果可以，则返回改造的大阳日天教，不可以则返回-1

输入描述
输入row * column个网格数据，每个网格值枚举值如下: YES，NO，NA；

样例:
YES YES NO
NO NO NO
NA NO YES

输出描述
可改造区是否能全部变成宜居区，如果可以，则返回改造的太阳日天数，不可以则返回-1。

备注
grid[i][j]只有3种情况，YES、NO、NA

row == grid.n
column == grid[i].n
1 ≤ row, column ≤ 8

用例
输入
YES YES NO
NO NO NO
YES NO NO
输出	2
说明	经过2个太阳日，完成宜居改造

输入
YES NO NO NO
NO NO NO NO
NO NO NO NO
NO NO NO NO
输出	6
说明	经过6个太阳日，可完成改造

输入
NO NA
输出	-1
说明	无改造初始条件，无法进行改造

输入
YES NO NO YES
NO NO YES NO
NO YES NA NA
YES NO NA NO
输出	-1
说明	-1 // 右下角的区域，被周边三个死亡区挡住，无法实现改造
"""


# todo 腐烂的橘子变种题: 图的多源BFS模板:队列完成
import collections


def getResult(grid: list):
    rows, cols = len(grid), len(grid[0])  
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    step = 0  # 返回改造的大阳日天教，不可以则返回-1
    dq = collections.deque()  # 保存值为yes的坐标 + 统计天数cnt
    check = 0  # 保存no的坐标数量,用来判断最后是否都扩散到

    # 并目每个宜居区能同时在每个大阳日单位向上下左右四个方向的相邻格子进行扩散，自动将4个方向相邻的真空区改造成宜居区
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'YES':
                dq.append((i, j, step))
            elif grid[i][j] == 'NO':
                check += 1

    # bfs
    while dq:
        x, y, step = dq.popleft()
        for ox, oy in offsets:
            nx = x + ox
            ny = y + oy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'NO':
                grid[nx][ny] = 'YES'
                check -= 1
                dq.append((nx, ny, step + 1))
                
    # 计算这个待改造区域的网格中，可改造区是否能全部成宜居区，如果可以，则返回改造的大阳日天教，不可以则返回-1
    return -1 if check > 0 else step


if __name__ == '__main__':
    # 获取输入：按照输入为空作为结束标识
    grid = []
    while True:
        s = input()
        if s == '':
            break
        grid.append(s.split())

    # 调用函数
    # grid = [['YES', 'YES', 'NO'], ['NO', 'NO', 'NO'], ['YES', 'NO', 'NO']]
    # grid = [['YES', 'NO', 'NO', 'NO'], ['NO', 'NO', 'NO', 'NO'], ['NO', 'NO', 'NO', 'NO'], ['NO', 'NO', 'NO', 'NO']]
    print(getResult(grid))
