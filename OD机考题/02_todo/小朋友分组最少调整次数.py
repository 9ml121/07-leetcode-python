

nums = list(map(int, input().split()))
adj_nums = list(map(int, input().split()))
n = len(nums)

groups = {}
for i, num in enumerate(adj_nums):
    group = i // 3
    groups[num] = group

nums_to_groups = list(map(lambda x : groups[x], nums))
# print(nums)
[0, 0, 1, 0, 1, 1]

old_groups = [] *

    
    
    







""" 
1 3 5 2 4 6
1 2 3 4 5 6

[1,3,5], [2,4,6]
"""
