
import collections


class Flag:
    def __init__(self) -> None:
        self.minRow = float('inf')
        self.maxRow = float('-inf')
        self.minCol = float('inf')
        self.maxCol = float('-inf')

    def setRowCol(self, i, j):
        self.minRow = min(self.minRow, i)
        self.maxRow = max(self.maxRow, i)
        self.minCol = min(self.minCol, j)
        self.maxCol = max(self.maxCol, j)
    
# cols, rows = 3, 3
cols, rows = map(int, input().split())

maps = collections.defaultdict(Flag)
# 查找相同数字的最大/最小横坐标和纵中标
for i in range(rows):
    lines = list(map(int, input().split()))
    for j in range(cols):
        if lines[j] != 0:
            maps[lines[j]].setRowCol(i, j)

maxArea = 0
for flag in maps.values():
    area = (flag.maxRow - flag.minRow + 1) * (flag.maxCol - flag.minCol + 1)
    maxArea = max(maxArea, area)

print(maxArea)