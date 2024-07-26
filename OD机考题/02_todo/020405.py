

s = input()
uppers = 0
lowers = 0
nums = 0
others = 0

res1 = []
res2 = False

i = len(s) - 1
while i >= 0:
    if s[i] == '<':
        i -= 2
    else:
        if s[i].isupper():
            uppers += 1 
        elif s[i].islower():
            lowers += 1
        elif s[i].isdigit():
            nums += 1
        else:
            others += 1

        res1.append(s[i])
        i -= 1

if any([len(res1) < 8 , uppers == 0, lowers == 0, nums == 0,others == 0]):
    res2 = False
else:
    res2 = True

print(''.join(res1[::-1]), res2,sep=',')


# ABC<c89%000<