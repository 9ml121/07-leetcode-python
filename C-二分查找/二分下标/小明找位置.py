"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134640116

OJ用例
https://hydro.ac/d/HWOD2023/p/OD355/solution

题目描述
小朋友出操，按学号从小到大排成一列；

小明来迟了，请你给小明出个主意，让他尽快找到他应该排的位置。

算法复杂度要求不高于nLog(n)；学号为整数类型，队列规模 ≤ 10000；

输入描述
第一行：输入已排成队列的小朋友的学号（正整数），以","隔开；例如：

93,95,97,100,102,123,155

第二行：小明学号，如：

110

输出描述
输出一个数字，代表队列位置（从1开始）。例如：

6

用例1
输入
93,95,97,100,102,123,155
110
输出
6
"""


# 获取输入
# 第一行：输入已排成队列的小朋友的学号
heights = list(map(int, input().split(',')))
ming = int(input())
# print(heights)


# 二分下标
def main():
    n = len(heights)
    lo = 0
    hi = n-1
    while lo <= hi:
        mid = (lo+hi) >> 1
        if ming > heights[mid]:
            lo = mid+1
        else:
            hi = mid-1

    # 队列位置从1开始
    return lo+1 if lo < n else n


print(main())
