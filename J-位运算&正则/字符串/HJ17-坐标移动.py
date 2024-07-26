"""
描述
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：
合法坐标为A(或者D或者W或者S) + 数字（两位以内）
坐标之间以;分隔。
非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
处理过程：
起点（0,0）
+   A10   =  （-10,0）
+   S20   =  (-10,-20)
+   W10  =  (-10,-10)
+   D30  =  (20,-10)
+   x    =  无效
+   A1A   =  无效
+   B10A11   =  无效
+  一个空 不影响
+   A10  =  (10,-10)

结果 （10， -10）

输入描述：
一行字符串

输出描述：
最终坐标，以逗号分隔

输入：
A10;S20;W10;D30;X;A1A;B10A11;;A10;
输出：
10,-10

输入：
ABC;AKL;DA1;
输出：
0,0
"""


# 分析：
# 1。排除输入的异常值，可以用正则，也可以用常规方法，正则的话就代码少一点
# 2。后面输出的结果只要靠题意理解正确

# 方法1：正则
def method1():
    import re
    # s = input()
    s = 'A10;S20;W10;D30;X;A1A;B10A11;;A10;'
    lst = list(filter(None, s.split(';')))
    # print(stack)
    # ['A10', 'S20', 'W10', 'D30', 'X', 'A1A', 'B10A11', 'A10']
    x, y = 0, 0
    # 合法坐标为A(或者D或者W或者S) + 数字（两位以内）
    # 坐标之间以;分隔。
    # 非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
    for elem in lst:
        if re.match(r'^[ADSW]\d{1,2}$', elem):
            # print(elem)
            num = int(elem[1:])
            # A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
            if elem[0] == 'A':
                x -= num
            elif elem[0] == 'D':
                x += num
            elif elem[0] == 'W':
                y += num
            elif elem[0] == 'S':
                y -= num
    print(str(x) + ',' + str(y))


# 方法2：不用正则
s = input()
# s = 'A10;S20;W10;D30;X;A1A;B10A11;;A10;'
lst = list(filter(None, s.split(';')))
# print(stack)
# ['A10', 'S20', 'W10', 'D30', 'X', 'A1A', 'B10A11', 'A10']
x, y = 0, 0
# 合法坐标为A(或者D或者W或者S) + 数字（两位以内）
# 坐标之间以;分隔。
# 非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。
for elem in lst:
    alpha = elem[0]
    num = elem[1:]
    if alpha in ['A', 'D', 'S', 'W'] and num.isdigit() and 1 <= len(num) <= 2:
        num = int(num)
        # A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。
        if elem[0] == 'A':
            x -= num
        elif elem[0] == 'D':
            x += num
        elif elem[0] == 'W':
            y += num
        elif elem[0] == 'S':
            y -= num
print(str(x) + ',' + str(y))
