"""
给你一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

你必须设计并实现线性时间复杂度的算法且仅使用常量额外空间来解决此问题。

 

示例 1：

输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。
示例 2：

输入：nums = [-1,0]
输出：[-1,0]
示例 3：

输入：nums = [0,1]
输出：[1,0]
 

提示：

2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
除两个只出现一次的整数外，nums 中的其他数字都出现两次
"""



from collections import Counter
from typing import List


# 方法1：计数器（空间复杂度为O(N)）
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [num for num, occ in freq.items() if occ == 1]
    

# todo 方法2：位运算

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 除两个只出现一次的整数外，nums 中的其他数字都出现两次，找出只出现一次的那两个元素
        
        # 1.获取两个只出现一次元素（a和b）异或的结果c（相同数字异或为0，故c可用所有数字异或求出）
        xor = 0
        for num in nums:
            xor ^= num

        # todo 代码实现时，需要找到异或和中的某个值为 1 的比特位。
        # 一种方式是计算 lowbit，只保留二进制最低位的 1，举例如下：
        '''
        s = 101100
        ~s = 010011           # ~s表示s的反码
        -s = (~s)+1 = 010100  # -s表示s的补码，即先按位取反再加1
        s & -s = 000100       # 原码(101100) 与 补码(010100) 做与运算( & )，得 000100，这就是原码s的lowbit
        '''
        lowbit = xor & -xor

        # 2.由于a和b都只出现一次，所以a!=b, 所以在异或和中必然有个比特位上的值是1
        # 再次遍历nums,对于这个比特位，把值为0的分为一组，值为1的分到另外一组
        # 那么a和b必然分到不同的组，现在同一组只有一个数出现一次，其余数都出现2次，所以问题就变成 136. 只出现一次的数字.py
        # 计算每一组的异或和，就是答案
        ans = [0, 0]
        for num in nums:
            if num & lowbit == 0:
                ans[0] ^= num
            else:
                ans[1] ^= num

        return ans


    # 位运算简化写法
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 除两个只出现一次的整数外，nums 中的其他数字都出现两次，找出只出现一次的那两个元素
        from functools import reduce
        from operator import xor

        xor_all = reduce(xor, nums)
        lowbit = xor_all & -xor_all
        ans = [0, 0]
        for x in nums:
            ans[(x & lowbit) != 0] ^= x  # 分组异或
        return ans
