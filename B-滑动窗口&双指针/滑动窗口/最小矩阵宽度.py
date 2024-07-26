"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135230697?spm=1001.2014.3001.5501

OJ用例
题解 - 最小矩阵宽度 - Hydro

题目描述
给定一个矩阵，包含 N * M 个整数，和一个包含 K 个整数的数组。

现在要求在这个矩阵中找一个宽度最小的子矩阵，要求子矩阵包含数组中所有的整数。

输入描述
第一行输入两个正整数 N，M，表示矩阵大小。

接下来 N 行 M 列表示矩阵内容。

下一行包含一个正整数 K。

下一行包含 K 个整数，表示所需包含的数组，K 个整数可能存在重复数字。

所有输入数据小于1000。

输出描述
输出包含一个整数，表示满足要求子矩阵的最小宽度，若找不到，输出-1。

用例1
输入
2 5
1 2 2 3 1
2 3 2 3 2
3
1 2 3
输出
2
说明
矩阵第0、3列包含了1，2，3，矩阵第3，4列包含了1，2，3

用例1
输入
2 5
1 2 2 3 1
1 3 2 3 4
3
1 1 4
输出
5
说明
矩阵第1、2、3、4、5列包含了1、1、4
"""

# todo 考察滑动窗口/尺取法 + 字典
# 我们可以维护一个滑动窗口，从左到右扫描矩阵的每一列，同时记录每个整数的出现次数。
# 当窗口内包含了所有目标整数时，我们可以收缩窗口的左边界，直到不再满足条件

import collections

# 输入
# 第一行输入两个正整数 N，M，表示矩阵大小
R, C = map(int, input().split())
# 接下来 N 行 M 列表示矩阵内容。
grid = [list(map(int, input().split())) for _ in range(R)]
# 下一行包含一个正整数 K。
k = int(input())
# 下一行包含 K 个整数，表示所需包含的数组，K 个整数可能存在重复数字
nums = list(map(int, input().split()))


# 输出：一个整数，表示满足要求子矩阵的最小宽度，若找不到，输出-1
minLen = float('inf')
counter = collections.Counter(nums)

# 双指针
l = 0
# 1.先挪动右窗口，找到包含所有数组的列
for r in range(C):
    for i in range(R):
        num = grid[i][r]
        if num in counter:
            if counter.get(num, 0) > 0:
                k -= 1
            counter[num] -= 1  # 注意：counter里面val可能为负数
    

    # 2.找到数组所有元素之后，再挪动左窗口，确定子矩阵最小宽度
    while k == 0:
        minLen = min(minLen, r - l + 1)
        # print(f'minLen={minLen}')
        for i in range(R):
            num = grid[i][l]
            if num in counter:
                counter[num] += 1
                if counter.get(num, 0) > 0:
                    k += 1
        l += 1
print(minLen if minLen != float('inf') else -1)
