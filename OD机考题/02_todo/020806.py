

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
limit = int(input())


max_sz = 0
left, right = 0, 0
used_money = 0
while right < n:
    used_money += nums[right]
    
    if used_money <= limit:
        cur_sz = right - left + 1
        max_sz = max(max_sz, cur_sz)
    else:
        while used_money > limit:
            used_money -= nums[left]
            left += 1

    right += 1


print(max_sz)

# 7
# 8
# 4
# 6
# 3
# 1
# 6
# 7
# 10
# 2

# 5
# 1
# 2
# 3
# 10
# 2
# 12
# 3