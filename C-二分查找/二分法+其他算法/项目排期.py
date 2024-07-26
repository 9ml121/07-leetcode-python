"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134772481?spm=1001.2014.3001.5502

题目描述
项目组共有 N 个开发人员，项目经理接到了 M 个独立的需求，每个需求的工作量不同，且每个需求只能由一个开发人员独立完成，不能多人合作。

假定各个需求直接无任何先后依赖关系，请设计算法帮助项目经理进行工作安排，使整个项目能用最少的时间交付。

输入描述
第一行输入为 M 个需求的工作量，单位为天，用逗号隔开。

例如：

X1 X2 X3 ... Xm

表示共有 M 个需求，每个需求的工作量分别为X1天，X2天，...，Xm天。其中：

0 < M < 30
0 < Xm < 200
第二行输入为项目组人员数量N

例如：

5

表示共有5名员工，其中 0 < N < 10

输出描述
最快完成所有工作的天数

例如：

25

表示最短需要25天完成所有工作

用例1
输入
6 2 7 7 9 3 2 1 3 11 4
2
输出
28
说明
共有两位员工，其中一位分配需求 6 2 7 7 3 2 1 共需要28天完成，另一位分配需求 9 3 11 4 共需要27天完成，故完成所有工作至少需要28天。
"""


"""
本题可以换个说法理解：

M个独立需求 →  M个球
N个开发人员  →  N个桶
现在要将M个球装入N个桶中，问桶的最小容量是多少？

我们可以利用二分法来求桶的容量，首先确定桶容量的范围：
    如果桶非常多，满足一个球一个桶，那么此时桶容量至少应该是max(X1, X2, ... , Xm)
    如果桶非常少，比如只有一个桶，那么此时所有球都需要装入该桶，则桶容量至多是 sum(X1, X2, ..., Xm)
    因此，我们可以在上面范围内二分取中间值mid作为可能的最小桶容量去尝试：N个桶装M个球

关于N个桶装M个球是否可以装下，本题N,M数量级较小，可以使用回溯算法，暴力尝试所有球装桶情况，只要发现一种可以装完的策略，则可以返回TRUE，即在对应mid容量下可以实现N个桶装M个球。

具体实现请看：参考leetcode 698.划分为k个相等的子集.py

如果mid可以实现实现N个桶装M个球，则二分中间值mid就是一个可能解，但不一定是最优解，我们应该尝试更小的容量，此时只需要缩小二分的右边界为mid-1，然后再次二分取中间值即可。

如果mid不可以实现N个桶装M个球，则说明mid容量取小了，因此我们应该尝试更大的容量，此时只需要扩大二分的左边界为mid+1，然后再次二分取中间值即可。

"""
# todo 考察二分法 + 回溯算法（划分为k个等和子集）

# 输入获取
# 第一行输入为 M 个需求的工作量
days = list(map(int, input().split()))
# 第二行输入为项目组人员数量N
n = int(input())  # 其中 0 < N < 10

#
# 输出：最短需要多少天完成所有工作


def main():
    # 1.这里对days降序，有利于降低后面回溯操作的复杂度
    days.sort(reverse=True)
    print(days)

    # 项目组人员为1时，需要完成天数最大，为sum(days)
    # 由于每个需求只能由一个开发人员独立完成，因此最快的完成天数为max(days)
    lo = days[0]  # 桶至少要有max(balls)的容量
    hi = sum(days)  # 当只有一个桶时，此时该桶容量要装下所有balls

    # 记录题解
    ans = hi

    # todo 二分查找days需求，在n个开发人员下，能不能在mid天完成
    while lo <= hi:
        mid = (lo + hi) >> 1

        if check(0, [0] * n, mid):
            # 如果k个mid容量的桶，可以装完所有balls，那么mid容量就是一个可能解，但不一定是最优解，我们应该尝试更小的桶容量
            ans = mid
            hi = mid - 1
        else:
            # 如果k个mid容量的桶，无法装完所有balls，那么说明桶容量取小了，我们应该尝试更大的桶容量
            lo = mid + 1

    return ans


def check(idx, buckets, limit):
    """
    :param index: 要被装入球的（balls）索引
    :param buckets: 桶数组，buckets[i]记录第i个桶的已经使用的容量
    :param limit: 每个桶的最大容量，即限制
    :return: k个桶（每个桶容量limit）是否可以装下所有balls
    """
    if idx == len(days):
        # 如果balls已经取完，则说明k个limit容量的桶，可以装完所有balls
        return True

    # select是当前要装的球
    selected = days[idx]

    # 遍历桶
    for i in range(len(buckets)):
        # 剪枝优化
        if i > 0 and buckets[i] == buckets[i - 1]:
            continue

        # 如果当前桶装了当前选择的球后不超过容量限制，则可以装入
        if selected + buckets[i] <= limit:
            buckets[i] += selected
            # 递归装下一个球
            if check(idx + 1, buckets, limit):
                return True
            # 如果这种策略无法装完所有球，则回溯
            buckets[i] -= selected

    return False


# 算法调用
print(main())
