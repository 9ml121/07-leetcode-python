import collections

n = map(int, input())
nums = list(map(int, input().split()))
limit = int(input())

cnts = collections.Counter(nums)

# 方法1
# res = [k for k , v in sorted(cnts.items(), key=lambda k:(-cnts[k], k)) if v >= limit]
# print(len(res))
# if len(res) > 0:
#     for num in res:
#         print(num)


# 方法2
items = list(filter(lambda x: x[1] >= limit, cnts.items()))
print(len(items))
if len(items) > 0:
    items.sort(key = lambda x: (-x[1], x[0]))
    for k , v in items:
        print(k)
# 10
# 1 2 1 2 1 2 1 2 1 2
# 5