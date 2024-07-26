

import collections
n = int(input())

res = [{} for _ in range(10)]
for i in range(n):
    s = input()
    lst = s.split('/')
    # print(lst)
    for i in range(1, len(lst)):
        key = lst[i]
        res[i][key] = res[i].get(key, 0) + 1

level, target = input().split()
level = int(level)

ans = 0
if level >= 10:
    ans = 0
else:
    ans = res[level].get(target, 0)

print(ans)


# 5
# /aa/bb/cc/dd
# /aa/bb
# /aa
# /aa/ee/cc/dd
# /aa/ff/cc/dd
# 4 two