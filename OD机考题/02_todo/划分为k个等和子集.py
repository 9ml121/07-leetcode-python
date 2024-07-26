

# nums = [2,2,2,2,2,3,5,9,9]
nums = [9,5,4,3,3,3]


def main():
    # 数组划分为k个等和子集
    max_k = len(nums)
    min_k = 2
    nums.sort(reverse=True)  # 9,5,4,3,3,3
    sumV = sum(nums)
    for k in range(max_k, min_k-1, -1):
        if canPartition(nums[:], k, sumV):
            return k
        
    return -1

def canPartition(nums, k, sumV):
    if sumV % k != 0:
        return False
    
    subV = sumV // k
    
    if nums[0] > subV:
        return False
    while nums and nums[0] == subV:
        nums.pop(0)
        k -= 1
    
    buckets = [0] * k
    return  partition(nums, 0,  buckets, subV)
         
def partition(nums, idx,  buckets, subV):
    if idx == len(nums):
        return True
    
    for i in range(len(buckets)):
        if i > 0 and buckets[i] == buckets[i-1]:
            continue

        if buckets[i] + nums[idx] > subV:
            continue

        buckets[i] += nums[idx]
        print(buckets)
        if partition(nums, idx+1, buckets, subV):
            return True
        buckets[i] -= nums[idx]        

    return False

print(main())  




