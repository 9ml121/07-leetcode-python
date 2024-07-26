"""
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

 
示例 1：
输入：num1 = "11", num2 = "123"
输出："134"

示例 2：
输入：num1 = "456", num2 = "77"
输出："533"

示例 3：
输入：num1 = "0", num2 = "0"
输出："0"
 

提示：
1 <= num1.length, num2.length <= 104
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
"""

# todo 简单的​多指针指向问题
# 类似：03-数组&链表\链表指针指向问题\2. 两数相加.py


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 从后往前，将num1和num2相同位置数值累计，返回相加之后的数字字符串
        n1 = len(num1) - 1
        n2 = len(num2) - 1
        ans = ''
        carry = 0
        
        while n1 >= 0 or n2 >= 0 or carry:
            total = carry
            if n1 >= 0:
                total += int(num1[n1])
            if n2 >= 0:
                total += int(num2[n2])
                
            d = total % 10
            carry = total // 10
            ans = str(d) + ans
            n1 -= 1
            n2 -= 1

        return ans
