import os

s1 = [1, 2, 3]

# comp表达式
dic = {d: d for d in s1}


# 智能注释
# 变量重命名:可以使用 PyCharm 的 Refactor 功能，它会自动匹配作用域，既做到批量更改，也做到不误伤。
def fun(aa, b):
    """

    Args:
        aa:
        b:

    Returns:

    """
    print(aa + b)


# ...if表达式
'''
在该句子最后增添.if 并点击 Tab 键，PyCharm 将修复该 if 条件句。
该用法同样适用于 True.while。 a.print
这即是 PyCharm 的 Postfix Completion 功能，它可以帮助用户减少退格键使用次数。
'''
a = 10
if a > 7:
    pass
while a:
    pass
print(a)

if a is None:
    pass

# for表达式:iter
items = [1, 2, 3, 4]
for item in items:
    pass

# main表达式、
if __name__ == '__main__':
    pass

# !!!快速开启新的一行 shift + Enter
# 快捷键：Ctrl + Shift + ↩，自动结束代码，行末自动添加分号
# 快捷键：Alt + ↩，也称万能键，显示意向动作和快速修复代码
if not s1.append(a):
    pass
else:
    pass

# 善用 TODO 记录待办事项
