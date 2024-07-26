

nums = [1,3,5,5,6,8,9]


def check(level:int, nums:list):
    L = 0
    R = len(nums)-1
    height = 0
    while L <= R:
        if nums[R] == level:
            R -= 1
            height += 1
        elif nums[R] + nums[L] == level:
            R-=1
            L+=1
            height += 1
        else:
            return -1
    return height
        
# 只用1个或者用2个
def main():
    # 最多层
    maxHeight = -1
    nums.sort()
    n = len(nums)
    if n == 1:
        return 1
    if n > 1:
        maxHeight = max(check(nums[-1], nums), check(nums[0] + nums[-1], nums))
    
    return maxHeight

    
print(main())