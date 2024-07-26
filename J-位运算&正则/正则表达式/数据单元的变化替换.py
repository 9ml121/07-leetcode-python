"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134939544?spm=1001.2014.3001.5502

题目描述
将一个 csv 格式的数据文件中包含有单元格引用的内容替换为对应单元格内容的实际值。

comma separated values(CSV) 逗号分隔值，csv 格式的数据文件使用逗号 "," 作为分隔符将各单元的内容进行分隔。

输入描述
输入只有一行数据，用逗号分隔每个单元格，行尾没有逗号。最多26个单元格，对应编号A~Z。

每个单元格的内容包含字母和数字，以及使用 '<>' 分隔的单元格引用，例如：<A>表示引用第一个单元的值。

每个单元格的内容，在替换前和替换后均不超过100个字符。

引用单元格的位置不受限制，允许排在后面的单元格被排在前面的单元格引用。

不存在循环引用的情况，比如下面这种场景是不存在的：

A单元恪：aCd<B>8U

B单元格：KAy<A>uZq0

不存在多重 '<>' 的情况，一个单元只能引用一个其他单元格。比如下面这种场景是不存在的：

A单元格：aCdOu

B单元格：kAydzco

C单元格：y<<A><B>>d

输出描述
输出替换后的结果

用例1
输入
1,2<A>00
输出
1,2100
说明
第二个单元中有对A单元的引用，A单元格的值为1，替换时，将A单元的内容替代<A>的位置，并和其他内容合并。

用例2
输入
1<B>2,1
输出
112,1
说明
第一个单元中有对B单元的引用，B单元格的值为1，耆换时，将第二个数据第单元的内容替代<B>的位置，并和其他内容合并

用例3
输入
<A>
输出
-1
说明
第一个单元中有错误的单元格引用方式，输出字符串"-1"表示错误
"""

import re

# 考察递归算法
# 1<B><C>2
def dfs(idx, vis)->bool:
    refs = p.findall(cells[idx])
    if not refs:
        return True

    vis[idx] = True
    for ref in refs:
        # 内容长度只能是1
        if len(ref) > 1:  # 2<AB>
            return False

        # 内容只能是A~Z字母=>0~26
        # 内容的单个字母对应的索引，不能超出输入单元格数量
        new_idx = ord(ref) - ord('A')
        if new_idx < 0 or new_idx >= n:  # 0,1,2<Z>
            return False

        # 循环引用
        if vis[new_idx]:
            return False

        if dfs(new_idx, vis):
            cells[idx] = cells[idx].replace(f'<{ref}>', cells[new_idx])

    return True


def solution():
    for i in range(n):
        vis = [False] * n
        if not dfs(i, vis):
            return -1
    return ','.join(cells)


# 获取输入
cells = input().split(',')
n = len(cells)
# print(ord('A'))
# print(chr(65))
# todo 正则(.*?)表示非贪婪模式。比如<A><B>,能够匹配出['A', 'B'], 而不是['A><B']
p = re.compile(r'<(.*?)>')
# p = re.compile(r'<(.*)>')
# print(p.findall('<A><B>'))

print(solution())
