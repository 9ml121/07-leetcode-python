"""
对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。

例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
给你一个整数 num ，输出它的补数。

 

示例 1：

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。
示例 2：

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。
 

提示：

1 <= num < 231
 

注意：本题与 1009 https://leetcode-cn.com/problems/complement-of-base-10-integer/ 相同
"""


class Solution:
    def findComplement(self, num: int) -> int:
        # 构造掩码 mask=2**(i+1)−1，它是一个 i+1 位的二进制数，并且每一位都是 1
        # 将 num 与 mask 进行异或运算，即可得到答案
        high_bit = num.bit_length()
        return num ^ ((1 << high_bit) - 1)


if __name__ == '__main__':
    # 整数取反示例
    num = 5   # 二进制表示：00000101
    result = ~num
    print(bin(result))  # 输出：-0b110, 其对应的二进制表示为11111010
    
    # 布尔值取反示例
    a = True
    b = False
    print(~a)   # 输出：-2
    print(~b)   # 输出：-1
    
    # 位级别数据翻转示例
    data = 0b10101010
    result = ~data
    print(bin(result))  # 输出：-0b10101011, 其二进制表示为11111101
