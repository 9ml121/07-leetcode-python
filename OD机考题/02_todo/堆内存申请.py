"""
5
0 2
8 10
20 2

10
24 4
29 7
47 2
"""

requst = int(input())
arr = []
while True:
    try:
        start, size = map(int, input().split())
        arr.append([start, start + size])
    except:
        break

# 内存分配原则为：优先紧接着前一块已使用内存，分配空间足够且最接近申请大小的空闲内存。


def solution(arr):
    minDiff = 101
    ans = -1
    pre_y = 0
    for i in range(len(arr)):
        cur_x, cur_y = arr[i]
        diff = cur_x - pre_y
        if diff < 0 or cur_y > 100:
            return -1

        if diff == requst:
            return pre_y

        if diff > requst and diff < minDiff:
            minDiff = diff
            ans = pre_y

        pre_y = cur_y

    diff = 100 - pre_y
    if diff > requst and diff < minDiff:
        minDiff = diff
        ans = pre_y

    return ans


arr.sort(key=lambda x: x[0])
ans = solution(arr)
print(ans)
