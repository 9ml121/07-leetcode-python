"""
题目解析和算法源码
华为OD机试 - 掌握的单词个数（Java & JS & Python & C）-CSDN博客

题目描述
有一个字符串数组 words 和一个字符串 chars。

假如可以用 chars 中的字母拼写出 words 中的某个“单词”（字符串），那么我们就认为你掌握了这个单词。

words 的字符仅由 a-z 英文小写字母组成，例如 "abc"

chars 由 a-z 英文小写字母和 "?" 组成。其中英文 "?" 表示万能字符，能够在拼写时当作任意一个英文字母。例如："?" 可以当作 "a" 等字母。

注意：每次拼写时，chars 中的每个字母和万能字符都只能使用一次。

输出词汇表 words 中你掌握的所有单词的个数。没有掌握任何单词，则输出0。

输入描述
第一行：输入数组 words 的个数，记作N。

第二行 ~ 第N+1行：依次输入数组words的每个字符串元素

第N+2行：输入字符串chars

输出描述
输出一个整数，表示词汇表 words 中你掌握的单词个数

备注
1 ≤ words.length ≤ 100
1 ≤ words[i].length, chars.length ≤ 100
所有字符串中都仅包含小写英文字母、英文问号
用例1
输入
4
cat
bt
hat
tree
atach??
输出
3
说明
可以拼写字符串"cat"、"bt"和"hat"

用例2
输入
3
hello
world
cloud
welldonehohneyr
输出
2
说明
可以拼写字符串"hello"和"world"

用例3
输入
3
apple
car
window
welldoneapplec?
输出
2
说明
可以拼写字符串"apple"和“car”
"""
import collections

n = int(input())
words = []
for i in range(n):
    words.append(input())
chrs = input()

chrs_cnt = collections.Counter(chrs)
ans = 0
for word in words:
    cnts = chrs_cnt.copy()
    flag = True
    for c in word:
        if cnts.get(c, 0) > 0:
            cnts[c] -= 1
        elif cnts.get('?', 0) > 0:
            cnts['?'] -= 1
        else:
            flag = False
            break
    if flag:
        ans += 1

print(ans)
