"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134724995?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22134724995%22%2C%22source%22%3A%22qfc_128220%22%7D

OJ用例
题解 - 部门人力分配 - Hydro

题目描述
部门在进行需求开发时需要进行人力安排。

当前部门需要完成 N 个需求，需求用 requirements 表述，requirements[i] 表示第 i 个需求的工作量大小，单位：人月。

这部分需求需要在 M 个月内完成开发，进行人力安排后每个月人力时固定的。

目前要求每个月最多有2个需求开发，并且每个月需要完成的需求不能超过部门人力。

请帮助部门评估在满足需求开发进度的情况下，每个月需要的最小人力是多少？

输入描述
输入为 M 和 requirements，M 表示需求开发时间要求，requirements 表示每个需求工作量大小，N 为 requirements长度，

1 ≤ N/2 ≤ M ≤ N ≤ 10000
1 ≤ requirements[i] ≤ 10^9
输出描述
对于每一组测试数据，输出部门需要人力需求，行末无多余的空格

用例1
输入
3
3 5 3 4
输出
6
说明
输入数据两行，

第一行输入数据3表示开发时间要求，

第二行输入数据表示需求工作量大小，

输出数据一行，表示部门人力需求。

当选择人力为6时，2个需求量为3的工作可以在1个月里完成，其他2个工作各需要1个月完成。可以在3个月内完成所有需求。

当选择人力为5时，4个工作各需要1个月完成，一共需要4个月才能完成所有需求。

因此6是部门最小的人力需求。
"""

# todo 考察：二分查找 + 左右双指针

# 输入
# 开发时间要求
m = int(input())
# 每个需求工作量大小
requirements = list(map(int, input().split()))


# 每个月最多2个需求开发，每个月的人力是固定的
# 输出在满足需求开发进度的情况下，每个月需要的最小人力
# 注意：隐含条件：一个需求只能在一个月内完成（参考"租车骑绿岛"）
def main():
    # 只有1个需求，最小人力就是当前需求天数
    if len(requirements) == 1:
        return requirements[0]

    requirements.sort()
    # 因为一个需求只能在一个月内完成，所以最低人力是max(requirements)，此时花的时间做多
    # 因为每个月最多2个需求开发，所以最高人力时requirements最多的2个需求天数之和，此时花的时间最少
    # todo 二分查找requirements 在人力为mid时，能不能在m天完成
    lo = requirements[-1]
    hi = requirements[-1] + requirements[-2]
    ans = hi
    while lo <= hi:
        mid = (lo+hi) >> 1
        # 如果最小人力为mid时，可以在m天内完成，得到一个可能解，需要在尝试有没有更优解
        if check(mid):
            ans = mid
            hi = mid-1
        else:
            lo = mid + 1
    return ans

# todo 以下逻辑类似：A-滑动窗口&双指针\双指针+其他算法\881. 救生艇.py
def check(mid):
    # 同向双指针：人力为mid时，需要的开发时间
    time = 0
    l = 0
    r = len(requirements)-1
    while l <= r:
        # 判断1个月时完成1个需求，还是可以完成2个需求
        if requirements[r] + requirements[l] > mid:
            # 最大的只能单独在1个月完成
            r -= 1
        else:
            # 最大和最小的2个需求可以在同一天完成
            l += 1
            r -= 1
        time += 1

    return time <= m


print(main())
