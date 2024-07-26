"""
题目描述
有一个简易内存池，内存按照大小粒度分类，每个粒度有若干个可用内存资源，用户会进行一系列内存申请，需要按需分配内存池中的资源返回申请结果成功失败列表。

分配规则如下：

1。分配的内存要大于等于内存的申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用；
2。需要按申请顺序分配，先申请的先分配，有可用内存分配则申请结果为true；没有可用则返回false。
注意：不考虑内存释放

输入描述
输入为两行字符串

第一行为内存池资源列表，包含内存粒度数据信息，粒度数据间用逗号分割

一个粒度信息内用冒号分割，冒号前为内存粒度大小，冒号后为数量
资源列表不大于1024
每个粒度的数量不大于4096
第二行为申请列表，申请的内存大小间用逗号分割

申请列表不大于100000
如
64:2,128:1,32:4,1:128
50,36,64,128,127

输出描述
输出为内存池分配结果
如true,true,true,false,false

用例
输入	64:2,128:1,32:4,1:128
        50,36,64,128,127
输出	true,true,true,false,false
说明	内存池资源包含：64K共2个、128K共1个、32K共4个、1K共128个的内存资源；
针对50,36,64,128,127的内存申请序列，分配的内存依次是：64,64,128,NULL,NULL,
第三次申请内存时已经将128分配出去，因此输出结果是：
true,true,true,false,false
"""

# todo 常规二分查找应用
'''
常规方案是2个循环，外循环是内存申请列表(要按照原序返回结果，因此不能排序)，内循环是可用的内存池资源列表(可提前排序好)
按照分配规则：
1。分配的内存要大于等于内存的申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用；
2。需要按申请顺序分配，先申请的先分配，有可用内存分配则申请结果为true；没有可用则返回false。
申请列表长度m上限10^5，资源列表长度n上限1024，时间复杂度O(mn)，10^8,肯定会时间超限，
二分查找的化可以转换为O(nlogm)，循环此时可以降低到百万级
'''


def binSearch(keys: list, num: int):
    # 1。优先使用内存小的  2。用掉了要数量减1
    # todo 左边界二分查找问题
    left = 0
    right = len(keys) - 1
    
    while left <= right:
        mid = (left + right) // 2
        val = keys[mid]
        if val >= num:  # 中间的比目标大，12 3 4 5  num=3
            right = mid - 1
        elif val < num:
            left = mid + 1
    # 找的是>=num的数，左侧二分查找
    if left == len(keys):  # 没有比num大的，返回False todo:这时候left = len(keys)，已经索引越界
        return False
    return keys[left]  # 有比num大的，返回的是keys中第一个大于等于num的值 todo:这时候left = mid


def getResult(pools: dict, applys: list):
    # 1。分配的内存要大于等于内存的申请量，存在满足需求的内存就必须分配，优先分配粒度小的，但内存不能拆分使用；
    # 2。需要按申请顺序分配，先申请的先分配，有可用内存分配则申请结果为true；没有可用则返回false。
    n = len(applys)
    res = ['false'] * n
    keys = sorted(pools.keys())  # 排序，用来二分查找

    for i in range(n):
        num = applys[i]
        target = binSearch(keys, num)
        if not target or pools[target] == 0:
            res[i] = 'flase'
        else:
            res[i] = 'true'
            pools[target] -= 1  # 维护内存池可用资源数量
            if pools[target] == 0:  # todo 维护二分查找的列表，避免重复查找
                keys.remove(target)  # todo 题目没说pools中key是否不重复，这里默认是不重复的,所以直接用remove

    return ','.join(res)


if __name__ == '__main__':
    # todo 注意这里获取输入的手法
    # pools = eval('{'+ input() + '}')
    # applys = list(map(int, input().split()))
    pools = {64: 2, 128: 1, 32: 4, 1: 128}
    applys = [50, 36, 64, 128, 127]
    # true,true,true,false,false
    print(getResult(pools, applys))
