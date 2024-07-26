"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127341945

OJ用例
https://hydro.ac/d/HWOD2023/p/OD241/solution

题目描述
一个整数可以由连续的自然数之和来表示。

给定一个整数，计算该整数有几种连续自然数之和的表达式，且打印出每种表达式

输入描述
一个目标整数T (1 <=T<= 1000)

输出描述
该整数的所有表达式和表达式的个数。

如果有多种表达式，输出要求为：自然数个数最少的表达式优先输出，每个表达式中按自然数递增的顺序输出，具体的格式参见样例。

在每个测试数据结束时，输出一行”Result:X”，其中X是最终的表达式个数。

用例
输入	9
输出	
9=9
9=4+5
9=2+3+4
Result:3

说明	
整数 9 有三种表示方法，第1个表达式只有1个自然数，最先输出，

第2个表达式有2个自然数，第2次序输出，

第3个表达式有3个自然数，最后输出。

每个表达式中的自然数都是按递增次序输出的。

数字与符号之间无空格

输入	10
输出	
10=10
10=1+2+3+4
Result:2

说明	无
"""


# todo 滑动窗口
# 如果是求最短的连续整数，可以用数学方法，性能更好, 参考：05-字符串&整数&哈希/数学问题/数的分解.py

import math

# 输入
# 一个目标整数T (1 <=T<= 1000)
T = int(input())

# 输出：该整数的所有表达式和表达式的个数。
# 1.组成连续数之和等于T的最少连续数个数为1，也就是T本身，先加入结果集
ans = [[T]]  # 连续数组列表

# 2.确定滑动窗口边界：连续数组最小值为1， 最大值为math.ceil(T/2)
max_num = math.ceil(T/2) 
lo = 1
hi = 2
sumV = 1 # 记录窗口内连续元素之和
# 注意循环结束条件，是左边界到达最大数
while lo < max_num:  
    if sumV < T:  
        if hi > max_num:
            break
        sumV += hi
        hi += 1
    elif sumV > T: 
        sumV -= lo
        lo += 1
    else: 
        seq = list(range(lo, hi))
        ans.append(seq)
        sumV -= lo
        lo += 1
        
ans.sort(key=lambda x:len(x))
for seq in ans:
    print(f"{T}={'+'.join(map(str, seq))}")
print(f'Result:{len(ans)}')
