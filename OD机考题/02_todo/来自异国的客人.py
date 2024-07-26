""" 
题目描述
有位客人来自异国，在该国使用 m 进制计数。

该客人有个幸运数字n（n < m），每次购物时，其总是喜欢计算本次支付的花费（折算为异国的价格后）中存在多少幸运数字。

问：当其购买一个在我国价值 k 的产品时，其中包含多少幸运数字?        

输入描述
第一行输入为 k，n，m。

其中：

k 表示该客人购买的物品价值（以十进制计算的价格）
n 表示该客人的幸运数字
m 表示该客人所在国度采用的进制
输出描述
输出幸运数字的个数，行末无空格

备注
当输入非法内容时，输出0

用例
输入	10 2 4
输出	2
说明	10用4进制表示时为22，同时，异国客人的幸运数字是2，故而此处输出为2，表示有2个幸运数字。

输入	10 4 4
输出	0
说明	
此时客人的幸运数字为4，但是由于该国最大为4进制，故而在该国的进制下不可能出现幸运数字，故而返回0。

5 1 4
23 1 12

# 按照m进制的 “位值” 来对比幸运数 
"""

k, luck, carry = map(int, input().split())
# luck < carry

# 将十进制数字转换为任意进制(除留取余)
def decimal_to_baseX(decimal:int, x):
    # baseX = ''
    cnt = 0
    while decimal > 0:
        decimal, mod = divmod(decimal, x)
        
        # 按照m进制的 “位值” 来对比幸运数
        if mod == luck:
            cnt += 1

        # baseX = str(mod) + baseX
    
    return cnt

ans = decimal_to_baseX(k, carry)
# ans = baseX.count(str(luck))
print(ans)

