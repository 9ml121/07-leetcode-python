"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134590660

题目描述
n 个学生排成一排，学生编号分别是 1 到 n，n 为 3 的整倍数。

老师随机抽签决定将所有学生分成 m 个 3 人的小组（n == 3 * m） ，

为了便于同组学生交流，老师决定将小组成员安排到一起，也就是同组成员彼此相连，同组任意两个成员之间无其它组的成员。

因此老师决定调整队伍，老师每次可以调整任何一名学生到队伍的任意位置，计为调整了一次， 请计算最少调整多少次可以达到目标。

注意：对于小组之间没有顺序要求，同组学生之间没有顺序要求。

输入描述
两行字符串，空格分隔表示不同的学生编号。

第一行是学生目前排队情况
第二行是随机抽签分组情况，从左开始每 3 个元素为一组
n 为学生的数量，n 的范围为 [3, 900]，n 一定为 3 的整数倍

第一行和第二行元素的个数一定相同

输出描述
老师调整学生达到同组彼此相连的最小调整次数

备注
同组相连：同组任意两个成员之间无其他组的成员，比如有两个小组 [4, 5, 6] 和 [1, 2, 3]，

以下结果都满足要求：

1,2,3,4,5,6；

1,3,2,4,5,6；

2,3,1,5,6,4；

5,6,4,1,2,3；

以下结果不满足要求：

1,2,4,3,5,6；（4与5之间存在其他组的成员3）

用例1
输入
7 9 8 5 6 4 2 1 3
7 8 9 4 2 1 3 5 6
输出
1
说明
学生目前排队情况：7 9 8 5 6 4 2 1 3

学生分组情况：7 8 9 4 2 1 3 5 6

将3调整到4之前，队列调整为：7 9 8 5 6 3 4 2 1，那么三个小组成员均彼此相连 [7 9 8] [5 6 3] [4 2 1]

输出1

用例2
输入
8 9 7 5 6 3 2 1 4
7 8 9 4 2 1 3 5 6
输出
0
说明
学生目前排队情况：8 9 7 5 6 3 2 1 4

学生分组情况：7 8 9 4 2 1 3 5 6

无需调整，三个小组成员均彼此相连：

[7 8 9] [4 2 1] [3 5 6]

输出0
"""


# 1. 获取输入
# 第一行是学生目前排队情况
nums = list(map(int, input().split()))
# 第二行是随机抽签分组情况
sorted_nums = list(map(int, input().split()))
# print(nums, sorted_nums, sep = '\n')

# 测试用例
# nums = [1, 4, 7, 8, 9, 2, 3, 5, 6]
# sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2.根据sorted_nums统计每个数字所属的分组,并将nums转换为组号列表
num2group = {}
n = len(sorted_nums)
for i, num in enumerate(sorted_nums):
    num2group[num] = i // 3
groups = list(map(lambda x: num2group[x], nums))
# print(groups)
# [0, 1, 2, 2, 2, 0, 0, 1, 1]

# 3.判断groups需要调整的次数
cnt = 0
remove_groups = []  # 需要移动的分组
while len(groups) > 3:
    g1 = groups[0]
    g2 = groups[1]
    g3 = groups[2]
    if g1 == g2 == g3:  # 111 000
        groups = groups[3:]
    elif g1 == g2 != g3:  # 110 100 / 110 001
        if g1 in remove_groups:
            remove_groups.remove(g1)
        else:
            # todo 查找列表某个元素最后出现的索引下标,列表index()参数
            idx = groups.index(g1, 3)
            groups.pop(idx)
            cnt += 1
        groups = groups[2:]
    elif g1 == g3 != g2:  # 101 100 / 101 001
        remove_groups.append(g2)
        cnt += 1
        groups.pop(1)
    else:  # 102 010 122/ 100 110
        remove_groups.append(g1)
        cnt += 1
        groups.pop(0)

    # print(groups)

print(cnt)
