"""
描述
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。
现在密码学会请你设计一个程序，从已有的 n （ n 为偶数）个正整数中挑选出若干对组成“素数伴侣”，
挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，
而将2和5、6和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，
当然密码学会希望你寻找出“最佳方案”。

输入:
有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。
4
2 5 6 13

输出:
输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。
2


数据范围： 1≤n≤100  ，输入的数据大小满足 2≤value≤30000
输入描述：
输入说明
1 输入一个正偶数 n
2 输入 n 个整数

输出描述：
求得的“最佳方案”组成“素数伴侣”的对数。
"""
import math

'''
此题为匈牙利算法解决二分图最大匹配问题。我们可以把数据分为偶数，奇数两部分，然后进行配对（因为素数为一奇一偶的和）。
解题思路： 
1.判断一个数是否为素数：
    在这里需要注意的是全部数判断会超时，所以选择半位数来判断可以节省时间。
    选用原理：一个数能被另一个数除尽，则这个数也能被它的2倍数除尽，一个数不能被另一个数除尽则也不能被它的2倍数除尽。 
2.判断最大匹配数： 
    这个是参考已有的答案来的，一个列表里的数与另一个列表里的每一个数判断，如果他们的和是素数就标记，
    若这个数还有另一个匹配的数，则看看之前匹配的数是否还有其他匹配的数，有则这个数就被当前数替代，没有则跳过。
    如此一来得到的数即为最大匹配数 
3.数的分配与具体判断实现： 
    奇数和奇数相加与偶数和偶数相加得到的是偶数不可能是素数，只能是奇数和偶数相加才可能存在素数。
    因此将所有可匹配的数按奇数和偶数分为两个列表。然后让每一个奇数与所有偶数列表的数去匹配看相加的和是否为素数，如果是则加1。
最终将计算的数打印出来
'''


def isPrime(num):  # 判断是否是素数
    # 用math.ceil要对2单独判断
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def find(odd, visited, choose, evens):  # 配对的过程
    for j, even in enumerate(evens):
        # 如果即能配对，这两个数之前没有配过对（即使两个不能配对visit值为0，但是也不能过是否是素数这一关，所以visit就可以看为两个能配对的素数是否能配对）
        if isPrime(odd + even) and not visited[j]:
            visited[j] = True  # 代表这两个数能配对
            # 如果当前奇数没有和任何一个偶数现在已经配对，那么认为找到一组可以连接的，如果当前的奇数已经配对，那么就让那个与之配对的偶数断开连接，让他再次寻找能够配对的奇数
            if choose[j] == 0 or find(choose[j], visited, choose, evens):
                choose[j] = odd  # 当前奇数已经和当前的偶数配对
                return True
    return False  # 如果当前不能配对则返回False


def getResult(nums):
    count = 0
    evens = []
    odds = []

    # 将输入的数分为奇数和偶数
    for num in nums:
        if num % 2 == 0:
            odds.append(num)
        else:
            evens.append(num)

    # choose用来存放当前和这个奇数配对的那个偶数
    choose = [0] * len(evens)
    for odd in odds:
        # visit用来存放当前奇数和偶数是否已经配过对
        visited = [False] * len(evens)
        if find(odd, visited, choose, evens):
            count += 1
    # print(count)
    return count


if __name__ == '__main__':
    # n = int(input())
    # nums = list(map(int, input().split(" ")))
    n = 4
    nums = [2, 5, 6, 13]
    print(getResult(nums))
