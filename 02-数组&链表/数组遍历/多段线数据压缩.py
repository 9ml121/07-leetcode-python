"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134900877?spm=1001.2014.3001.5501

题目描述
下图中，每个方块代表一个像素，每个像素用其行号和列号表示。

image

为简化处理，多线段的走向只能是水平、竖直、斜向45度。

上图中的多线段可以用下面的坐标串表示：(2,8),(3,7),(3,6),(3,5),(4,4),(5,3),(6,2),(7,3),(8,4),(7,5)。

但可以发现，这种表示不是最简的，其实只需要存储6个蓝色的关键点即可，它们是线段的起点、拐点、终点，而剩下4个点是冗余的。

现在，请根据输入的包含有冗余数据的多线段坐标列表，输出其最简化的结果。

输入描述
2 8 3 7 3 6 3 5 4 4 5 3 6 2 7 3 8 4 7 5

所有数字以空格分隔，每两个数字一组，第一个数字是行号，第二个数字是列号；
行号和列号范围 为 [0, 64)，用例输入保证不会越界，考生不必检查；
输入数据至少包含两个坐标点
输出描述
2 8 3 7 3 5 6 2 8 4 7 5

压缩后的最简化坐标列表，和输入数据的格式相同。

备注
输出的坐标相对顺序不能变化

用例1
输入
2 8 3 7 3 6 3 5 4 4 5 3 6 2 7 3 8 4 7 5
输出
2 8 3 7 3 5 6 2 8 4 7 5
说明
如上图所示，6个蓝色像素的坐标依次是：

(2, 8)、(3, 7)、(3, 5)、(6, 2)、(8, 4)、(7, 5)

将他们按顺序输出即可。
"""

line = list(map(int, input().split()))
pos = []
for i in range(0, len(line), 2):
    pos.append([line[i], line[i+1]])

def solution(pos):
    n = len(pos)
    ans = []
    if n <= 2:
        return pos

    ans.append(pos[0])
    for i in range(1, n-1):
        ox1 = pos[i][0] - pos[i-1][0]
        oy1 = pos[i][1] - pos[i-1][1]
        # 注意：这里是计算斜率的一种方法，
        # 另外一种方法是(1,2), (3,6) => x = x/max(abs(x), abs(y)), y = y/max(abs(x), abs(y))
        o1 = ox1/oy1 if oy1 != 0 else 90

        ox2 = pos[i+1][0] - pos[i][0]
        oy2 = pos[i+1][1] - pos[i][1]
        o2 = ox2/oy2 if oy2 != 0 else 90

        if o1 == o2:
            continue

        ans.append(pos[i])

    ans.append(pos[n-1])
    return ans


ans = solution(pos)
ans2 = []
for pos in ans:
    ans2.extend(pos)
print(' '.join(map(str, ans2)))
