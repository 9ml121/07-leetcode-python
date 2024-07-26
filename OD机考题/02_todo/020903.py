

na, nb = map(int, input().split())
lst_a = list(map(int, input().split()))
lst_b = list(map(int, input().split()))

suma = sum(lst_a) 
sumb = sum(lst_b) 
avg = (suma + sumb)//2

lst_a.sort()
for num in lst_a:
    if suma - num >= avg:
        continue
    need = avg - (suma-num)
    if need in lst_b:
        print(f'{num} {need}')
        break


# 3 2
# 1 2 5
# 2 4
# ==> 5 4

# 2 2
# 1 1
# 2 2
# ==> 1 2
        
# 1 2
# 2
# 1 3
# ==> 2 3
        
# 2 2
# 1 2
# 2 3
# ==> 1 2