"""
超级丑数 是一个正整数，并满足其所有质因数都出现在质数数组 primes 中。

给你一个整数 n 和一个整数数组 primes ，返回第 n 个 超级丑数 。

题目数据保证第 n 个 超级丑数 在 32-bit 带符号整数范围内。

 

示例 1：

输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
示例 2：

输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。
 
提示：

1 <= n <= 10^5
1 <= primes.length <= 100
2 <= primes[i] <= 1000
题目数据 保证 primes[i] 是一个质数
primes 中的所有值都 互不相同 ，且按 递增顺序 排列
"""

# todo 堆 + 合并 K 条有序链表

"""
https://labuladong.online/algo/frequency-interview/ugly-number-summary/#%E8%B6%85%E7%BA%A7%E4%B8%91%E6%95%B0

把每个质因子看做一条有序链表，264题相当于让你合并三条有序链表，而这道题相当于让你合并 len(primes) 条有序链表，也就是 双指针技巧秒杀七道链表题目 中讲过的「合并 K 条有序链表」的思路。

注意我们在上道题抽象出了三条链表，需要 p2, p3, p5 作为三条有序链表上的指针，同时需要 product2, product3, product5 记录指针所指节点的值，每次循环用 min 函数计算最小头结点。

这道题相当于输入了 len(primes) 条有序链表，我们不能用 min 函数计算最小头结点了，而是要用优先级队列来计算最小头结点，同时依然要维护链表指针、指针所指节点的值，我们可以用一个三元组来保存这些信息。
"""

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        # 输入一个质数列表 primes 和一个正整数 n，请你计算第 n 个「超级丑数」。
        # 所谓超级丑数是一个所有质因数都出现在 primes 中的正整数
        import heapq
        # 优先队列中装三元组 [product, prime, pi]
        # 其中 product 代表链表节点的值，prime 是计算下一个节点所需的质数因子，pi 代表链表上的指针
        pq = []

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
