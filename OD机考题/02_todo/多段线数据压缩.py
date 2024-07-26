line = list(map(int, input().split()))
pos = []
for i in range(0, len(line), 2):
    pos.append([line[i], line[i+1]])


def sulution(pos):
    n = len(pos)
    ans = []

    ox1, oy1 = 0, 0
    for i in range(n-1):
        x2 = pos[i+1][0] - pos[i][0]
        y2 = pos[i+1][1] - pos[i][1]
        base = max(abs(x2), abs(y2))

        ox2, oy2 = x2//base, y2//base
        if ox2 == ox1 and oy2 == oy1:
            continue

        ans.extend(pos[i])
        ox1, oy1 = ox2, oy2

    ans.extend(pos[n-1])
    return ans


ans = sulution(pos)
print(' '.join(map(str, ans)))
