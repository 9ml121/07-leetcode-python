


strs = input()
cnt_x, cnt_y = 0, 0
res = 0
for c in strs:
    if c == 'X':
        cnt_x += 1
    else:
        cnt_y += 1
    
    if cnt_x == cnt_y:
        res += 1

print(res)

# XXYYXY
# XYXYYYXX