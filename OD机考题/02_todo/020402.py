

n = 4
vals = [100,200,300,500]
total = vals[::]
for i in range(n-1):
    n1, n2 = map(int, input().split())
    total[n1-1] += vals[n2-1]

print(total)
print(max(total))
