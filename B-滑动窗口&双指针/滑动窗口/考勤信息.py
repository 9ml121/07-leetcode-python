""" 
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127944519

题目描述
公司用一个字符串来表示员工的出勤信息

absent：缺勤
late：迟到
leaveearly：早退
present：正常上班
现需根据员工出勤信息，判断本次是否能获得出勤奖，能获得出勤奖的条件如下：

缺勤不超过一次；
没有连续的迟到/早退；
任意连续7次考勤，缺勤/迟到/早退不超过3次。
输入描述
用户的考勤数据字符串

记录条数 >= 1；
输入字符串长度 < 10000；
不存在非法输入；
输出描述
根据考勤数据字符串，如果能得到考勤奖，输出”true”；否则输出”false”。

用例1
输入
2
present
present present
输出
true true
用例2
输入
2
present
present absent present present leaveearly present absent
输出
true false
"""

# 考察滑动窗口和逻辑分析
n = int(input())

def check(records):
    # 缺勤不超过一次
    absents = 0
    # 没有连续的迟到/早退
    late_or_early = {'late', 'leaveearly'}
    # 任意连续7次考勤，缺勤/迟到/早退不超过3次
    presents = 0
    n = len(records)
    pre = 'present'
    start = 0
    for i in range(n):
        r = records[i] 
        if r == 'absent':
            absents += 1
            if absents > 1:
                # 缺勤不超过一次
                return False
        elif r == 'present':
            presents += 1
        else:
            # 没有连续的迟到/早退
            if pre in late_or_early:
                return False
        pre = r

        if i >= 7:
            presents -= (records[start] == 'present')
            start += 1
        
        # 任意连续7次考勤，缺勤/迟到/早退不超过3次
        # 也就是正常次数要大于等于4次
        window_sz = min(7, i - start + 1)
        not_presents = window_sz - presents
        if not_presents > 3:
            return False
    return True


ans = []
for i in range(n):
    records = input().split()
    if check(records):
        ans.append('true')
    else:
        ans.append('false')

print(' '.join(ans))
