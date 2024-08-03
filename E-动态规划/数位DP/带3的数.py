"""
题目来源
https://blog.csdn.net/qfc_128220/article/details/128128007

题目描述
求区间[L,R]范围内有多少带3的数。
所谓带3的数就是这个数的十进制表示中存在至少一位为3。
比如3, 123, 3333,都是带3的数，如12, 456, 1000都是不带3的数

输入描述
输入一行包含两个整数 L,R（1 ≤ L ≤ R ≤ 10^12）。

输出描述
输出一个整数，表示区间[L,R]范围内带3的数的个数。

用例
输入	100 200
输出	19

说明
103
113
123
130、131、132、133、134、135、136、137、138、139
143
153
163
173
183
193

共19个

题目解析
本题最容易想到的思路就是暴力枚举，从L枚举到R，统计其中含有3的枚举数。但是这种方式是O(n)时间复杂度，对于数量级1 ≤ L ≤ R ≤ 10^12来说，肯定会超时。
"""
from functools import cache
import math

# 输入
L, R = map(int, input().split())

# 输出：求区间[L,R]范围内有多少带3的数。
"""
方法2：逆向思维：我们可以发现统计带3的数的个数的逻辑有些复杂，因此我们可以转换思维，统计不带3的数的个数，
之后用总数 - 不带3的数的个数 = 带3的数的个数
"""

def main(num:int):
    # todo 数位搜索标准模板
    @cache
    def dfs(s: str, i: int = 0, is_limit: bool = True):
        if i == len(s):
            return 1  # 能走到最后的肯定是不带3的数，因此算统计到1个带3的数，返回1个

        up = int(s[i]) if is_limit else 9
        res = 0

        for d in range(up + 1):
            #  只统计不带3的数的个数
            if d != 3:
                res += dfs(s, i + 1, is_limit and d == up)

        return res

    # 总数 - 不带3数的个数 = 带3数的个数
    ans = num + 1 - dfs(str(num))
    return ans


# print(main(135))
print(main(R) - main(L - 1))


'''
方法1：暴力枚举：超时
'''
def digitSearch(num):
    l, r = map(int, input().split())
    cnt = 0
    for i in range(l, r + 1):
        if '3' in str(i):
            cnt += 1
    return cnt


'''
前置知识点：数位搜索/数位枚举：234以内的所有正整数
第0位（百位）可选数为：0,1,2
第1位（十位）可选数取决于第0位
第2位 (个位）可选数取决于第1位
'''
def digitSearch2(num):
    # 全局变量
    res = []
    # 把num按照位数拆解为整数列表：2 3 4
    s = list(map(int, str(num)))

    def dfs(level: int, limit: bool, path: list) -> list:
        """
        level:表示数字的第几位
        limit:表示上一位对当前位是否有限制
        s:数字按照位数拆分成的整数列表
        path:表示每条递归线最终返回的结果
        返回res:234以内所有正整数集合列表
        """
        # 根节点（递归出口）
        if level == len(s):
            res.append(''.join(map(str, path)))
            return res

        # 如果是约束范围，即limit为true，则当前位只能取0~str[level]，如果不是约束范围，则当前可以取0~9
        maxV = s[level] if limit else 9

        for i in range(0, maxV + 1):  # 0 1 2
            path.append(i)
            # 判断下一位取值是否为约束范围：当前位取值为约束范围，即limit为true，且当前位取值为max
            dfs(level + 1, limit and i == maxV, path)
            # 回溯，把path结果清空
            path.pop()

        return res

    res = dfs(0, True, [])  # 2 3 4
    print(res)


'''
方法1：正向思维：数位dp查找135内所有带3的数的个数
'''
def digitSearch3(num):
    @cache
    def dfs(s:str, level=0, limit=True):
        if level == len(s):
            return 0

        maxV = int(s[level]) if limit else 9
        count = 0

        for i in range(maxV + 1):
            # 枚举到3，则后面位就不需要枚举了，必然含3
            if i == 3:
                # 统计含3数的个数
                if limit and i == maxV:  # 如果当前枚举3是上界值
                    count += int("".join(s[level + 1:])) + 1  # 从0计数，因此要加1
                else:
                    count += int(math.pow(10, len(s) - level - 1))
            else:
                count += dfs(s, level + 1, limit and i == maxV)

        return count

    count = dfs(str(num))
    print(count)


# digitSearch3(135)



'''
记忆化搜索写法：新增了三行关于f数组记忆化搜索的代码
'''
def digitSearch5(num):
    def dfs(level, limit, s, f):
        if level == len(s):
            return 1

        if not limit and f[level] is not None:  # 记忆化搜索
            return f[level]

        maxV = int(s[level]) if limit else 9
        count = 0

        for i in range(maxV + 1):
            if i != 3:
                count += dfs(level + 1, limit and i == maxV, s, f)

        if not limit:  # 记忆化
            f[level] = count

        return count

    s = str(num)
    f = [None] * len(s)  # f[i]表示第i位不含3的数的个数
    count = num + 1 - dfs(0, True, s, f)
    print(count)


# digitSearch5(135)

'''
题目最终答案
最后，找L，R范围内的含3数的个数，即先找0~L-1范围内的含3数个数count1，再找0~R范围内的含3数的个数count2，然后用count2 - count1作为题解。
'''


# 数位搜索 + 记忆化存储
def dfs(level, limit, s, f):
    if level == len(s):
        return 1

    # todo: 当前数位没有上限限制，才能重复路径，可以用memo, 否则不能用memo
    if not limit and f[level] is not None:  # 记忆化搜索
        return f[level]

    maxV = int(s[level]) if limit else 9
    count = 0

    for i in range(maxV + 1):
        if i != 3:
            count += dfs(level + 1, limit and i == maxV, s, f)

    if not limit:  # 记忆化
        f[level] = count

    return count


# 算法入口
def digitSearch6(num):
    s = str(num)
    f = [None] * len(s)  # f[i]表示第i位不含3的数的个数
    return num + 1 - dfs(0, True, s, f)


