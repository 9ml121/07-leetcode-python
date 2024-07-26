"""
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

 
示例 1:
输入: num = 100
输出: "202"

示例 2:
输入: num = -7
输出: "-10"
 

提示：
-10^7 <= num <= 10^7
"""

# todo 将十进制整数转换为 x 进制字符串： 除 x 取余，并逆序输出
"""
10 进制转化任意进制的思路都是除 x 取余，其中 x 为进制数，比如 2 进制就是 除 2 取余，7 进制就是除 7 取余。
比如 num = 123， 需要转化为 7 进制
- 123//7=17, 余数为4
- 17//7=2，余数为3
- 2//7=0， 余数为2

123的七进制表示为234
"""

# 迭代写法
class Solution:
    def convertToBase7(self, num: int) -> str:
        # 将整数num转换为7进制字符串
        if num == 0:
            return "0"

        ans = []        # ans保存7进制从低位到高位的数字字符数组
        flag = '' if num >= 0 else '-'    # flag代表正负号
        x = abs(num)   

        while x > 0:
            x, remain = x//7, x % 7
            ans.append(str(remain))

        return flag + ''.join(ans[::-1])


# 递归写法
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        
        return self.convertToBase7(num // 7) + str(num % 7)


"""
# 拓展：将七进制字符串转换为十进制整数
# 输入：七进制字符串
base7_str = '234'

# 输出：代表的十进制整数
dec_int = int(base7_str, 7)
print(dec_int)  # 123
"""
