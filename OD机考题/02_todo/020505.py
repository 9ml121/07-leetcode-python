

import math


nums = list(map(int, input().split()))
# nums.sort()
n = len(nums)

def get_time(cap):
    time = 0
    for num in nums:
        time += math.ceil(num / cap)
    return time

if n > 8:
    res = -1
else:
    right = max(nums)
    left = 0
    while left <= right:
        mid = (left + right) // 2
        time = get_time(mid)
        print(left, right, time)

        if time > 8:
            left = mid + 1
        else:
            right = mid - 1

    res = left

print(res)

# 30 12 25 8 19