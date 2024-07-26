"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

 

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
 

提示：

1 <= num1.length, num2.length <= 200
num1 和 num2 只能由数字组成。
num1 和 num2 都不包含任何前导零，除了数字0本身。
"""

# todo 考察数学知识
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        # todo 两数相乘的结果长度最多为两数长度之和
        res = [0] * (n1+n2)

        # 从后往前遍历两个数字字符串
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                # todo 两个位置相乘的计算结果应该填到res[i+j+1]这个位置
                mul = int(num1[i]) * int(num2[j]) + res[i+j+1]
                res[i+j+1] = mul % 10  # 当前位
                res[i+j] += mul // 10  # 进位

        # print(res)
        # 将结果转化为字符串，跳过前导0
        ans = ''.join(map(str, res))
        return ans.lstrip('0')  # 去除可能存在的前导0
