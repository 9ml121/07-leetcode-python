"""
题目描述
一个设备由N种类型元器件组成(每种类型元器件只需要一个，类型type编号从0~n-1)，
每个元器件均有可靠性属性reliability，可靠性越高的器件其价格price越贵。
而设备的可靠性由组成设备的所有器件中可靠性最低的器件决定。

给定预算S，购买N种元器件( 每种类型元器件都需要购买一个)，在不超过预算的情况下，请给出能够组成的设备的最大可靠性。

输入描述
S n // S总的预算，N元器件的种类
total // 元器件的总数，每种型号的元器件可以有多种;
此后有total行具体器件的数据
type reliability price // type 整数类型，代表元器件的类型编号从0 ~ n-1; reliabilty 整数类型 ，代表元器件的可靠性; price 整数类型 ，代表元器件的价格

输出描述
符合预算的设备的最大可靠性，如果预算无法买齐N种器件，则返回 -1

备注
0 <= S,price <= 10000000
0 <= n <= 100
0 <= type <= n-1
0 <= total <= 100000
0 < reliability <= 100000

用例
输入	500 3
6
0 80 100
0 90 200
1 50 50
1 70 210
2 50 100
2 60 150
输出	60
说明
预算500，设备需要3种元件组成，方案
类型0的第一个(可靠性80),
类型1的第二个(可靠性70),
类型2的第二个(可靠性60),
可以使设备的可靠性最大 60

输入	100 1
1
0 90 200
输出	-1
说明	组成设备需要1个元件，但是元件价格大于预算，因此无法组成设备，返回-1
"""


# 设备类
class Device:
    def __init__(self, reliability: int, price: int):
        self.reliability = reliability
        self.price = price


# 判断最高可靠性为rel时，1.能否买足所有类型设备，2.总价格不超标
# kinds为对应类型的所有器件类：已经按照可靠性升序排列
# S为金额限制
def check(kinds, S, rel: int):
    sumPrice = 0  # 统计最终花费的价格

    # 在kind种类内找到第一个可靠性>=目标值的器件
    # 左侧边界二分查找
    for kind in kinds:  # kind内的器件已经按照可靠性升序
        n = len(kind)
        low = 0
        high = n - 1

        while low <= high:  # 3,5,7  t =8
            mid = (low + high) // 2
            device = kind[mid]

            if device.reliability >= rel:
                high = mid - 1
            elif device.reliability < rel:
                low = mid + 1

        # 判断kind所有类型产品可靠性是否有>=目标值可
        if low == n:  # 说明kind所有产品可靠性都小于目标值
            return False

        # kind[low]为kind中第一个>=目标值的产品
        sumPrice += kind[low].price

    # 2.总价格不超标
    return sumPrice <= S


def getResult(datas, S, N):
    # S总的预算，N元器件的种类
    # datas:具体器件的数据  type reliability price

    # 1.不超过预算
    # 2.每种类型元器件都需要购买一个
    # 能够组成的设备的最大可靠性: 所有器件中可靠性最低的器件决定

    rels = set()  # 收集所有器件的可靠性
    kinds = [[] for _ in range(N)]  # 各种器件类列表

    for ty, reliability, price in datas:
        rels.add(reliability)
        device = Device(reliability, price)
        kinds[ty].append(device)

    # 将每个种类内的器件按照可靠性升序
    for kind in kinds:
        kind.sort(key=lambda x: x.reliability)

    # 将所有器件的可靠性集合，变为数组
    maybe = list(rels)
    maybe.sort()

    # ans记录最终答案
    ans = -1
    # 二分选取可能的最大可靠性maybe
    low = 0
    high = len(maybe) - 1
    while low <= high:
        mid = (low + high) // 2

        # 如果maybe[mid]可靠性可以保证所有种类器件都能选到，且价格之和小于s
        if check(kinds, S, maybe[mid]):
            # 则maybe[mid]可靠性就是一个可能解
            ans = maybe[mid]
            # 继续尝试更优解，即找更大的可靠性
            low = mid + 1
        else:
            # 否则，说明可靠性选高了，我们应该继续尝试更低的可靠性
            high = mid - 1

    return ans


if __name__ == '__main__':
    # 获取输入
    # S总的预算，N元器件的种类
    # S, n = map(int, input().split())
    # # total // 元器件的总数，每种型号的元器件可以有多种;
    # total = int(input())
    # datas = []  # total行具体器件的数据
    # for i in range(total):
    #     line = list(map(int, input().split()))
    #     datas.append(line)

    # print(datas)

    S = 500
    N = 3
    total = 6
    datas = [[0, 80, 100], [0, 90, 200], [1, 50, 50], [1, 70, 210], [2, 50, 100], [2, 60, 150]]

    # 调用算法
    print(getResult(datas, S, N))
