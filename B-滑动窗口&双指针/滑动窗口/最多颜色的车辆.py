"""
题目描述
在一个狭小的路口，每秒只能通过一辆车，假设车辆的颜色只有 3 种，找出 n 秒内经过的最多颜色的车辆数量。

三种颜色编号为0 ，1 ，2

输入描述
第一行输入的是通过的车辆颜色信息

[0,1,1,2] 代表4 秒钟通过的车辆颜色分别是 0 , 1 , 1 , 2

第二行输入的是统计时间窗，整型，单位为秒

输出描述
输出指定时间窗内经过的最多颜色的车辆数量。

用例
输入	0 1 2 1
        3
输出	2
说明	在 3 秒时间窗内，每个颜色最多出现 2 次。例如：[1,2,1]

输入	0 1 2 1
        2
输出	1
说明	在 2 秒时间窗内，每个颜色最多出现1 次。

2023.03.31 根据考友反馈，本题会出现不止3种颜色，可能出现多种颜色，因此代码需要解除颜色限制。
"""

# todo 固定长度的滑窗 + 字典
'''
分析
简单的滑动窗口应用。(固定长度)
(我们可以利用相邻两个滑窗的差异比较，来避免重复的计算。)

 第二个滑窗相较于第一个滑窗而言，失去了0，新增了1，因此我们不需要重新统计第二个滑窗内部各种颜色的数量，只需要在第一个滑窗的统计结果基础上，减少0颜色数量1个，增加1颜色数量1个即可。
'''
import collections

# 输入
cars = input().split()
t = int(input())

def main():
    # 先排除特殊情况
    if t == 0:
        return 0
    
    n = len(cars)
    # 输出：找出 t 秒内经过的最多颜色的车辆数量
    ans = 0 
    # cars_cnt统计窗口内每种颜色的车出现的次数
    cars_cnt = collections.Counter() 
    
    # 第一个窗口
    for i in range(0, min(t, n)):   
        cars_cnt[cars[i]] += 1
        ans = max(ans, cars_cnt[cars[i]])
            
    # 后续窗口
    for i in range(t, n):
        remove = cars[i - t]  
        add = cars[i]  
        cars_cnt[remove] -= 1
        cars_cnt[add] += 1
        ans = max(ans, cars_cnt[add])  # 注意，这里新窗口最多的车辆只可能是新增加的这一辆
    return ans


