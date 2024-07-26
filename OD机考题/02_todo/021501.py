

k = int(input())
s = input()


lst = s.split('-')
ans = [lst[0]]
s2 = ''.join(lst[1:])

for i in range(0, len(s2), k):
    tmp = s2[i:i+k]
    lowers = 0
    uppers = 0
    for c in tmp:
        if 'a' <= c <= 'z':
            lowers += 1
        elif 'A' <= c <= 'Z':
            uppers += 1

    # print(tmp)
    if lowers > uppers:
        res = tmp.lower()
    elif lowers < uppers:
        res = tmp.upper()
    else:
        res = tmp
    ans.append(res)

print('-'.join(ans))
