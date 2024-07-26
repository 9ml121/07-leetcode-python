

N, M =  map(int, input().split())
pfs = []
for _ in range(N):
    pfs.append(int(input()))

tests = {}
for i in range(M):
    line = list(map(int, input().split()))
    sumP = 0
    for idx in line:
        sumP += pfs[idx-1]
    tests[i+1] = sumP

order_tests = sorted(tests.items(), key=lambda x:(-x[1], x[0]))
for k, v in order_tests:
    print(k)



