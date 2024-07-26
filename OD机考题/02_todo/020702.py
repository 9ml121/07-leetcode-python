
import collections

n = int(input())
words = []
for i in range(n):
    words.append(input())
strs = input()

cnts = collections.Counter(strs)

res1 = []
res = 0
for word in words:
    tmp = cnts.copy()
    flag = True
    for c in word:
        if tmp.get(c, 0) == 0 and tmp.get('?', 0) == 0:
            flag = False
            break
        else:
            if tmp.get(c, 0) > 0:
                tmp[c] -= 1
            else:
                tmp['?'] -= 1
    if flag:
        res1.append(word)
        res += 1

print(res, res1)  

# 4
# cat
# bt
# hat
# tree
# atach??

