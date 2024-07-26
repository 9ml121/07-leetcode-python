


nums = list(map(int, input().split()))
n = len(nums)

res = []
for i in range(n):
    cur = nums[i]
    for j in range(i+1, i+n):
        nxt = nums[j % n]
        if nxt < cur:
            cur += nxt
            break

    res.append(cur)

print(' '.join(map(str, res)))

# 3 15 6 14