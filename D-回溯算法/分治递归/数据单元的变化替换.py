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
输入：<B<12,1
输出：-1
说明
第一个单元中有错误的单元格引用方式， 输出-1


用例6
输入
01<D>23<B>45<C>6,B,C,D
输出
01D23B45C6,B,C,D

用例7
输入
0,1<B>,2<C>,3<D>,4,5
输出
-1

用例8
输入
0,1,2<AB>,3,4,5
输出
-1

用例12
输入
0,1,2<A>>,3,4,5
输出
-1

用例13
输入
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30
输出
-1

用例14
输入
0,1,2$,3,4,5
输出
-1

用例15
输入
<B>,<C>,<D>,<E>,<F>,<G>,<H>,<I>,<J>,<K>,<L>,<M>,<N>,<O>,<P>,<Q>,<R>,<S>,<T>,<U>,<V>,<W>,<X>,<Y>,Z0123456789Z0123456789Z0123456789Z0123456789Z0123456789Z0123456789Z0123456789Z0123456789Z0123456789Z0123456789
输出
-1

"""

# todo 考察递归算法 + 正则查找（非贪婪模式）
import re

# 输入：用逗号分隔每个单元格
cells = input().split(',')

# 输出：替换后的结果


def check_and_replace(idx) -> bool:
    # todo 正则(.*?)表示非贪婪模式。比如<A><B>,能够匹配出['A', 'B'], 而不是['A><B']
    p = re.compile(r'<(.*?)>')
    # p = re.compile(r'<(.*)>')
    # print(p.findall('<A><B>'))
    
    refs = p.findall(cells[idx])

    # ref 记录引用单元格编号
    for ref in refs:
        # 引用内容长度只能是1
        if len(ref) > 1:  # 2<AB>
            return False

        # 引用内容只能是A~Z字母，且不能超出输入单元格数量
        new_idx = ord(ref) - ord('A')
        if new_idx < 0 or new_idx >= len(cells):  # 0,1,2<Z>
            return False

        # 不能自引用
        if new_idx == idx:
            return False
        
        # todo 递归
        if not check_and_replace(new_idx):
            return False
        
        # 将单元格内容中的引用部分，替换为被引用的单元格的内容
        cells[idx] = cells[idx].replace(f'<{ref}>', cells[new_idx])

    return True


def main():
    if len(cells) > 26:
        # 最多26个单元格，对应编号A~Z
        return -1
    
    for i in range(len(cells)):
        # 替换单元格中的引用
        if not check_and_replace(i):
            return -1
    
        if len(cells[i]) > 100:
            # 每个单元格的内容，在替换前和替换后均不超过100个字符
            return -1
    
        if not re.match(r"^[a-zA-Z0-9]+$", cells[i]):
            # 每个单元格的内容包含字母和数字
            return "-1"

    return ','.join(cells)

print(main())

# print(ord('A'))
# print(chr(65))

        

