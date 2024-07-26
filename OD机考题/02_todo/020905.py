

nums = [0,1,2,4,3,1,0,0,1,2,3,1,2,1,0]

ans = 0
nums = [0] + nums + [0]
n = len(nums)
for i in range(1, n-1):
    if nums[i-1] < nums[i]  and nums[i] > nums[i+1]:
        ans += 1
print(ans)