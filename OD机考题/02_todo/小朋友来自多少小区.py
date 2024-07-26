""" 
题目描述
幼儿园组织活动，老师布置了一个任务：

每个小朋友去了解与自己同一个小区的小朋友还有几个。

我们将这些数量汇总到数组 garden 中。

请根据这些小朋友给出的信息，计算班级小朋友至少来自几个小区？

输入描述
输入：garden[] = {2, 2, 3}

输出描述
输出：7

备注
garden 数组长度最大为 999
每个小区的小朋友数量最多 1000 人，也就是 garden[i] 的范围为 [0, 999]
用例
输入	2 2 3
输出	7
说明	
第一个小朋友反馈有两个小朋友和自己同一小区，即此小区有3个小朋友。

第二个小朋友反馈有两个小朋友和自己同一小区，即此小区有3个小朋友。

这两个小朋友，可能是同一小区的，且此小区的小朋友只有3个人。

第三个小区反馈还有3个小朋友与自己同一小区，则这些小朋友只能是另外一个小区的。这个小区有4个小朋友。

题目解析
本题的输出其实是至少的小朋友数量，而不是班级小朋友至少来自几个小区。

2 1 2 2 2 2 2 2 1 1
==> 13
"""

# 方法1
garden = list(map(int, input().split()))
garden.sort()
ans = garden[0] + 1
cnt = 1
for i in range(1, len(garden)):
    if garden[i] == garden[i-1] and cnt + 1 <= garden[i] + 1:
        cnt += 1
        continue
    cnt = 1
    ans += garden[i] + 1

print(ans)


# 方法2
import math
def solution(garden):
    cnts = {}
    for num in garden:
        cnts[num + 1] = cnts.get(num + 1, 0) + 1
    
    ans = 0
    for k, v in cnts.items():
        ans += math.ceil(v/k) * k

    return ans


garden = list(map(int, input().split()))
ans = solution(garden)
print(ans)
