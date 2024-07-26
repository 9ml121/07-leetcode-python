


s = '1220*19*34'


reversd_res = []
def solution():
    i = len(s) - 1
    while i >= 0 :
        c = s[i]
        if c == '*':
            i -= 2
            num = int(s[i:i+2])
        else:
            num = int(c)

        letter = chr(num + 96)
        reversd_res.append(letter)

        i -= 1
    return ''.join(reversd_res[::-1])

res = solution()
print(res)