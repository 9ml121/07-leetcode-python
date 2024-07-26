"""
输入描述：
读入4个[1,10]的整数，数字允许重复，测试用例保证无异常数字。

输出描述：
对于每组案例，输出一行表示能否得到24点，能输出true，不能输出false
"""

# 方法2：递归（推荐）
# 不考虑括号
def helper(arr, item):  # 先写一个利用递归+枚举解决算24的程序
    if item < 1:  # 排除被除数为0，以及负数那种
        return False
    if len(arr) == 1:  # 递归终点，当数组arr只剩一个数的时候，判断是否等于item
        return arr[0] == item
    else:  # 如果arr不是只剩一个数，就调用函数本身（直到只剩一个为止返回真假）
        for i in range(len(arr)):
            m = arr[0:i] + arr[i + 1:]
            n = arr[i]
            if helper(m, item + n) or helper(m, item - n) or helper(m, item * n) or helper(m, item / n):
                return True
        return False


while True:
    try:
        if helper(list(map(int, input().split())), 24):
            print('true')
        else:
            print('false')
    except:
        break

"""
# 方法1：暴力枚举，要用到itertools函数
复杂度分析
时间复杂度：O(1)
    对于该方法中的4个数字来说，首先排列组合的操作次数为4×3×2×1=24
    对于构造前两个数字的运算操作的lst4数组来说，新的操作次数累计为24×4=96
    对于构造前三个数字的运算操作的lst16数组来说，新的操作累计数量为96×4=384
    对于构造四个数字运算操作的lst64数组来说，新的操作累计数量为384×4=1536
    以上对于每项的计算都是O(1)级别，因此总复杂度为O(1)
空间复杂度：O(1)
常数级别的空间开销
"""

import itertools


def method2():
    ops = ["+", "-", "*", "/"]

    def cal(a, b, i):
        if i == 0:
            return a + b
        elif i == 1:
            return a - b
        elif i == 2:
            return a * b
        elif i == 3:
            if b != 0:
                return a / b
            else:
                return 0

    nums = map(int, input().split())
    lst = list(itertools.permutations(nums, 4))
    n = len(lst)  # 24

    def check(lst):
        for elem in lst:
            a, b, c, d = elem
            for i in range(4):
                ab = cal(a, b, i)
                for j in range(4):
                    abc = cal(ab, c, j)
                    cd = cal(c, d, j)
                    for k in range(4):
                        abcd = cal(abc, d, k)
                        abcd2 = cal(ab, cd, k)
                        if abcd == 24 or abcd2 == 24:
                            return True
        return False

    if check(lst):
        print('true')
    else:
        print("false")
