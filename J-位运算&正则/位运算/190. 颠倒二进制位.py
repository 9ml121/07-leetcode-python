"""
颠倒给定的 32 位无符号整数的二进制位。

提示：
请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。

在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在 示例 2 中，输入表示有符号整数 -3，输出表示有符号整数 -1073741825。


示例 1：
输入：n = 00000010100101000001111010011100
输出：964176192 (00111001011110000010100101000000)
解释：输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
     因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
     
示例 2：
输入：n = 11111111111111111111111111111101
输出：3221225471 (10111111111111111111111111111111)
解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
     因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。


提示：
输入是一个长度为 32 的二进制字符串


进阶: 如果多次调用这个函数，你将如何优化你的算法？
"""



# 方法1：format函数 + reversed函数
class Solution:
    def reverseBits(self, n: int) -> int:
        # 颠倒给定的 32 位无符号整数的二进制位。
        
        # todo 将整数n转换为32位二进制字符串
        # s = format(n, '032b')[::-1]
        s = f'{n:032b}'[::-1]
        print(s)
        
        return int(s, 2)


# 方法2：位运算：二进制移位操作 + 与操作
class Solution:
    # 给定一个 32 位的无符号整型，让你按位翻转， 第一位变成最后一位， 第二位变成倒数第二位。。。

    # todo n 从高位开始逐步左移， ans 从低位（0）开始逐步右移
    # 逐步判断，如果该位是 1，就 res + 1 , 如果是该位是 0， 就 res + 0
    # todo 可以用任何数字和 1 进行位运算的结果都取决于该数字最后一位的特性简化操作和提高性能
    # n & 1 == 1, 说明 n 的最后一位是 1
    # n & 1 == 0, 说明 n 的最后一位是 0
    
    def reverseBits(self, n:int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) | (n & 1) 
            n >>= 1
        return ans
    
# or
class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(31, -1, -1):
            ans |= ((n >> i) & 1) << (31 - i)
        return ans
