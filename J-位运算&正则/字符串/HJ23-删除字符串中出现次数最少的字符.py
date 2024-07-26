"""
描述
实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。

数据范围：输入的字符串长度满足 1≤n≤20  ，保证输入的字符串中仅出现小写字母
输入描述：
字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

输出描述：
删除字符串中出现次数最少的字符后的字符串。

输入：
aabcddd

输出：
aaddd
"""

# s = input()
s = 'aabcddd'
dic = {}
for elem in s:
    if elem not in dic:
        dic[elem] = 1
    else:
        dic[elem] += 1
# print(dic)
# {'a': 2, 'b': 1, 'c': 1, 'd': 3}
min_num = min(dic.values())
res = ''
for elem in s:
    if dic[elem] > min_num:
        res += elem
print(res)