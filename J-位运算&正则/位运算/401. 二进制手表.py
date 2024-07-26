"""
二进制手表顶部有 4 个 LED 代表 小时（0-11），底部的 6 个 LED 代表 分钟（0-59）。
每个 LED 代表一个 0 或 1，最低位在右侧。

例如，下面的二进制手表读取 "4:51" 。
H 8 4 2 1  PM     => 0100 = 2^2 = 4
M 32 16 8 4 2 1   => 110011 = 2^5+2^4+2^1+2^0=32+16+2+1=51

给你一个整数 turnedOn ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。
你可以 按任意顺序 返回答案。

1.小时不会以零开头：
    例如，"01:00" 是无效的时间，正确的写法应该是 "1:00" 。
2.分钟必须由两位数组成，可能会以零开头：
    例如，"10:2" 是无效的时间，正确的写法应该是 "10:02" 。


示例 1：
输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

示例 2：
输入：turnedOn = 9
输出：[]


提示：
0 <= turnedOn <= 10
"""
from typing import List

# todo 暴力枚举 + 二进制运算

# 写法1：


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
        ans = []

        def countBits(n: int) -> int:
            # 计算整数n的二进制表示中 1 的个数。
            count = 0
            while n:
                count += n & 1  # n和1的与运算: 判断n的最低位是否为1，如果是则count加1。
                n >>= 1         # 将n右移1位，相当于将n的二进制表示向右移动一位，丢弃最低位。
            return count

        # 通过两个嵌套的循环遍历小时和分钟的所有可能取值。
        # 对于每个小时和分钟，我们使用 countBits 函数计算其二进制表示中 1 的个数，并判断是否等于给定的 num。
        # 如果相等，则将该小时和分钟的组合加入到结果列表中。
        for hour in range(12):
            for minute in range(60):
                if countBits(hour) + countBits(minute) == turnedOn:
                    ans.append(f"{hour}:{minute:02d}")
        return ans


"""
在Python中，f'{minute:02d}'是一种字符串格式化方法，用于将变量minute格式化为两位数的字符串。
 
具体来说，这里的f表示使用 f-string（格式化字符串），{}中的内容表示要插入的变量。
在这个例子中，变量minute被插入到{}中，并使用:后面的格式说明符进行格式化。 

在格式说明符中，02d表示将minute格式化为两位数的整数，并在不足两位时在前面补零。
例如，如果minute的值为5，那么f'{minute:02d}'将返回字符串'05'。 
 
这种格式化方法在需要将数字转换为特定格式的字符串时非常有用，例如在时间、日期等场景中。
"""

# 写法2


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # 给你一个数字 num， 将其分成两部分。其中一部分（不妨设为a）给小时，另一部分给分（就是 num - a）。
        # 最终的结果就是 a 能表示的所有小时的集合和 num - a所能表示的分的集合的笛卡尔积。
        # 枚举所有可能的 (a, num - a) 组合即可。
        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h)+bin(m)).count('1') == num:
                    # todo 要找 a 和 b 相加等于 num，并且 a 和 b 就是二进制表示中 1 的个数
                    time = str(h) + ":" + str(m).rjust(2, '0')
                    ans.append(time)

        return ans
