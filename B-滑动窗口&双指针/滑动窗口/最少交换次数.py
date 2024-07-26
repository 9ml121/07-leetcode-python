"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127418208

题目描述
给出数字K,请输出所有结果小于K的整数组合到一起的最少交换次数。

组合一起是指满足条件的数字相邻，不要求相邻后在数组中的位置。

数据范围：

-100 <= K <= 100
-100 <= 数组中数值 <= 100
输入描述
第一行输入数组：1 3 1 4 0
第二行输入K数值：2

输出描述
第一行输出最少交换次数：1

用例1
输入
1 3 1 4 0
2
输出
1
说明
小于2的表达式是1 1 0, 共三种可能将所有符合要求数字组合一起，最少交换1次。
"""

# todo 考察滑动窗口，类似：A-滑动窗口&双指针\滑动窗口\1151.最少交换次数来组合所有的1.py

# 输入
arr = list(map(int, input().split()))
# 窗口内数字小于k
k = int(input())

# 输出：最少交换次数
# 先统计arr中所有小于k的数字个数sz，也是滑动窗口大小
window_sz = len([x for x in arr if x < k])

# 第一个窗口
# cur统计每个窗口内小于k的元素个数
cur = 0 
for i in range(window_sz):
    if arr[i] < k:
        cur += 1
# max_cnt 统计所有窗口小于k的元素个数 的最大值
max_cnt = cur 

# 后续窗口
for i in range(window_sz, len(arr)):
    if arr[i] < k:
        cur += 1
    if arr[i-window_sz] < k:
        cur -= 1
    max_cnt = max(max_cnt, cur)

# 4.计算最少交换次数，也就是所有窗口内大于等于k的个数的最小值
ans = window_sz - max_cnt
print(ans)
