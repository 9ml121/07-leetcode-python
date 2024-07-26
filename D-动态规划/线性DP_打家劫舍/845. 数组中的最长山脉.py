"""
把符合下列属性的数组 arr 称为 山脉数组 ：
arr.length >= 3
存在下标 i（0 < i < arr.length - 1），满足
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
给出一个整数数组 arr，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 0 。



示例 1：
输入：arr = [2,1,4,7,3,2,5]
输出：5
解释：最长的山脉子数组是 [1,4,7,3,2]，长度为 5。

示例 2：
输入：arr = [2,2,2]
输出：0
解释：不存在山脉子数组。


提示：
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4


进阶：
你可以仅用一趟扫描解决此问题吗？
你可以用 O(1) 空间解决此问题吗？
"""
from typing import List
# todo 方法1：中心扩散法(左右双指针)（最优解）
# 类似：
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 返回arr最长山脉子数组的长度,（左边严格递增，右边严格递减）
        ans = 0
        n = len(arr)
        if n < 3:
            return 0

        for i in range(1, n-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                l = i
                r = i
                while l >= 1 and arr[l] > arr[l-1]:
                    l -= 1
                while r <= n-2 and arr[r] > arr[r+1]:
                    r += 1
                ans = max(ans, r-l+1)
        return ans
                
        
        

# 方法2：利用2个dp数组分别记录从左到右和从右到左遍历每个位置得到的最长山脉子数组长度（2趟扫描）
# 时间复杂度：O(N), 空间复杂度：O(N),注：dp数组可以压缩为O(1)的常数
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        # 返回arr最长山脉子数组的长度,（左边严格递增，右边严格递减）
        n = len(arr)
        if n < 3:
            return 0

        ans = 0
        left_inc = [0] * n
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                left_inc[i] = left_inc[i - 1] + 1
       

        right_inc = [0] * n
        for j in range(n-1, -1, -1):
            if arr[j] > arr[j + 1]:
                right_inc[j] = right_inc[j + 1] + 1
                if left_inc[j] >= 1 and right_inc[j] >= 1:
                    ans = max(ans, left_inc[j] + right_inc[j] + 1)
       

        return ans

