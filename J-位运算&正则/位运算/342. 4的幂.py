"""
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x

 
示例 1：
输入：n = 16
输出：true

示例 2：
输入：n = 5
输出：false

示例 3：
输入：n = 1
输出：true
 

提示：

-2^31 <= n <= 2^31 - 1
 

进阶：你能不使用循环或者递归来完成本题吗？
"""


# todo n & (n-1) 这个操作在算法中比较常见，作用是消除数字 n 的二进制表示中的最后一个 1。
# 231. 2 的幂.py

# 方法2：
# 4 的幂次方的二进制表示 1 的位置都是在奇数位（且不在最低位），其他位置都为 0, 1=0b1, 4=0b100, 16=0b10000
# 2 的幂次方的特点是最低位之外，其他位置有且仅有一个 1（1 可以在任意位置），1=0b1, 2=0b10, 4=0b100, 8=0b1000

# 如果一个数字是四的幂次方，那么只需要满足：
# 1.是 2 的幂次方， 就能保证最低位之外，其他位置有且仅有一个 1
# 2.这个 1 一定在偶数位置出现
class Solution:
    # 写法 1
    def isPowerOfFour(self, n: int) -> bool:
        return n >= 1 and n & (n-1) == 0 and n.bit_length() % 2 == 1

    # 写法 2: n 是一个 32 位的有符号整数，因此我们可以构造一个整数 mask
    # 1.比如4:100,在第二位，那么就给出一个掩码01010101.....，需要32位，用十六进制表示，就是0x55555555,然后利用与运算，n & MASK，如果没有变，说明奇数位全为0，那么就满足了。
    # 2.也可以给出掩码位0xaaaaaaaa，代表了10101010....,奇数位为1，然后再跟n做与运算，如果为0，说明奇数位上没有，则满足。

    def isPowerOfFour(self, n: int) -> bool:
        MASK = 0x55555555
        return n >= 1 and n & (n-1) == 0 and n & MASK == n

    def isPowerOfFour(self, n: int) -> bool:
        MASK = 0xaaaaaaaa
        return n >= 1 and n & (n-1) == 0 and n & MASK == 0

    # 写法 3：将数字转化为二进制表示的字符串，利用字符串的相关操作进行判断
    def isPowerOfFour(self, num: int) -> bool:
        s = bin(num)[2:]
        return s.strip('0') == '1' and len(s) % 2 == 1

    # 写法 4：如果 n 是 4 的幂，那么它可以表示成 4**x的形式，我们可以发现它除以 3 的余数一定为 1，即：4**x === (3+1)**x === 1**x === 1(mod 3)
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1


# 方法1: 循环方法
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 判断n是不是4的幂次方
        while n > 0 and n % 4 == 0:
            n //= 4

        return n == 1
