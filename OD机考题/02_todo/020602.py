

n, total_money, limit_risk = map(int, input().split())
rates = list(map(int, input().split()))  
risks = list(map(int, input().split()))
limit_money = list(map(int, input().split()))

max_profit = 0
min_risks = float('inf')
selected = {}

# n选2
for i in range(n):
    # 1.投资单个产品
    if risks[i] <= limit_risk:
        money_i = min(limit_money[i], total_money)
        total_profit = rates[i] * money_i
        total_risk = risks[i]
        if total_profit > max_profit or (total_profit == max_profit and total_risk < min_risks):
            max_profit = total_profit
            min_risks = total_risk
            selected.clear()
            selected[i] = money_i
    else:
        continue
    
    # 2.投资2个产品
    for j in range(i+1, n):
        if risks[i] + risks[j] <= limit_risk:
            # 先比较收益，优先买收益大的
            if rates[i] > rates[j]:
                money_i = min(limit_money[i], total_money)
                money_j = min(total_money - money_i, limit_money[j])
            elif rates[i] < rates[j]:
                money_j = min(limit_money[j], total_money)
                money_i = min(total_money - money_j, limit_money[i])
            # 在比较收益相同，优先买风险低
            elif risks[i] < risks[j]:
                money_i = min(limit_money[i], total_money)
                money_j = min(total_money - money_i, limit_money[j])
            else:
                money_j = min(limit_money[j], total_money)
                money_i = min(total_money - money_j, limit_money[i])

            # 保留收益最大，风险最小的
            total_profit = rates[i] * money_i + rates[j] * money_j
            total_risk = risks[i] + risks[j]
            if total_profit > max_profit or (total_profit == max_profit and total_risk < min_risks):
                max_profit = total_profit
                min_risks = total_risk
                selected.clear()
                selected[i] = money_i
                selected[j] = money_j

res = []
for i in range(n):
    if i in selected:
        res.append(selected[i])
    else:
        res.append(0)
        
print(' '.join(map(str, res)))


# 5 100 10
# 10 20 30 40 50
# 3 4 5 6 10
# 20 30 20 40 30