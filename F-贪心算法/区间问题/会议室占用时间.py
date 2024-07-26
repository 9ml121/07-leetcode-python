"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134939442?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22134939442%22%2C%22source%22%3A%22qfc_128220%22%7D

OJ用例
题解 - 会议室占用时间 - Hydro

题目描述
现有若干个会议，所有会议共享一个会议室，用数组表示各个会议的开始时间和结束时间，格式为：

[[会议1开始时间, 会议1结束时间], [会议2开始时间, 会议2结束时间]]

请计算会议室占用时间段。

输入描述
第一行输入一个整数 n，表示会议数量

之后输入n行，每行两个整数，以空格分隔，分别表示会议开始时间，会议结束时间

输出描述
输出多行，每个两个整数，以空格分隔，分别表示会议室占用时间段开始和结束

备注
会议室个数范围：[1, 100]
会议室时间段：[1, 24]
用例1
输入
4
1 4
2 5
7 9
14 18
输出
1 5
7 9
14 18
说明
输入：[[1,4],[2,5],[7,9],[14,18]]

输出：[[1,5],[7,9],[14,18]]

说明：时间段[1,4]和[2,5]重叠，合并为[1,5]
"""

# 输入
# 第一行输入一个整数 n，表示会议数量
n = int(input())
# 之后输入n行，每行两个整数，以空格分隔，分别表示会议开始时间，会议结束时间
rans = []
for _ in range(n):
    rans.append(list(map(int, input().split())))
# 按照开始时间排序
rans.sort(key=lambda x: x[0])
# print(rans)

res = []
pre_start, pre_end = rans[0]
for i in range(1, n):
    start, end = rans[i]

    if start <= pre_end:
        pre_end = max(pre_end, end)
    else:
        res.append([pre_start, pre_end])
        pre_start, pre_end = start, end

res.append([pre_start, pre_end])
for start, end in res:
    print(f'{start} {end}')
