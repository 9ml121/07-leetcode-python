

import collections

n = int(input())
weights = list(map(int, input().split()))

projects = {}
for i in range(n):
    lines = input().split()
    name = lines[0]
    stars = list(map(int, lines[1:]))
    score = 0
    for i in range(5):
        score += weights[i] * stars[i]
    projects[name] = score

res = sorted(projects, key = lambda k : (-projects[k], k.lower()))
for i in range(n):
    print(res[i])


# 5
# 5 6 6 1 2
# cam 13 88 46 26 169
# gra 64 38 87 23 103
# luc 91 79 98 154 79
# leo 29 27 36 43 178
# ava 29 27 36 43 179