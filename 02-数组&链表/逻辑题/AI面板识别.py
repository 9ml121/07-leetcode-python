"""
题目描述
AI识别到面板上有N（1 ≤ n ≤ 100）个指示灯，灯大小一样，任意两个之间无重叠。

由于AI识别误差，每次别到的指示灯位置可能有差异，以4个坐标值描述AI识别的指示灯的大小和位置(左上角x1,y1，右下角x2,y2)，

请输出先行后列排序的指示灯的编号，排序规则：
- 每次在尚未排序的灯中挑选最高的灯作为的基准灯，
- 找出和基准灯属于同一行所有的灯进行排序。两个灯高低偏差不超过灯半径算同一行（即两个灯坐标的差 ≤ 灯高度的一半）。

输入描述
第一行为N，表示灯的个数
接下来N行，每行为1个灯的坐标信息，格式为：

编号 x1 y1 x2 y2

编号全局唯一
1 ≤ 编号 ≤ 100
0 ≤ x1 < x2 ≤ 1000
0  ≤  y1 < y2 ≤ 1000

输出描述
排序后的编号列表，编号之间以空格分隔

用例
输入	5
1 0 0 2 2
2 6 1 8 3
3 3 2 5 4
5 5 4 7 6
4 0 4 2 6
输出	1 2 3 4 5
说明
"""


# light类只存储灯的左上角坐标和编号
class light:
    def __init__(self, ids, x, y):
        self.ids = ids
        self.x = x
        self.y = y



# 输入
# 灯的个数
# n = int(input())
# 每行为1个灯的坐标信息，格式为：编号 x1 y1 x2 y2
# datas = [list(map(int, input().split())) for _ in range(n)]

# 测试数据
n = 5
datas = [[1, 0, 0, 2, 2], [2, 6, 1, 8, 3], [
    3, 3, 2, 5, 4], [5, 5, 4, 7, 6], [4, 0, 4, 2, 6]]

# 输出：排序后的编号列表，编号之间以空格分隔
# 排序规则只针对每个灯左上角坐标:
# todo 注意题目给出的x,y坐标跟实际坐标是相反的
lights = [light(data[0], data[2], data[1]) for data in datas]

# 把第一个灯的坐标作为排序基准点
start = lights[0]
# 计算灯半径,  注意：所有灯大小都一样
r = (start.y - start.x) // 2

ans = []
sameRow = [start]
queues = [start]
# 从第2个灯开始
for i in range(1, n):
    light = lights[i]

    if light.x - start.x <= r:
        # 不超过半径就证明在同一行, 根据同一行规则进行比较
        sameRow.append(light)
    else:
        # 在同一行，根据y坐标升序
        sameRow.sort(key=lambda light: light.y)
        for j in range(len(sameRow)):
            ans.append(sameRow[j].ids)

        # 然后清空sameRow,开始新一行统计
        sameRow.clear()
        start = light
        sameRow.append(start)
        
# 还有最后一行没处理
if sameRow:
    sameRow.sort(key=lambda light: light.y)
    for j in range(len(sameRow)):
        ans.append(sameRow[j].ids)

print(' '.join(map(str, ans)))
