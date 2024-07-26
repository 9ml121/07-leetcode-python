"""
题目描述
某软件系统会在运行过程中持续产生日志，系统每天运行N单位时间，运行期间每单位时间产生的日志条数保行在数组records中。records[i]表示第i单位时间内产生日志条数。
由于系统磁盘空间限制，每天可记录保存的日志总数上限为total条。
如果一天产生的日志总条数大于total，则需要对当天内每单位时间产生的日志条数进行限流后保存，请计算每单位时间最大可保存日志条数limit，以确保当天保存的总日志条数不超过total。
对于单位时间内产生日志条数不超过limit的日志全部记录保存;
对于单位时间内产生日志条数超过limit的日志，则只记录保存limit条日志；
如果一天产生的日志条数总和小于等于total，则不需要启动限流机制．result为-1。
请返回result的最大值或者-1。

输入描述
第一行为系统某一天运行的单位时间数N,1<=n<=10^5
第二行为表示这一天每单位时间产生的日志数量的数组records[]，0 <= records[i] <= 10^5
第三行为系统一天可以保存的总日志条数total。1 <= total <= 10^9

输出描述
每单位时间内最大可保存的日志条数limit，如果不需要启动限流机制，返回-1。

用例
输入	6
    3 3 8 7 10 15
    40
输出	9
说明	无
"""


def getResult(records: list, total: int):
    n = len(records)
    sumV = sum(records)
    # 如果不需要启动限流机制，返回-1
    if sumV <= total:
        return -1
    
    lo = total // n    # 最小限制数,这时候日志总数最小，肯定小于等于total(不用考虑索引越界)
    hi = max(records)  # 最大限制数,这时候日志总数最大，为sum(record)
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        # todo 计算限制数量为mid时，产生的日志总数fx(mid越大，fx越大)
        fx = sum(list(map(lambda r: r if r <= mid else mid, records)))
        
        if fx <= total:
            # 如果限制为mid时，fx没有超过，可以继续增大fx，即增大mid
            lo = mid + 1
        elif fx > total:
            # 如果fx超过了，肯定不行，需要减少fx,即减少mid
            hi = mid - 1
            
    # 如果mid为maxL,这时候fx<=record, minL = maxL + 1,说明不用限制
    if lo == max(records) + 1:
        return -1
    else:
        return lo - 1


if __name__ == '__main__':
    # 获取输入
    # n = int(input())
    # records = list(map(int, input().split()))
    # total = int(input())
    n = 6
    records = [3, 3, 8, 7, 10, 15]
    total = 40  # 输出	9
    # 问题：请计算每单位时间最大可保存日志条数limit，以确保当天保存的总日志条数不超过total？
    # limit最大值为max(records),也就是没有限制，这时候日志总是就是sum(records)
    # 最小值为1？日志总数为n，应该是total//n
    print(getResult(records, total))
