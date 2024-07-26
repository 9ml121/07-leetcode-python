import bisect

nums = list(map(int, input().split(',')))
target = int(input())

# idx = bisect.bisect_left(nums, target)
# print(idx + 1)

# 93,95,97,100,102,123,155
# 180

def bst(nums, t):
    lo,hi = 0, len(nums)-1
    
    while lo <= hi:
        mid = (lo+hi)//2
        num = nums[mid]
        if target > num:
            lo = mid+1
        elif target < num:
            hi = mid-1
        else:
            return mid
    return lo if lo < len(nums) else len(nums)

idx = bst(nums, target)
print(idx+1)