import bisect

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
while len(nums) >= 3:
    z, y, x = nums.pop(), nums.pop(), nums.pop()
    newNum = abs((z-y) - (y-x))

    if newNum > 0:
        idx = bisect.bisect_left(nums, newNum)
        nums.insert(idx, newNum)

ans = 0
if len(nums) > 0:
    ans = max(nums)


print(ans)

