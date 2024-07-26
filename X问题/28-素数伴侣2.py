"""
此题为匈牙利算法解决二分图最大匹配问题。我们可以把数据分为偶数，奇数两部分，然后进行配对（因为素数为一奇一偶的和）。
"""

import math


def isPrime(x):
    if x <= 3:
        return x > 1
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False

    return True


# // 该odd是否有匹配的even，返回boolean值
def match(odd):
    # // 对偶数进行遍历，看是否与该奇数配对
    for i in range(n):
        # // 若两数和为素数且该偶数在这轮循环中没有被访问过
        if isPrime(odd + evens[i]) and vis[i] == 0:
            # // 将该偶数标记为已访问
            vis[i] = 1
            # // p[i] = odd 为该偶数对应的odd储存值，如果该偶数没有奇数odd匹配，则为0，否则返回所匹配的odd
            # // 如果p[i]还未匹配或者p[i]已经有其他匹配的odd2，且该match(odd2)还有其他可以匹配的偶数(True)
            if p[i] == 0 or match(p[i]):
                # // 取代原来的p[i] = odd2，变为p[i] = odd
                p[i] = odd
                return True
    return False


while True:
    try:
        n = int(input())
        nums = list(map(int, input().split()))
        odds = []
        evens = []
        for num in nums:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
        m = len(odds)
        n = len(evens)
        s = 0
        p = [0] * n
        for num in odds:
            # // 每一次循环的vis必须要清空
            vis = [0] * n
            if match(num):
                s += 1
        print(s)

    except:
        break
