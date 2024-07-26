


num = int(input())

res = 'N'
lst = []
if num < 3:
    res = 'N'
elif num  % 2 == 1:
    res = f'2: {num//2} + {num//2 + 1}'
else:
    # 6 8 10 12 偶数
    for i in range(3, num // 2 + 1, 2):
        if num % i == 0:  
            mid = num // i
            
            odd = i
            even = mid * 2
            if odd <= even:
                # 奇数个
                res = f'{odd}: {mid - (i-1)//2} ~ {mid + (i-1)//2}'
            else:
                # 偶数个
                res = f'{even}: {i//2 - (mid-1)} ~ {i//2 + 1 + {mid-1}}'
            break
print(res)
