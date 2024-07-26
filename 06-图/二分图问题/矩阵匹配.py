"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134628637?spm=1001.2014.3001.5501

OJ用例
题解 - 矩阵匹配 - Hydro

题目描述
从一个 N * M（N ≤ M）的矩阵中选出 N 个数，任意两个数字不能在同一行或同一列，求选出来的 N 个数中第 K 大的数字的最小值是多少。

输入描述
输入矩阵要求：1 ≤ K ≤ N ≤ M ≤ 150

输入格式：

N M K

N*M矩阵

输出描述
N*M 的矩阵中可以选出 M! / N! 种组合数组，每个组合数组种第 K 大的数中的最小值。无需考虑重复数字，直接取字典排序结果即可。

备注
注意：结果是第 K 大的数字的最小值

用例1
输入
3 4 2
1 5 6 6
8 3 4 3
6 8 6 3
输出
3
说明
N*M的矩阵中可以选出 M！/ N！种组合数组，每个组合数组种第 K 大的数中的最小值；

上述输入中选出数组组合为：

1,3,6;

1,3,3;

1,4,8;

1,4,3;

......

上述输入样例中选出的组合数组有24种，最小数组为1,3,3，则第2大的最小值为3
"""

# todo 考察二分图 + 二分查找
"""
题目需要我们多组N个元素中的第K大元素的最小取值，
换位思考一下，假设我们已经知道了第K大的最小取值是kth，那么：
    检查矩阵中是否至多找到（N - K + 1 个） ≤ kth 的元素值，且这些元素值互不同行同列
    N个数中，有K-1个数比kth大，那么相对应的有 (N - (K-1)) = (N - K + 1 ) 个数 ≤ kth。
    即找的 N - K + 1 个数中包含了 kth（第K大值）本身。

而kth的大小和二分图最大匹配是正相关的，因为：
    每个匹配边 其实就是 行号到列号的配对连线
    而行号和列号的组合其实就是坐标位置，根据坐标位置可以得到一个矩阵元素值

因此kth越小，意味着可以找到的 ≤ kth 的矩阵元素越少，相反的，kth 越大，则找到的 ≤ kth 的矩阵元素越多。
因此kth值大小和二分图最大匹配数是线性关系，我们可以使用二分法，来枚举kth。

二分枚举的范围是：1 ~ 矩阵元素最大值，这里不用担心二分枚举到kth不是矩阵元素，因为这种情况会被过滤掉，
原因是：我们要找 N - K + 1 个 <= kth 的矩阵元素，最后把关的必然是 kth 本身，即我们必然要在矩阵中找到一个 kth 值，如果二分枚举到的 kth 不是矩阵元素，则无法满足这个要求。
"""

# 输入
# N * M（N ≤ M）的矩阵中选出 N 个数, 1 ≤ K ≤ N ≤ M ≤ 150
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# print(grid)

# 输出：每个组合数组种第 K 大的数中的最小值。无需考虑重复数字，直接取字典排序结果即可

# 方法：二分查找 + 二分图


def main():
    # 确定k的取值范围
    lo = float('inf')
    hi = float('-inf')
    for i in range(n):
        for j in range(m):
            num = grid[i][j]
            lo = min(lo, num)
            hi = max(hi, num)

    # 二分查找n个数字中第k大的数字的最小值
    while lo <= hi:
        mid = (lo+hi) >> 1
        if check(mid):
            hi = mid-1
        else:
            lo = mid+1

    return lo


# 二分图配对：
def check(mid):
    # 判断选出来的n个数，第k大的数字有没有可能是mid

    # 1.利用二分图最大匹配来求解，小于等于kth（第K大值）的元素个数（即二分图最大匹配）
    smallerCount = 0

    # 2.match[j]表示列号j选取的行序号，初始化为-1， 表示没有选取
    match = [-1] * m
    # 1. 先遍历行序号，去找可以配对的列序号
    for i in range(n):
        # used记录每一列是否被选取
        vis = [False] * m
        if dfs(i, vis, match, mid):
            smallerCount += 1

    return smallerCount >= n-k+1


def dfs(i, vis, match, mid):
    # 1.行号i发起配对请求
    # 2.遍历列号，
    for j in range(m):
        # 3.如果当前列号j未被增广路探索过 && 当前列j行i可以配对（如果行列号位置(i,j)对应矩阵元素值小于等于kth（第K大值），则可以配对）
        if not vis[j] and grid[i][j] <= mid:
            vis[j] = True
            # 4.如果对应列号j未配对，或者，已配对但是配对的行号match[j]可以找到其他列号重新配对
            if match[j] == -1 or dfs(match[j], vis, match, mid):
                # 则当前行号i 和 列号j 可以配对
                match[j] = i
                return True

    return False


print(main())
