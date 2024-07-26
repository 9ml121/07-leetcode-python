

A = 'xxcdefg'
B = 'cdefghi'
V = 5

n = len(A)
diffs = []
for i in range(n):
    diffs.append(abs(ord(A[i])-ord(B[i])))

l = 0
r = 0
sumV = 0
maxLen = 0
while r < n:
    sumV += diffs[r]
    if sumV  <= V:
        maxLen = max(maxLen, r-l+1)
    else:
        sumV -= diffs[l]
        l += 1

    r += 1
print(maxLen)