"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:
输入: [7,5,6,4]
输出: 5


限制：
0 <= 数组长度 <= 50000
"""
from typing import List

'''
归并算法中：统计归并元素前面比他大的数：
1.当前位置要归并的是左边元素，cnt += 0
2.当前位置要归并的是右边元素，cnt += m - i + 1
3.如果只剩左边元素，cnt+=0
4.如果只剩右边元素：cnt+=0

方法1：统计归并元素前面比它大的数cnt：
1) 归并右边元素
        2是当前要归并回去的元素 
        k
nums: 1 4 5 8 / 2 3 6 7
tmp:    4 5 8 / 2 3 6 7
        i   m   j               
统计归并元素前面比它大的数cnt： 
cnt += m - i + 1

2）归并左边元素 
            4是当前要归并回去的元素 
            k
nums: 1 2 3 8 / 2 3 6 7
tmp:    4 5 8 /     6 7
        i   m       j               
cnt += 0   

3）只剩右边元素    
            5是当前要归并回去的元素
            k      
nums: 1 4 / 5 8
tmp:      / 5 8
        m i j
cnt += 0  
  
4）只剩左边元素    
            5是当前要归并回去的元素
            k      
nums: 1 4 / 5 8
tmp:  5 8 /  
      i m       j
cnt += 0    


方法2：统计归并元素后面比它小的数：
1)归并左边元素：
            4是当前要归并回去的元素
            k  
nums: 1 2 3 8 / 2 3 6 7
tmp:    4 5 8 /     6 7
          i m       j           
统计归并元素后面比它小的数：
cnt += j - m - 1

2)归并右边元素：cnt += 0   
3）只剩右边元素    
            5是当前要归并回去的元素
            k      
nums: 1 4 / 5 8
tmp:      / 5 8
        m i j
cnt += 0  
4）只剩左边元素    
              7是当前要归并回去的元素
              k      
nums: 4 5 / 6 4
tmp:    7 /    
        i m     j
统计归并元素后面比它小的数：
cnt += j - m - 1          
'''


class Solution:
    def __init__(self, tmp: list = None, cnt: int = 0):
        self.tmp = tmp  # tmp辅助数组，用做归并排序之前，记录原始数组的索引对应的值

    def reversePairs(self, nums: List[int]) -> int:
        """计算数组中的逆序对"""
        n = len(nums)
        if n == 0:
            return 0

        self.tmp = [0] * n
        return self._reversePairs(nums, 0, n - 1)

    def _reversePairs(self, nums, left, right) -> int:
        """将nums按照索引递归分成[left...mid] 和[mid+1, right]两部分，
        调用merge函数对2个数组合并排序, 计算并返回逆序对个数"""
        if left == right:  # 只有1个元素，结果为0
            return 0

        mid = (right + left) // 2  # 向下取整，可以保证mid+1不越界

        leftPairs = self._reversePairs(nums, left, mid)
        rightPairs = self._reversePairs(nums, mid + 1, right)

        # todo 二叉树后续位置
        # 优化：如果左数组最大值小于右数组最小值，整个数组就已经有序了，这时候左边都比右边小，mergeAndCnt = 0
        if nums[mid] <= nums[mid + 1]:
            return leftPairs + rightPairs
        else:
            # mergeAndCnt = self.mergeTwoSortedArr(nums, left, mid, right)  # 方法1：计算每一个数前面有多少个数比它大
            mergeAndCnt = self.mergeTwoSortedArr2(nums, left, mid, right)   # 方法2：计算每一个数后面有多少个数比它小
            return leftPairs + rightPairs + mergeAndCnt

    def mergeTwoSortedArr(self, nums, left, mid, right) -> int:
        """方法1：计算每一个数前面有多少个数比它大"""
        for i in range(left, right + 1):
            self.tmp[i] = nums[i]

        i, j = left, mid + 1
        cnt = 0  # cnt代表统计的逆序对总数
        for k in range(left, right + 1):
            if i == mid + 1:
                # 只剩右边元素
                nums[k] = self.tmp[j]
                j += 1
                # todo 统计归并元素 前面 比他 大 的数字个数
                # cnt += mid - i + 1  # 此时 mid - i + 1 = 0
            elif j == right + 1:
                nums[k] = self.tmp[i]
                i += 1
            elif self.tmp[i] <= self.tmp[j]:
                nums[k] = self.tmp[i]
                i += 1
            elif self.tmp[i] > self.tmp[j]:
                # 归并右边元素
                nums[k] = self.tmp[j]
                j += 1
                # todo 统计归并元素 前面 比他 大 的数字个数
                cnt += mid - i + 1
        return cnt

    def mergeTwoSortedArr2(self, nums, left, mid, right) -> int:
        """方法2：计算每一个数后面有多少个数比它小"""
        for i in range(left, right + 1):
            self.tmp[i] = nums[i]

        i, j = left, mid + 1
        cnt = 0  # cnt代表统计的逆序对总数
        for k in range(left, right + 1):
            if i == mid + 1:
                nums[k] = self.tmp[j]
                j += 1
            elif j == right + 1:
                # 只剩左边元素
                nums[k] = self.tmp[i]
                i += 1
                # todo 统计归并元素 后面 比他 小 的数字个数
                cnt += j - mid - 1
                # cnt += right - mid  # 这样写也可以
            elif self.tmp[i] <= self.tmp[j]:
                # 归并左边元素
                nums[k] = self.tmp[i]
                i += 1
                # todo 统计归并元素 后面 比他 小 的数字个数
                cnt += j - mid - 1
            else:
                nums[k] = self.tmp[j]
                j += 1
        return cnt


if __name__ == '__main__':
    nums = [7, 5, 6, 4]
    print(Solution().reversePairs(nums))
