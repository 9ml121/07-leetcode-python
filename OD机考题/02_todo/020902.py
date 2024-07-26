

n = int(input())
luck = int(input())
steps = list(map(int, input().split()))

maxPos = 0
curPos = 0
for step in steps:
    if step == luck:
        if step < 0:
            step -= 1
        elif step > 0:
            step += 1
        else:
            step += 0
    curPos += step
    maxPos = max(maxPos, curPos)

print(maxPos)
