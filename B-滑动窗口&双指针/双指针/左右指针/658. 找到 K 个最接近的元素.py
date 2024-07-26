"""
给定一个 排序好 的数组 arr ，两个整数 k 和 x ，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。

整数 a 比整数 b 更接近 x 需要满足：

|a - x| < |b - x| 或者
|a - x| == |b - x| 且 a < b
 

示例 1：

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]
示例 2：

输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]
 

提示：

1 <= k <= arr.length
1 <= arr.length <= 10^4
arr 按 升序 排列
-10^4 <= arr[i], x <= 10^4
"""
from typing import List
# todo 方法1:逆向思考 + 左右双指针（推荐）

class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # 从升序数组arr中找到最靠近 x（两数之差最小）的 k 个数
        # 也就是要删除n-k个最远离x的数，因为arr有序，所以跟x绝对差最大的数只可能在数组两边
        n = len(arr)
        l = 0
        r = n - 1
        for _ in range(n-k):
            if x - arr[l] <= arr[r] - x:
                # 删除最右边
                r -= 1
            else:
                # 删除最左边
                l += 1
        
        return arr[l:r+1]
    
# 方法2：二分查找 + 中心扩散法
# 类似 B-滑动窗口&双指针\双指针\左右指针\845. 数组中的最长山脉.py

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from bisect import bisect_left
        # 从升序数组arr中找到最靠近 x（两数之差最小）的 k 个数
        # todo l,r指向arr中跟x绝对差值最小的2个相邻索引, 以这2个位置为中心向两边扩散，直到找到k个数
        r = bisect_left(arr, x) # arr[r] >= x
        l = r - 1  # arr[l] < x
        
        for _ in range(k):
            if l < 0: 
                r += 1
            elif r >= len(arr) :
                l -= 1
            elif x - arr[l] <= arr[r] - x:
                l -= 1
            else:
                r += 1
        return arr[l + 1: r]



