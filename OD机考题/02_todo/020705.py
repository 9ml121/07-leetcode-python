

import sys
sys.setrecursionlimit(5000)
rows, cols, limit = map(int, input().split())

offsets = [(-1, 0), (1, 0), (0,-1), (0,1)]
def inArea(x, y):
    return 0 <= x < rows and 0 <= y < cols

def calSum(x, y):
    num = 0
    while x > 0:
        num += (x % 10)
        x //= 10

    while y > 0:
        num += (y % 10)
        y //= 10

    return num   


res = 0
visited = [[False] * cols for _ in range(rows)]
def dfs(i, j):
    global res
    visited[i][j] = True
    res += 1

    for ox, oy in offsets:
        newX, newY = i+ox, j + oy
        num = calSum(newX, newY)
        if inArea(newX, newY) and not visited[newX][newY] and num <= limit:
            dfs(newX, newY)

dfs(0, 0)
print(res)

# 5 4 7