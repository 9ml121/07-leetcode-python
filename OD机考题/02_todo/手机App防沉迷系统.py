""" 
题目描述
智能手机方便了我们生活的同时，也侵占了我们不少的时间。“手机App防沉迷系统”能够让我们每天合理地规划手机App使用时间，在正确的时间做正确的事。

它的大概原理是这样的：

在一天24小时内，可以注册每个App的允许使用时段
一个时间段只能使用一个App
App有优先级，数值越高，优先级越高。注册使用时段时，如果高优先级的App时间和低优先级的时段有冲突，则系统会自动注销低优先级的时段，如果App的优先级相同，则后添加的App不能注册。
请编程实现，根据输入数据注册App，并根据输入的时间点，返回时间点使用的App名称，如果该时间点没有注册任何App，请返回字符串“NA”。

输入描述
第一行表示注册的App数量 N（N ≤ 100）

第二部分包括 N 行，每行表示一条App注册数据

最后一行输入一个时间点，程序即返回该时间点使用的App

2
App1 1 09:00 10:00
App2 2 11:00 11:30
09:30

数据说明如下：

N行注册数据以空格分隔，四项数依次表示：App名称、优先级、起始时间、结束时间
优先级1~5，数字越大，优先级越高
时间格式 HH:MM，小时和分钟都是两位，不足两位前面补0
起始时间需小于结束时间，否则注册不上
注册信息中的时间段包含起始时间点，不包含结束时间点

输出描述
输出一个字符串，表示App名称，或NA表示空闲时间

用例
输入	1
App1 1 09:00 10:00
09:30
输出	App1
说明	App1注册在9点到10点间，9点半可用的应用名是App1

输入	
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:20
输出	App2
说明	App1和App2的时段有冲突，App2优先级高，注册App2之后，App1自动注销，因此输出App2。

输入	
2
App1 1 09:00 10:00
App2 2 09:10 09:30
09:50
输出	NA
说明	无
"""




class App:
    def __init__(self, name, p, st, et) -> None:
        self.name = name
        self.p = p
        self.st = st
        self.et = et


n = int(input())
apps = {}
for i in range(n):
    name, p, st, et = input().split()
    if st >= et:
        continue

    # 注册使用时段时，如果高优先级的App时间和低优先级的时段有冲突，则系统会自动注销低优先级的时段
    # 如果App的优先级相同，则后添加的App不能注册
    flag = True
    remove_names = []
    for k, v in apps.items():
        if st >= v.et or et <= v.st:
            # 时间没有冲突
            continue
        else:
            # 时间有冲突
            # if p < v.p or (p == v.p and st >= v.st):
            if p <= v.p:
                # 优先级较低，或者优先级相同但是后添加, 不能注册
                flag = False
                break
            else:
                # 优先级较高，或者优先级相同但是先添加，原来注册的app要注销
                remove_names.append(k)

    if flag:
        app = App(name, p, st, et)
        apps[name] = app

    for k in remove_names:
        del apps[k]


time = input()
def solution():
    for name, app in apps.items():
        if app.st <= time < app.et:
            return name

    return 'NA'


ans = solution()
print(ans)
