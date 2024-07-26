

# 输入
# 第一行为初始信息
C, R, y, x, sy, sx, t = map(int, input().split())
# 第二行开始一共 h 行，为二维矩阵信息
grid = [input() for _ in range(R)]

# 测试数据
# C, R, y, x, sy, sx, t = 12, 7, 2, 1, 1, -1, 13
# grid = ['001000010000',
#         '001000010000',
#         '001000010000',
#         '001000010000',
#         '001000010000',
#         '001000010000',
#         '001000010000',
#         ]

# 输出：经过1的个数
# 左上角为[0, 0], 代表[列，行]
cnt = 0
if grid[x][y] == '1':
    cnt = 1
for i in range(t):
    # print(x, y)
    # 总共跑t次，
    # 反射规律
    if (x == 0 and sx < 0) or (x == R-1 and sx > 0):
        sx = -sx
    if (y == 0 and sy < 0) or (y == C-1 and sy > 0):
        sy = -sy

    x += sx
    y += sy

    # 统计经过网格为1的个数
    if grid[x][y] == '1':
        cnt += 1

print(cnt)
