

s = ['0'] + list(input()) + ['0']
n = len(s)

res = 0
for i in range(1, n-1):
    if s[i] == '0' and s[i-1] == '0' and s[i+1] == '0':
        res += 1
        s[i] = '1'

print(res)



    
 