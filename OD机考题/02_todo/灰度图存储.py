""" 
灰度图存储
"""

line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))


rows,cols = line1[0], line1[1]
search = line2[0] * cols + line2[1]
grid = [[-1] * cols for _ in range(rows)]
pre, cur = 0, 0
x0, y0 = 0, 0
ans = -1
for i in range(2, len(line1), 2):
    val = line1[i]
    cnt = line1[i+1]
    cur += cnt
    if pre <= search < cur:
        ans = val
        break

    pre = cur
print(ans)


"""
10 10 56 34 99 1 87 8 99 3 255 6 99 5 255 4 99 7 255 2 99 9 255 21
3 4
==> 99

10 10 255 34 0 1 255 8 0 3 255 6 0 5 255 4 0 7 255 2 0 9 255 21
3 5
==> 255
"""