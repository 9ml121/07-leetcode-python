"""
https://fcqian.blog.csdn.net/article/details/127490548
题目描述
You are given a car odometer which displays the miles traveled as an integer. The odometer has a defect, however: it proceeds from the digit 2 to the digit 4 and from the digit 7 to the digit 9, always skipping over the digit 3 and 8. This defect shows up in all positions (the one's, the ten's, the hundred's, etc.). For example, if the odometer displays 15229 and the car travels one mile, odometer reading changes to 15240 (instead of 15230).

给你一个汽车里程表，它以整数的形式显示行驶的英里数。然而，里程表有一个缺陷:它从数字2到数字4，从数字7到数字9，总是跳过数字3和8。这个缺陷出现在所有位置(1位，10位，100位，等等)。例如，如果里程表显示15229，而汽车行驶了一英里，则里程表读数变为15240(而不是15230)。

输入描述
Each line of input contains a positive integer in the range 1..999999999 which represents an odometer reading. (Leading zeros will not appear in the input.) The end of input is indicated by a line containing a single 0. You may assume that no odometer reading will contain the digit 3 and 8.

每一行输入的数范围是[1,999999999 ]，表示里程表读数。(前导零不会出现在输入中。)输入的结束由包含一个0的行表示。您可能会认为里程表读数中没有数字3和8。

输出描述
Each line of input will produce exactly one line of output, which will contain: the odometer reading from the input, a colon, one blank space, and the actual number of miles traveled by the car.

每一行输入将产生一行输出，其中将包含:从输入读取的里程表、一个冒号、一个空格和汽车实际行驶的英里数。

用例
输入	15
输出	12

输入	2005
输出	1028

输入	250
输出	160

输入	1500
输出	768

输入	999999
输出	262143
"""

# todo 8进制转10进制整数
# 类似：05-字符串&整数&哈希\位运算\靠谱的车.py
'''
题目解析
这题和算法 - https://blog.csdn.net/qfc_128220/article/details/127418150?spm=1001.2014.3001.5502
一样，只是靠谱的车是九进制，本题是八进制。
8进制
1=>1
2=>2
+1
3=>4=> (4-1)*8^0
4=>5
5=>6
6=>7
+1
7=>9=> (9-2)*8^0
8=>10

8=>11
10=>12
+1
11=>14=> 1*8^1 + (4-1)*8^0
12=>15
13=>16
14=>17
+1
15=>19=> 1*8^1 + (9-2)*8^0
16=>20


160=>250=> 2*8^2 + (5-1)*8^1 + 0*8^0
1500=> 1*8^3 + (5-1)*8^2 + 0*8^1 + 0*8^0=768
999999 =>(9-2)*8^5 + (9-2)*8^4 + (9-2)*8^3 + (9-2)*8^2 + (9-2)*8^1 + (9-2)*8^0 = 262143
'''

# 输入：里程表读数，里程表读数中没有数字3和8。
# 它从数字2到数字4，从数字7到数字9，总是跳过数字3和8
s = input()

# 输出：汽车实际行驶的英里数
ans = 0
# todo: s实际代表一个8进制字符串，从低位开始算起，转换为10进制整数
for i, x in enumerate(s[::-1]):
    # i代表8进制的位置下标，x代表该位置数字，需要计算x的正确数字
    num = int(x)
    # 注意下面2个顺序不能颠倒
    if num > 8:
        # 跳过了3和8这2个数字
        num -= 2
    elif num > 3:
        # 只跳过了3这一个数字
        num -= 1
    
    ans += num * (8**i)
print(ans)