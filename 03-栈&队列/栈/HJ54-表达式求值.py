"""
描述
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。

数据范围：运算过程中和最终结果均满足 ∣value∣≤ 2^31 − 1  ，即只进行整型运算，确保输入的表达式合法
输入描述：
输入算术表达式

输出描述：
计算出结果值

示例1
输入：
400+5

输出：
405
"""

"""
python 直接用eval可以解决问题，但是失去了题目的意义。用python重写eval函数，也能解决表达式中可能出现的多位数的情况。
# 这道题的考察用法应该是用堆栈，因为python3没有栈，所以用list仿造一个堆栈。
"""


# eval函数用法
# print(eval(input()))

# 亲自实现eval函数功能
def cal(nums, ops):
    # nums = [3, 1, 6, 3]
    # ops = ['+', '*', '/']
    # 处理计算的优先级：先计算乘除，在计算加减
    if "*" in ops or "/" in ops:
        for op in ops.copy():
            i = ops.index(op)
            if op == "*":
                b = nums.pop(i + 1)
                a = nums.pop(i)
                nums.insert(i, a * b)
                ops.pop(i)
            elif op == "/":
                b = nums.pop(i + 1)
                a = nums.pop(i)
                nums.insert(i, a / b)
                ops.pop(i)

    for op in ops.copy():
        i = ops.index(op)
        if op == "+":
            b = nums.pop(i + 1)
            a = nums.pop(i)
            nums.insert(i, a + b)
            ops.pop(i)
        elif op == "-":
            b = nums.pop(i + 1)
            a = nums.pop(i)
            nums.insert(i, a - b)
            ops.pop(i)

    return float(nums[0])


# 判断字符串是否是数字(数字、小数、负数、负小数、0)
# 字符串
def check_num(str_number):
    # str_numbers = ["-0.3","0","2","0.002","-5","china","中国","-like","-中国"]
    # for str_number in str_numbers:
    if (str_number.split(".")[0]).isdigit() \
            or str_number.isdigit() \
            or (str_number.split('-')[-1]).split(".")[-1].isdigit():
        return True
    else:
        return False


# 合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。即只进行整型运算
# s = input()
# s = "400+5"
# s = "5-3+9*6*(6-10-2)"
# s = '10*10+8-6-2+10-7+1+8+(1+6+(9*9)*8+1)'
# s = '(7+5*4*3+6)'
# s = '-1*(-1-1)'
s = '400+(-100/5)+5-2'
# [3,1,2,3]
# [+,*,/]
# 计算括号内的，考虑算法优先级
stack = []  # 存数字和运算符
tmp = ""  # 数字可能有2位数以上，也可能为负数，这里用来临时存单个数字字符串
i = 0
# 负数可能出现在字符开头，或者左括号右边。判断第一个是不是负数
if s[0] == '-':
    tmp += '-'
    i += 1
while i <= len(s) - 1:
    c = s[i]
    if check_num(c):
        tmp += c
        i += 1
    elif c in ['+', '-', '*', '/']:
        # 操作符左边可能是数字，也可能是右括号，所以这里要判断tmp
        if tmp:
            stack.append(tmp)
        tmp = ''
        stack.append(c)
        i += 1
    elif c == '(':  # 左括号左边只可能是操作符，或者字符开头。右边有可能是负数
        if s[i + 1] == '-':
            tmp += '-'
            i += 2  # 这里要跳2位
        else:
            i += 1
        stack.append(c)
    elif c == ')':
        stack.append(tmp)
        tmp = ''
        # 计算括号内的值
        nums = []
        ops = []
        new = 0  # 计算的中间结果
        while stack[-1] != "(":  # 10*10+8-6-2+10-7+1+8+(1+6+(9*9
            x = stack.pop()
            if check_num(x):
                nums.append(float(x))
            else:
                ops.append(x)
        nums.reverse()
        ops.reverse()
        new = cal(nums, ops)
        stack.pop()  # 将左括号删除
        stack.append(str(new))  # 将新的计算结果加入到lst
        i += 1
if tmp:
    stack.append(tmp)

nums = []
ops = []
for x in stack:
    if check_num(x):
        nums.append(float(x))
    else:
        ops.append(x)
res = cal(nums, ops)
print(int(res))
