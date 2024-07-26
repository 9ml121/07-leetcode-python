

s = input()


i, j = 0, 0
stack = []
while j < len(s):
    if s[j] == '$':
        # stack.append(s[j])
        j += 1
        i = j
    elif s[j] == '#':
        x = stack.pop()
        j += 1
        i = j
        while j < len(s) and s[j].isdigit():
            j += 1
        y = int(s[i:j])
        res = 4 * x + 3 * y + 2
        stack.append(res)
    else:
        while j < len(s) and s[j].isdigit():
            j += 1
        num = int(s[i:j])
        stack.append(num)

# print(stack)
x = stack[0]
for i in range(1, len(stack)):
    y = stack[i]
    x = 2 * x + y + 3
print(x)


# 方法2：正则
import re
# 输入获取
s = input()

# 算法入口
def getResult(s):
    p = re.compile("(\\d+)#(\\d+)")

    while True:
        m = p.search(s)
        if m:
            subS = m.group()
            x = int(m.group(1))
            y = int(m.group(2))
            # 注意这里replace只能进行替换第一次出现的，不能替换多次，因此replace方法第三个参数为1，表示只替换首次匹配
            s = s.replace(subS, str(4 * x + 3 * y + 2), 1)
        else:
            break

    arr = list(map(int, s.split("$")))

    x = arr[0]
    for y in arr[1:]:
        x = 2 * x + y + 3

    return x


# 算法调用
print(getResult(s))

""" 
输入	7#6$5#12
输出	157
说明	7#6$5#12  
=(4*7+3*6+2)$5#12
=48$5#12
=48$(4*5+3*12+2)
=48$58
=2*48+58+3
=157 
"""
