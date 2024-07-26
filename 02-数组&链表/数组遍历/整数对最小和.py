"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127969628

题目描述
给定两个整数数组array1、array2，数组元素按升序排列。

假设从array1、array2中分别取出一个元素可构成一对元素，现在需要取出k对元素，

并对取出的所有元素求和，计算和的最小值。

注意：

两对元素如果对应于array1、array2中的两个下标均相同，则视为同一对元素。

输入描述
输入两行数组array1、array2，每行首个数字为数组大小size(0 < size <= 100);

0 < array1[i] <= 1000

0 < array2[i] <= 1000

接下来一行为正整数k

0 < k <= array1.size() * array2.size()

输出描述
满足要求的最小和

用例1
输入
3 1 1 2
3 1 2 3
2
输出
4
说明
用例中，需要取2对元素

取第一个数组第0个元素与第二个数组第0个元素组成1对元素[1,1];

取第一个数组第1个元素与第二个数组第0个元素组成1对元素[1,1];

求和为1+1+1+1=4，为满足要求的最小和。
"""
line1 = list(map(int, input().split()))
line2 = list(map(int, input().split()))
k = int(input())
n1 = line1[0]
arr1 = line1[1:]
n2 = line2[0]
arr2 = line2[1:]

# 方法1:排序+暴力枚举
def solution1():
    res = []
    for i in range(n1):
        for j in range(n2):
            tmp = arr1[i] + arr2[j]
            res.append(tmp)

    res.sort()
    ans = 0
    for i in range(k):
        ans += res[i]
    print(ans)


    