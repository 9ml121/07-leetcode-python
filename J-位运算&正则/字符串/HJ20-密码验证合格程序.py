"""
描述
密码要求:
1.长度超过8位
2.包括大小写字母.数字.其它符号,以上四种至少三种
3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）

数据范围：输入的字符串长度满足 1≤n≤100

输入描述：
一组字符串。

输出描述：
如果符合要求输出：OK，否则输出NG

输入：
021Abc9000
021Abc9Abc1
021ABC9000
021$bc9000

输出：
OK
NG
NG
OK
"""


def check(s: str):
    # 1.长度超过8位
    if len(s) <= 8:
        return False
    # 2.包括大小写字母.数字.其它符号, 以上四种至少三种
    # upper = 0
    # lower = 0
    # num = 0
    # other = 0
    # for elem in s:
    #     if elem.isupper():
    #         upper = 1
    #     elif elem.islower():
    #         lower = 1
    #     elif elem.isdigit():
    #         num = 1
    #     else:
    #         other = 1
    # if upper + lower + num + other < 3:
    #     return False

    # 3.不能有长度大于2的包含公共元素的子串重复 （注：其他符号不含空格或换行）
    # 021Abc9Abc1, 这一步可以用数组滑动窗口，或者用字符串split函数，或者count函数解决！！！
    # 注意：这里range(len(s) - 2)这个范围可以有变化，最小为len(s)-5
    # for i in range(len(s) - 2):
    #     sub = s[i:i + 3]
    #     if sub in s[i + 3:]:
    #         return False

    # 2和3有另外的判断方法，如下
    # 2判断方法2：用ord函数
    a, b, c, d = 0, 0, 0, 0
    for item in s:
        if ord('a') <= ord(item) <= ord('z'):
            a = 1
        elif ord('A') <= ord(item) <= ord('Z'):
            b = 1
        elif ord('0') <= ord(item) <= ord('9'):
            c = 1
        else:
            d = 1
    if a + b + c + d < 3:
        return 0
    # 3的判断方法2:用字符串split或者count函数都可以
    # for i in range(len(s) - 3):
    #     #
    #     if len(s.split(s[i:i + 3])) >= 3:
    #         return 0
    # 3的判断方法3：哈希，时间复杂度最小
    dc = {}
    for i in range(len(s) - 2):  # 遍历所有的子字符串起点
        if s[i:i + 3] in dc:  # 在字典中搜索
            return False
        else:  # 如果未曾经出现过则加入字典中，等待之后的判定
            dc[s[i:i + 3]] = 1

    return True


while True:
    try:
        s = input()
        if check(s):
            print('OK')
        else:
            print('NG')
    except:
        break
