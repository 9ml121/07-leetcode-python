"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是质因子只包含 2、3 和 5 的正整数。

 
示例 1：
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

示例 2：
输入：n = 1
输出：1
解释：1 通常被视为丑数。
 

提示：
1 <= n <= 1690
"""

"""
todo 整体思路： 合并3个有序链表， 筛选素数
如果一个数 x 是丑数，那么 x * 2, x * 3, x * 5 都一定是丑数。
我们可以把丑数分为三类：2 的倍数、3 的倍数、5 的倍数。这三类丑数就好像三条有序链表，如下：

能被 2 整除的丑数：
1*2 -> 2*2 -> 3*2 -> 4*2 -> 5*2 -> 6*2 -> 8*2 ->...

能被 3 整除的丑数：
1*3 -> 2*3 -> 3*3 -> 4*3 -> 5*3 -> 6*3 -> 8*3 ->...

能被 5 整除的丑数：
1*5 -> 2*5 -> 3*5 -> 4*5 -> 5*5 -> 6*5 -> 8*5 ->...

我们如果把这三条「有序链表」合并在一起并去重，得到的就是丑数的序列，其中第 n 个元素就是题目想要的答案：
1 -> 1*2 -> 1*3 -> 2*2 -> 1*5 -> 3*2 -> 4*2 ->...

所以这里就和 链表双指针技巧汇总 中讲到的合并两条有序链表的思路基本一样了
对于这道题，我们抽象出三条有序的丑数链表，合并这三条有序链表得到的结果就是丑数序列，其中第 n 个丑数就是题目想要的答案。
"""

# 方法1：三指针解法，合并3个有序链表

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 给你一个整数 n ，请你找出并返回第 n 个 丑数 。
        # 丑数 就是质因子只包含 2、3 和 5 的正整数。

        # 理解为三个指向有序链表头结点的指针
        p2, p3, p5 = 1, 1, 1
        # 理解为三个有序链表的头节点的值
        product2, product3, product5 = 1, 1, 1
        # 理解为最终合并的有序链表（结果链表）
        ugly = [0] * (n + 1)
        # 理解为结果链表上的指针
        p = 1

        # 开始合并三个有序链表，找到第 n 个丑数时结束
        while p <= n:
            # 取三个链表的最小结点
            min_val = min(product2, product3, product5)
            # 将最小节点接到结果链表上
            ugly[p] = min_val
            p += 1
            # 前进对应有序链表上的指针
            if min_val == product2:
                product2 = 2 * ugly[p2]
                p2 += 1
            if min_val == product3:
                product3 = 3 * ugly[p3]
                p3 += 1
            if min_val == product5:
                product5 = 5 * ugly[p5]
                p5 += 1

        # 返回第 n 个丑数
        return ugly[n]


# 方法2：堆排序，合并n个有序链表
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        # 优先队列中装三元组 [product, prime, pi]
        # 其中 product 代表链表节点的值，prime 是计算下一个节点所需的质数因子，pi 代表链表上的指针
        pq = []
        primes = [2, 3, 5]
        for prime in primes:
            heapq.heappush(pq, [1, prime, 1])

        # 可以理解为最终合并的有序链表（结果链表）
        ugly = [0] * (n + 1)
        # 可以理解为结果链表上的指针
        p = 1

        while p <= n:
            # 取三个链表的最小结点
            product, prime, index = heapq.heappop(pq)

            # 避免结果链表出现重复元素
            if product != ugly[p - 1]:
                # 接到结果链表上
                ugly[p] = product
                p += 1

            # 生成下一个节点加入优先级队列
            heapq.heappush(pq, [ugly[index] * prime, prime, index + 1])

        return ugly[n]
