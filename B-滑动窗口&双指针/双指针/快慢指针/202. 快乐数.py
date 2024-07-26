"""
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。

如果 n 是 快乐数 就返回 true ；不是，则返回 false 。


示例 1：
输入：n = 19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

示例 2：
输入：n = 2
输出：false


提示：
1 <= n <= 2^31 - 1
"""

"""
根据我们的探索，我们猜测会有以下三种可能。
1.最终会得到 1。
2.最终会进入循环。
3.值会越来越大，最后接近无穷大。(距离可以看出来不可能)
"""


# 方法一：用哈希集合检测链表是否有环(最容易理解)
class Solution:
    def isHappy(self, n: int) -> bool:
        # 计算数字n转化的下一个数字
        def get_next_nbr(num: int) -> int:
            next_nbr = 0
            while num > 0:
                digit = num % 10  # 从低位到高位
                next_nbr += digit ** 2
                num //= 10
            return next_nbr

        # 判断是否进入了一个循环
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next_nbr(n)

        return n == 1


# todo 方法二：快慢指针, 类似检测一个链表是否有环的问题
# 不管乌龟和兔子在循环中从哪里开始，它们最终都会相遇。这是因为兔子每走一步就向乌龟靠近一个节点（在它们的移动方向上）。
class Solution2:
    def isHappy(self, n: int) -> bool:
        # 计算数字n转化的下一个数字
        def get_next_nbr(num: int) -> int:
            next_nbr = 0
            while num > 0:
                digit = num % 10
                next_nbr += digit ** 2
                num //= 10
            return next_nbr

        slow = n
        fast = get_next_nbr(n)
        # 如果 n 是一个快乐数，即没有循环，那么快跑者最终会比慢跑者先到达数字 1。
        # 如果 n 不是一个快乐的数字，那么最终快跑者和慢跑者将在同一个数字上相遇。
        while fast != 1 and slow != fast:
            slow = get_next_nbr(slow)
            fast = get_next_nbr(get_next_nbr(fast))

        return fast == 1
