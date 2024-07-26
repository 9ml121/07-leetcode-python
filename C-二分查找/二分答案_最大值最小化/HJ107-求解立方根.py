"""
描述
计算一个浮点数的立方根，不使用库函数。
保留一位小数。

数据范围：
∣value∣≤20

输入描述：
待求解参数，为double类型（一个实数）

输出描述：
输出参数的立方根。保留一位小数。

示例1
输入：
19.9

输出：
2.7

示例2
输入：
2.7

输出：
1.4
"""

'''
方法1；B-二分查找，考虑负数和val < 1
'''


# 返回浮点数val(∣value∣≤20)的立方根
def getResult(val: float) -> str:
    sign = ""
    # 判断符号,统一转为正数
    if val < 0:
        sign = "-"
        val = abs(val)
    # 判断特殊情况
    if val == 1.0 or val == 0.0:
        return sign + str(val)

    lo, hi = 1, 1
    # value < 1.0 和 value > 1.0的边界
    if val < 1.0:
        lo = val
    else:
        hi = val
    mid = lo + (hi - lo) / 2
    while abs(mid ** 3 - val) > 0.001:
        if mid > val / mid / mid:
            hi = mid
        elif mid ** 3 < val:
            lo = mid
        mid = lo + (hi - lo) / 2

    return sign + str(round(mid, 1))


if __name__ == '__main__':
    val = float(input())
    print(getResult(val))
