"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134746490?spm=1001.2014.3001.5502

OJ用例
题解 - CPU算力分配 - Hydro

题目描述
现有两组服务器A和B，每组有多个算力不同的CPU，其中 A[i] 是 A 组第 i 个CPU的运算能力，B[i] 是 B组 第 i 个CPU的运算能力。

一组服务器的总算力是各CPU的算力之和。

为了让两组服务器的算力相等，允许从每组各选出一个CPU进行一次交换，

求两组服务器中，用于交换的CPU的算力，并且要求从A组服务器中选出的CPU，算力尽可能小。

输入描述
第一行输入为L1和L2，以空格分隔，L1表示A组服务器中的CPU数量，L2表示B组服务器中的CPU数量。
第二行输入为A组服务器中各个CPU的算力值，以空格分隔。
第三行输入为B组服务器中各个CPU的算力值，以空格分隔。
1 ≤ L1 ≤ 10000
1 ≤ L2 ≤ 10000
1 ≤ A[i] ≤ 100000
1 ≤ B[i] ≤ 100000


输出描述
对于每组测试数据，输出两个整数，以空格分隔，依次表示A组选出的CPU算力，B组选出的CPU算力。

要求从A组选出的CPU的算力尽可能小。

备注
保证两组服务器的初始总算力不同。
答案肯定存在
用例1
输入
2 2
1 1
2 2
输出
1 2
说明
从A组中选出算力为1的CPU，与B组中算力为2的进行交换，使两组服务器的算力都等于3。

用例2
输入
2 2
1 2
2 3
输出
1 2

用例3
输入
1 2
2
1 3
输出
2 3

用例4
输入
3 2
1 2 5
2 4
输出
5 4
"""

# 输入
# n1表示A组服务器中的CPU数量，n2表示B组服务器中的CPU数量
n1, n2 = map(int, input().split())
# A组服务器中各个CPU的算力值
nums1 = list(map(int, input().split()))
# B组服务器中各个CPU的算力值
nums2 = list(map(int, input().split()))

# 输出：要求从A组选出的CPU的算力尽可能小，使两组算力总和相等
# 1.计算
total1 = sum(nums1)
total2 = sum(nums2)
avg = (total1 + total2)//2

# todo 将nums1排序，
nums2_set = set(nums2)
nums1.sort()
for num in nums1:
    x = avg - (total1 - num)
    if x in nums2:
        print(f'{num} {x}')
        break
