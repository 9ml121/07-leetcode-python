"""
题目解析和算法源码
华为OD机试 - 最大社交距离（Java & JS & Python & C & C++）_最大社交距离 od-CSDN博客

题目描述
疫情期间需要大家保证一定的社交距离，公司组织开交流会议。

座位一排共 N 个座位，编号分别为 [0, N - 1] 。

要求员工一个接着一个进入会议室，并且可以在任何时候离开会议室。

满足：

每当一个员工进入时，需要坐到最大社交距离（最大化自己和其他人的距离的座位）；
如果有多个这样的座位，则坐到索引最小的那个座位。
输入描述
会议室座位总数 seatNum

1 ≤ seatNum ≤ 500
员工的进出顺序 seatOrLeave 数组

元素值为 1，表示进场

元素值为负数，表示出场（特殊：位置 0 的员工不会离开）

例如 -4 表示坐在位置 4 的员工离开（保证有员工坐在该座位上）

输出描述
最后进来员工，他会坐在第几个位置，如果位置已满，则输出-1。

用例1
输入
10
[1, 1, 1, 1, -4, 1]
输出
5
说明
seat -> 0,空在任何位置都行，但是要给他安排索引最小的位置，也就是座位 0

seat -> 9,要和旁边的人距离最远，也就是座位 9

seat -> 4,要和旁边的人距离最远，应该坐到中间，也就是座位 4

seat -> 2,员工最后坐在 2 号座位上

leave[4], 4 号座位的员工离开

seat -> 5,员工最后坐在 5 号座位上
"""

import math

# 1.获取输入
seatNum = int(input())  # 1 ≤ seatNum ≤ 500
seatOrLeave = eval(input())
# print(type(seatOrLeave))

# 2.最后进来员工，他会坐在第几个位置，如果位置已满，则输出-1
last_num = -1
seats = []
for num in seatOrLeave:
    # 离开的座位号
    if num < 0:
        leave_num = -num
        seats.remove(leave_num)
    else:
        # 如果如果位置已满，则输出-1
        if len(seats) == seatNum:
            last_num = -1
            continue
        # 进来第一个员工，坐0号
        elif len(seats) == 0:
            seats.append(0)
            last_num = 0
        # 进来第二个员工，坐最后一个位置
        elif len(seats) == 1:
            seats.append(seatNum-1)
            last_num = seatNum-1
        else:
            # 进来第三个员工，需要比较seats上员工距离
            # 100010000
            max_dist = 0
            for i in range(1, len(seats)):
                dist = math.ceil((seats[i] - seats[i-1] - 1)/2)
                if dist > max_dist:
                    max_dist = dist
                    last_num = seats[i-1] + dist

            # 如果最后一个座位是空的，还要继续判断一次
            if seats[-1] != seatNum-1:
                dist = seatNum-1-seats[-1]
                if dist > max_dist:
                    last_num = seats[-1] + dist
            # 3.将进来的员工座位插入seats,并保证seats有序
            seats.append(last_num)
            seats.sort()
    # print(seats)
print(last_num)
