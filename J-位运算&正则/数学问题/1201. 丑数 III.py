"""
丑数是可以被 a 或 b 或 c 整除的 正整数 。

给你四个整数：n 、a 、b 、c ，请你设计一个算法来找出第 n 个丑数。

 

示例 1：

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
示例 2：

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。
示例 3：

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。
 

提示：

1 <= n, a, b, c <= 10^9
1 <= a * b * c <= 10^18
本题结果在 [1, 2 * 10^9] 的范围内
"""

# 方法1：超时
# 把 a, b, c 的倍数抽象成三条有序链表,
# 然后将这三条链表合并成一条有序链表并去除重复元素，这样合并后的链表元素就是丑数序列，我们从中找到第 n 个元素
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # 丑数是可以被 a 或 b 或 c 整除的 正整数，设计一个算法来找出第 n 个丑数
        
        productA = a
        productB = b
        productC = c

        p = 1
        ans = 0

        while p <= n:
            ans = min(productA, productB, productC)
            p += 1
            if ans == productA:
                productA += a
            if ans == productB:
                productB += b
            if ans == productC:
                productC += c

        return ans

# todo 方法2：二分查找 + 集合论 + 最小公倍数
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # 丑数是可以被 a 或 b 或 c 整除的 正整数，设计一个算法来找出第 n 个丑数
        
        # 计算a,b最大公因数（Greatest Common Divisor）
        def gcd(a: int, b: int) -> int:
            # 保证 a >= b，辗转相除/欧几里得算法
            if a < b:
                a, b = b, a
              
            while b != 0:
                a, b = b, a % b
            
            return a
            

        # 计算a,b最小公倍数 （Least Common Multiple）
        def lcm(a: int, b: int) -> int:
            # 最小公倍数就是乘积除以最大公因数
            return a * b // gcd(a, b)
        
        # 计算 [1..num] 之间有多少个能够被 a 或 b 或 c 整除的数字
        # 函数 f 的返回值是随着 num 的增加而增加的（单调递增）。
        def f(num: int) -> int:
            setA = num // a  # [1..num]能够整除 a 的数字个数
            setB = num // b  # [1..num]能够整除 b 的数字个数
            setC = num // c  # [1..num]能够整除 c 的数字个数
            setAB = num // lcm(a, b)  # A ∩ B 的元素个数
            setAC = num // lcm(a, c)  # A ∩ C 的元素个数
            setBC = num // lcm(b, c)  # B ∩ C 的元素个数
            setABC = num // lcm(lcm(a, b), c)  # A ∩ B ∩ C 的元素个数
            # 集合论定理：A + B + C - A ∩ B - A ∩ C - B ∩ C + A ∩ B ∩ C
            return setA + setB + setC - setAB - setAC - setBC + setABC

        # 求第 n 个能够整除 a 或 b 或 c 的数字是什么，也就是说我们要找到一个最小的 num，使得 f(num) == n
        # 这个 num 就是第 n 个能够整除 a 或 b 或 c 的数字。
        lo = 1
        hi = 2 * (10 ** 9)
        while lo <= hi:
            mid = (lo+hi) >> 1
            if f(mid) < n:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo


# 写法2：套用math.lcm
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        import math
        ab = math.lcm(a, b)
        bc = math.lcm(b, c)
        ac = math.lcm(a, c)
        abc = math.lcm(a, b, c)

        def check(mid):
            cnt = mid // a + mid//b + mid//c - mid // ab - mid // bc - mid//ac+mid//abc
            return cnt >= n
        
        left = 1
        right = 2*10**9
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


