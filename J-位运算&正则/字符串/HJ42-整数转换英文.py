"""
输入描述：
输入一个long型整数

输出描述：
输出相应的英文写法

# 数据范围：1≤n≤2000000
# 关键字提示：and，billion，million，thousand，hundred。

# 1,652,510:  one million six hundred and fifty two thousand five hundred and ten
# 486,669:  four hundred and eighty six thousand six hundred and sixty nine
# 8,088:  eight thousand (and) eighty eight
# 22: twenty two
# 100:  one hundred
# 145:  one hundred and forty five
"""


# n最多3位整数
def spell(n: int):
    if 0 <= n <= 19:
        s = NUMBER_CONSTANT[n]
        return s
    elif 20 <= n <= 99:
        ten = n // 10
        one = n % 10
        if one == 0:  # 20 30 ..
            s = IN_HUNDRED_CONSTANT[ten]
        else:  # 21
            s = IN_HUNDRED_CONSTANT[ten] + ' ' + NUMBER_CONSTANT[one]
        return s
    elif 100 <= n <= 999:
        hundred = n // 100
        ten = n - (hundred * 100)
        one = n % 10
        # 200 510
        if ten == 0 and one == 0:
            s = NUMBER_CONSTANT[hundred] + ' hundred'
        # 201 214
        elif 0 <= ten <= 19:
            s = NUMBER_CONSTANT[hundred] + ' hundred and ' + NUMBER_CONSTANT[ten]
        # 220 240
        elif 20 <= ten and one == 0:
            s = NUMBER_CONSTANT[hundred] + ' hundred and ' + IN_HUNDRED_CONSTANT[ten // 10]
        # 221 223
        else:
            s = NUMBER_CONSTANT[hundred] + ' hundred and ' + IN_HUNDRED_CONSTANT[ten // 10] + " " + NUMBER_CONSTANT[one]

        return s


NUMBER_CONSTANT = {0: "", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
                   9: "nine",
                   10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
                   17: "seventeen", 18: "eighteen", 19: "nineteen"}
IN_HUNDRED_CONSTANT = {0: "", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty",
                       9: "ninety"}

# keys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,30,40,50,60,70,80,90]
# values = ['one','two','three','four','five','six','seven','eight','nine','ten',
# 'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
# dic = dict(zip(keys, values))

n = 1652510
# n = int(input())
# 最后结果
l = []
# format(n, ',')
million = n // (1000 ** 2)
if million > 0:
    n -= million * (1000 ** 2)
    l.append(spell(million) + ' million')
thousand = n // 1000
if thousand > 0:
    n -= thousand * 1000
    l.append(spell(thousand) + ' thousand')

l.append(spell(n))

print(' '.join(l))
