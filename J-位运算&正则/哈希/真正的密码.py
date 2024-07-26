"""
题目描述
在一行中输入一个字符串数组，如果其中一个字符串的所有以索引0开头的子串在数组中都有，那么这个字符串就是潜在密码，

在所有潜在密码中最长的是真正的密码，如果有多个长度相同的真正的密码，那么取字典序最大的为唯一的真正的密码，求唯一的真正的密码。

输入描述
无

输出描述
无

用例
输入	h he hel hell hello o ok n ni nin ninj ninja
输出	ninja
说明
    按要求，hello、ok、ninja都是潜在密码。
    检查长度，hello、ninja是真正的密码。
    检查字典序，ninja是唯一真正密码。

输入	a b c d f
输出	f
说明
    按要求，a b c d f 都是潜在密码。
    检查长度，a b c d f 是真正的密码。
    检查字典序，f是唯一真正密码。
"""

'''
题目解析
我的解题思路如下：
将输入的所有字符串先按照长度升序，如果长度相同，则按照字典序升序。
这样最后一个字符串必然就是长度最长，字典序最大的，我们从最后一个字符串str开始：
接下来，我们不停地截取str的子串，即如下闭区间的子串：
0~str.n-2
0~str.n-3
0~str.n-4
....
0~2
0~1
0~0
然后将在输入的所有字符串中查找每次截取的子串是否存在，如果多存在则返回当str作为题解，如果有一个不存在，则直接中断查找，开始下一个str
'''

# str_list = input().split()
# print(str_list)
str_list = ['h', 'he', 'hel', 'hell', 'hello', 'o', 'ok', 'n', 'ni', 'nin', 'ninj', 'ninja']
# 先按照str长度降序，再按照字典升顺
# str_list = sorted(str_list, key=lambda x: (len(x), x), reverse=True)
# 或者这样写也可以：
str_list = sorted(str_list, key=lambda x: (-len(x), [-ord(c) for c in x]))
print(str_list)


# ['hello', 'ninja', 'hell', 'ninj', 'hel', 'nin', 'he', 'ni', 'ok', 'h', 'n', 'o']

def search(str_list:list):
    hashset = set(str_list)
    for elem in str_list:
        flag = True
        for i in range(1, len(elem)):
            if elem[0:i] not in hashset:
                falg = False
                break
        if flag:
            return elem
    return ''


res = search(str_list)
print(res)
