



import math

# 3 5
n, rows = map(int,  input().split())
# print(n,rows)
cols = math.ceil(n/rows)

res = [['*'] * cols for _ in range(rows)]
top, bottom = 0, rows-1
left, right = 0, cols-1
num = 1
x ,y = 0, 0
while num <= n:
    # 上
    while num <= n and y <= right:
        res[x][y] = str(num)
        num += 1
        y += 1
    
    top += 1
    y -= 1
    x += 1

    # 右边
    while num <= n and x <= bottom:
        res[x][y] = str(num)
        num += 1
        x += 1
    
    right -= 1
    x -= 1
    y -= 1

    # 下边
    while num <= n and y >= left:
        res[x][y] = str(num)
        num += 1
        y -= 1
    
    bottom -= 1
    y += 1
    x -= 1

    # 左边
    while num <= n and x >= top:
        res[x][y] = str(num)
        num += 1
        x -= 1
    left += 1
    x += 1
    y += 1

for i in range(rows):
    print(' '.join(res[i]))
