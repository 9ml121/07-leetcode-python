"""
题目描述
有一个64×64的矩阵，每个元素的默认值为0，现在向里面填充数字，相同的数字组成一个实心图形，如下图所示是矩阵的局部（空白表示填充0）：
数字1组成了蓝色边框的实心图形，数字2组成了红色边框的实心图形。

单元格的边长规定为1个单位。

请根据输入，计算每个非0值填充出来的实心图形的周长。

输入描述
第一行输入N，表示N个图形，n > 0 且 n < 64 × 64
矩阵左上角单元格坐标记作(0, 0)，第一个数字表示行号，第二个数字表示列号
接下来是N行，每行第一个数是矩阵单元格填充的数字，后续每两个一组，表示填充该数字的单元格坐标

答题者无需考虑数据格式非法的场景，题目用例不考察数据格式
题目用例保证同一个填充值只会有一行输入数据

输出描述
一共输出N个数值，每个数值表示某一行输入表示图形的周长
输出顺序需和输入的隔行顺序保持一致，即第1个数是输入的第1个图形的周长，第2个数是输入的第2个图形的周长，以此类推。
用例
输入	2
    1 1 3 2 2 2 3 2 4 3 2 3 3 3 4 4 1 4 2 4 3 4 4 5 2 5 3
    2 3 7 3 8 4 5 4 6 4 7 4 8 5 4 5 5 5 6 5 7 5 8 6 4 6 5 6 6 6 7 6 8 7 4 7 5 7 6 7 7 7 8
输出	18 20
说明	无
"""


def getResult(grid: list, num: int):
    # 64*64矩阵
    # 查找grid中由num数值表示图形的周长
    offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    area = 0  # 周长
    for i in range(64):
        for j in range(64):
            if grid[i][j] == num:
                # 查找grid[i][j]四个方向的坐标有几个跟他不一样
                for a, b in offsets:
                    x = i + a
                    y = j + b
                    if 0 <= x < 64 and 0 <= y < 64:
                        if grid[x][y] != num:
                            area += 1
                    # 如果图形元素的上下左右方向的元素越界了，那么也要为对应图形的周长+1。
                    else:
                        area += 1

    return area


if __name__ == '__main__':
    # 处理输入
    n = int(input())
    # 有一个64×64的矩阵，每个元素的默认值为0，
    grid = [[0] * 64 for _ in range(64)]
    nums = []  # 记录要查找的单元格目标值
    for i in range(n):
        line = list(map(int, input().split()))
        val = line[0]
        nums.append(val)
        for j in range(1, len(line) - 1, 2):  # 12 34 56
            x = line[j]
            y = line[j + 1]
            grid[x][y] = val
    # print(grid)

    ans = []  # 最后结果
    for i in range(n):
        ans.append(getResult(grid, nums[i]))
    print(' '.join(map(str, ans)))
    # 输出	18 20
