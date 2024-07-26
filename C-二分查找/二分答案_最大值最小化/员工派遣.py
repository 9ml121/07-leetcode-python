"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135050312?spm=1001.2014.3001.5501

OJ用例
题解 - 员工派遣 - Hydro

题目描述
某公司部门需要派遣员工去国外做项目。

现在，代号为 x 的国家和代号为 y 的国家分别需要 cntx 名和 cnty 名员工。

部门每个员工有一个员工号（1,2,3,......），工号连续，从1开始。

部长派遣员工的规则：

规则1：从 [1, k] 中选择员工派遣出去
规则2：编号为 x 的倍数的员工不能去 x 国，编号为 y 的倍数的员工不能去 y 国。
问题：

找到最小的 k，使得可以将编号在 [1, k] 中的员工分配给 x 国和 y 国，且满足 x 国和 y 国的需求。

输入描述
四个整数 x，y，cntx，cnty。

2 ≤ x < y ≤ 30000
x 和 y 一定是质数
1 ≤ cntx, cnty < 10^9
cntx + cnty ≤ 10^9
输出描述
满足条件的最小的k

用例1
输入
2 3 3 1
输出
5
说明
输入说明：

2 表示国家代号2

3 表示国家代号3

3 表示国家2需要3个人

1 表示国家3需要1个人
"""


# 考察：二分法
import sys

# 输入
# 四个整数 x，y，cntx，cnty。x 和 y 一定是质数,2 ≤ x < y ≤ 30000
x, y, cntx, cnty = map(int, input().split())

# 找到最小的 k，使得可以将编号在 [1, k] 中的员工分配给 x 国和 y 国，且满足 x 国和 y 国的需求。


def main():
    # [1..k]个数，为x的倍数的个数为k//x, 为y的倍数的个数为k//y, 同时为x也为y的倍数的数个数为k//(x*y)
    # 将x的倍数，不为y的倍数分给y
    # 将y的倍数，不为x的倍数分给x
    # 剩下的数看能不能满足x和y还需要的人数

    # k的最小数为cntx+cnty, 最大数设为sys.maxsize
    lo = cntx + cnty
    # hi = sys.maxsize
    hi = 10**9
    ans = lo
    while lo <= hi:
        mid = (lo+hi) >> 1
        if check(mid):
            ans = mid
            hi = mid-1
            # print(ans)
        else:
            lo = mid+1

    return ans


def check(k):  # k = 63
    # 判断[1..k]是否满足x 国和 y 国的需求。
    nxy = k//(x*y)
    nx = k//x  # 12
    ny = k//y  # 2
    # 将y的倍数，不是x的倍数的人分配给x,反之亦然
    remain_x = max(cntx - (ny - nxy), 0)  #
    remain_y = max(cnty - (nx - nxy), 0)
    # 剩余不为x和y的倍数个数
    remain = k - (nx+ny-nxy)  # 53
    return remain >= remain_x + remain_y


# print(check(63)) # 71
print(main())
