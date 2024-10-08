"""
有一个正整数数组 arr，现给你一个对应的查询数组 queries，其中 queries[i] = [Li, Ri]。

对于每个查询 i，请你计算从 Li 到 Ri 的 XOR 值（即 arr[Li] xor arr[Li+1] xor ... xor arr[Ri]）作为本次查询的结果。

并返回一个包含给定查询 queries 所有结果的数组。

 

示例 1：

输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
输出：[2,7,14,8] 
解释：
数组中元素的二进制表示形式是：
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
查询的 XOR 值为：
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8
示例 2：

输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
输出：[8,0,4,4]
 

提示：

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 10^9
1 <= queries.length <= 3 * 10^4
queries[i].length == 2
0 <= queries[i][0] <= queries[i][1] < arr.length
"""
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # todo 二进制异或操作， 前缀和
        n = len(arr)
        # preSum[i]代表nums[i]之前的元素累计异或结果
        preSum = [0] * (n+1)
        for i in range(1, n+1):
            preSum[i] = arr[i-1] ^ preSum[i-1]
        # print(preSum)

        # todo 利用preSum数组查询arr任意连续区间的异或结果
        # a代表[0..i)的异或结果，x代表[i..j]的异或结果，b代表[0..j]的异或结果，
        # 现在已知a,b， 求x
        # a^x=b => a^x^a=b^a => x=a^b
        ans = []
        for i, j in queries:
            res = preSum[i] ^ preSum[j+1]
            ans.append(res)

        return ans
