"""
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在 1≤n≤2^31−1
输入描述：
输入一个十六进制的数值字符串。
0xAA

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
170
"""

# 解法1：直接用int函数
# while 1:
#     try:
#         s = input()
#         print(int(s, 16))
#     except:
#         break

# 解法2：运用字典
nums = list(range(16))
keys = [str(i) for i in range(10)] + [i for i in 'ABCDEF']
# print(nums)
# print(keys)
d = dict(zip(keys, nums))
# print(d)
# {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

res = 0
s = input()[2:]  # 'FF'
for i, v in enumerate(reversed(s)):
    res += d[v] * (16 ** i)

print(res)
