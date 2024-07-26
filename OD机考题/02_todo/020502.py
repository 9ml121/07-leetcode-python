

n_stu, n_course = map(int, input().split())
courses = input().split()

stu_info = {}
for i in range(n_stu):
    info = input().split()
    stu_info[info[0]] = list(map(int, info[1:]))

rank_course = input()
idx = courses.index(rank_course) if rank_course in courses else -1

if idx != -1:
    res = sorted(stu_info, key=lambda k:(-stu_info[k][i], k))
else:
    res = sorted(stu_info, key=lambda k:(-sum(stu_info[k]), k))
    
print(' '.join(res))

# 3 2
# aa bb
# q1 95 90
# q2 88 95
# q3 90 95