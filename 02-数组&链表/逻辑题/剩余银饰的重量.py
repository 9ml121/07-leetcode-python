"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134640254

OJ用例
题解 - 剩余银饰的重量 - Hydro

题目描述
有 N 块二手市场收集的银饰，每块银饰的重量都是正整数，收集到的银饰会被熔化用于打造新的饰品。

每一回合，从中选出三块最重的银饰，然后一起熔掉。

假设银饰的重量分别为 x 、y和z，且 x ≤ y ≤ z。那么熔掉的可能结果如下：

如果 x == y == z，那么三块银饰都会被完全熔掉；
如果 x == y 且 y != z，会剩余重量为 z - y 的银块无法被熔掉；
如果 x != y 且 y == z，会剩余重量为 y - x 的银块无法被熔掉；
如果 x != y 且 y != z，会剩余重量为 z - y 与 y - x 差值 的银块无法被熔掉。
最后，

如果剩余两块，返回较大的重量（若两块重量相同，返回任意一块皆可）
如果只剩下一块，返回该块的重量
如果没有剩下，就返回 0
输入描述
输入数据为两行：

第一行为银饰数组长度 n，1 ≤ n ≤ 40，
第二行为n块银饰的重量，重量的取值范围为[1，2000]，重量之间使用空格隔开
输出描述
如果剩余两块，返回较大的重量（若两块重量相同，返回任意一块皆可）；

如果只剩下一块，返回该块的重量；

如果没有剩下，就返回 0。

用例1
输入
3
1 1 1
输出
0
说明
选出1 1 1，得到 0，最终数组转换为 []，最后没有剩下银块，返回0

用例2
输入
3
3 7 10
输出
1
说明
选出 3 7 10，需要计算 (7-3) 和 (10-7) 的差值，即(7-3)-(10-7)=1，所以数组转换为 [1]，剩余一块，返回该块重量，返回1
"""


# 输入
# 数组长度
n = int(input())
# n块银饰重量
weights = list(map(int, input().split()))


def main():
    # 每一回合，从中选出三块最重的银饰
    weights.sort()
    # print(weights)

    if n < 3:
        # 只有1块或者2块,返回较大的重量
        return weights[-1]

    while len(weights) >= 3:
        z = weights.pop()
        y = weights.pop()
        x = weights.pop()
        if x == y == z:
            continue
        elif z == y and y != x:
            weights.append(y-x)
        elif z != y and y == x:
            weights.append(z-y)
        else:
            # x!= y and y != z:
            # todo 当 x != y 且 y != z，此时剩余重量为 z - y 与 y - x 差值 的银块，可能是0，即完全融掉的情况
            diff = abs((z-y) - (y-x))
            if diff > 0:
                weights.append(diff)

        weights.sort()

    return weights[-1] if weights else 0


print(main())
