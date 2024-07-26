"""
描述
计算24点是一种扑克牌益智游戏，随机抽出4张扑克牌，通过加(+)，减(-)，乘(*), 除(/)四种运算法则计算得到整数24，
本问题中，扑克牌通过如下字符或者字符串表示，其中，小写joker表示小王，大写JOKER表示大王：

3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER

本程序要求实现：输入4张牌，输出一个算式，算式的结果为24点。

详细说明：

1.运算只考虑加减乘除运算，没有阶乘等特殊运算符号，没有括号，友情提醒，整数除法要当心，是属于整除，比如2/3=0，3/2=1；
2.牌面2~10对应的权值为2~10, J、Q、K、A权值分别为为11、12、13、1；
3.输入4张牌为字符串形式，以一个空格隔开，首尾无空格；如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算；
4.输出的算式格式为4张牌通过+-*/四个运算符相连，中间无空格，4张牌出现顺序任意，只要结果正确；
5.输出算式的运算顺序从左至右，不包含括号，如1+2+3*4的结果为24，2 A 9 A不能变为(2+1)*(9-1)=24
6.如果存在多种算式都能计算得出24，只需输出一种即可，如果无法得出24，则输出“NONE”表示无解。
7.因为都是扑克牌，不存在单个牌为0的情况，且没有括号运算，除数(即分母)的数字不可能为0

数据范围：一行由4张牌组成的字符串
输入描述：
输入4张牌为字符串形式，以一个空格隔开，首尾无空格；

输出描述：
输出怎么运算得到24，如果无法得出24，则输出“NONE”表示无解，如果输入的4张牌中包含大小王，则输出字符串“ERROR”，表示无法运算

示例1
输入：
A A A A

输出：
NONE

说明：
不能实现

示例2
输入：
4 2 K A

输出：
K-A*4/2

说明：
 A+K*2-4也是一种答案，输出任意一种即可

示例3
输入：
B 5 joker 4

输出：
ERROR

说明：
 存在joker，输出ERROR

示例4
输入：
K Q 6 K

输出：
NONE

说明：
按一般的计算规则来看，K+K-(Q/6)=24 或 K-((Q/6)-K)=24，但是因为这个题目的运算不许有括号，
所以去掉括号后变为 K+K-Q/6=26-Q/6=14/6=2 或 K-Q/6-K=1/6-K=0-K=-13，
其它情况也不能运算出24点，故不存在，输出NONE
"""
# 1.准备数据映射字典和操作列表
import itertools

d = {
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 1,
    "2": 2,
}

ops = ["+", "-", "*", "/"]


# 2. 准备运算结果函数f
# 参数k1,k2为计算的牌数值，op为操作符索引，返回计算结果
def f(n1: int, n2: int, op: int):
    # n1, n2 = d[k1], d[k2]
    # n = 0
    if op == 0:
        n = n1 + n2
    elif op == 1:
        n = n1 - n2
    elif op == 2:
        n = n1 * n2
    elif op == 3:
        n = n1 // n2
    return n


# 方法1:用到itertools.permutations函数
lst = input().split()


def loop():
    if "joker" in lst or "JOKER" in lst:
        print("ERROR")
    else:
        num_orders = itertools.permutations(lst, 4)
        # 运算结果res
        res = 0
        for nums in num_orders:
            k1, k2, k3, k4 = nums
            n1, n2, n3, n4 = d[k1], d[k2], d[k3], d[k4]
            for i in range(4):
                a = f(n1, n2, i)
                for j in range(4):
                    b = f(a, n3, j)
                    for k in range(4):
                        res = f(b, n4, k)
                        if res == 24:
                            exprs = k1 + ops[i] + k2 + ops[j] + k3 + ops[k] + k4
                            print(exprs)
                            return

    # 如果无法得出24，则输出“NONE”表示无解
    print("NONE")


loop()

"""
方法2：不用itertools函数，递归解决
"""


def method2():
    d = {'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
         '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 1, '2': 2}

    def f(nums, target):
        if len(nums) == 1:
            if d[nums[0]] == target:
                res.append(nums[0])
                return True
            else:
                return False
        for i in range(len(nums)):
            a = nums[i]
            b = nums[:i] + nums[i + 1:]
            if f(b, target + d[a]):
                res.append('-' + a)
                return True
            elif f(b, target - d[a]):
                res.append('+' + a)
                return True
            elif f(b, target * d[a]):
                res.append('/' + a)
                return True
            elif target % d[a] == 0 and f(b, target // d[a]):
                res.append('*' + a)
                return True
        return False

    while True:
        try:
            nums = input().strip()
            if 'joker' in nums or 'JOKER' in nums:
                print('ERROR')
            else:
                nums = nums.split()
                res = []
                if f(nums, 24):
                    print(''.join(res))
                else:
                    print('NONE')
        except:
            break
