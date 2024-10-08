"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
 

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
        # 方法1: 将整数数组转换为整数直接进行整数加减运算
        # return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))

 
        # 方法2：数组遍历（推荐）
        # 11 -> 12, 19->20, 99->100
        n = len(digits)
        carry = 1
        for i in range(n-1, -1, -1):
            tmp = digits[i] + carry
            digits[i] = tmp % 10
            carry = tmp // 10
            
        return [carry] + digits if carry else digits
