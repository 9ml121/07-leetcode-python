"""
描述
输入一个只包含小写英文字母和数字的字符串，按照不同字符统计个数由多到少输出统计结果，如果统计的个数相同，则按照ASCII码由小到大排序输出。
数据范围：字符串长度满足 1≤len(str)≤1000

输入描述：
一个只包含小写英文字母和数字的字符串。
aaddccdc

输出描述：
一个字符串，为不同字母出现次数的降序表示。若出现次数相同，则按ASCII码的升序输出。
cda

说明：
样例里，c和d出现3次，a出现2次，但c的ASCII码比d小，所以先输出c，再输出d，最后输出a.
"""


# method1: 字典去重和计数
def method1():
    s = input()
    dic = {}
    for i in s:
        # 1。字典get函数统计字符串每个字符出现个数
        dic[i] = dic.get(i, 0) + 1
    # 2。注意这里lambda函数用法，要按照2个值要求排序
    print("".join(i for i in sorted(dic, key=lambda x: [-dic[x], x])))


# method2:set去重，字符串count函数计数
def method2():
    s = input()
    ss = sorted(list(set(s)), key=lambda x: s.count(x) * 1000 - ord(x), reverse=True)
    print("".join(ss))


# method3：冒泡排序解法
def method3():
    s = input()
    d = {}
    for elem in s:
        # if elem.isalpha():
        if elem not in d.keys():
            d[elem] = 1
        else:
            d[elem] += 1

    keys = list(d.keys())
    for i in range(len(keys) - 1):
        for j in range(len(keys) - i - 1):
            # 为不同字母出现次数的降序表示
            if d[keys[j]] < d[keys[j + 1]]:
                keys[j], keys[j + 1] = keys[j + 1], keys[j]
            # 若出现次数相同，则按ASCII码的升序输出。
            elif d[keys[j]] == d[keys[j + 1]]:
                if keys[j] > keys[j + 1]:
                    keys[j], keys[j + 1] = keys[j + 1], keys[j]

    print(''.join(keys))
