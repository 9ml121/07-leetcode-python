"""
题目解析和算法源码
华为OD机试 - 堆内存申请（Java & JS & Python & C）-CSDN博客

题目描述
有一个总空间为100字节的堆，现要从中新申请一块内存，内存分配原则为：优先紧接着前一块已使用内存，分配空间足够且最接近申请大小的空闲内存。

输入描述
第1行是1个整数，表示期望申请的内存字节数

第2到第N行是用空格分割的两个整数，表示当前已分配的内存的情况，每一行表示一块已分配的连续内存空间，每行的第1和第2个整数分别表示偏移地址和内存块大小，如：

0 1

3 2

表示 0 偏移地址开始的 1 个字节和 3 偏移地址开始的 2 个字节已被分配，其余内存空闲。

输出描述
若申请成功，输出申请到内存的偏移；

若申请失败，输出 -1。

备注
若输入信息不合法或无效，则申请失败
若没有足够的空间供分配，则申请失败
堆内存信息有区域重叠或有非法值等都是无效输入
用例1
输入
1
0 1
3 2
输出
1
说明
堆中已使用的两块内存是偏移从0开始的1字节和偏移从3开始的2字节，空闲的两块内存是偏移从1开始2个字节和偏移从5开始95字节，根据分配原则，新申请的内存应从1开始分配1个字节，所以输出偏移为1。
"""

request = int(input())
arr = []
# todo 注意循环输入的处理方式
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

        if diff == request:
            return pre_y

        if diff > request and diff < minDiff:
            minDiff = diff
            ans = pre_y

        pre_y = cur_y

    # 处理收尾的数据
    diff = 100 - pre_y
    if diff > request and diff < minDiff:
        minDiff = diff
        ans = pre_y

    return ans


arr.sort(key=lambda x: x[0])
ans = solution(arr)
print(ans)
