"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/135024413?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22135024413%22%2C%22source%22%3A%22qfc_128220%22%7D

OJ用例
题解 - 文件缓存系统 - Hydro

题目描述
请设计一个文件缓存系统，该文件缓存系统可以指定缓存的最大值（单位为字节）。

文件缓存系统有两种操作：

存储文件（put）
读取文件（get）
操作命令为：

put fileName fileSize
get fileName
存储文件是把文件放入文件缓存系统中；

读取文件是从文件缓存系统中访问已存在，如果文件不存在，则不作任何操作。

当缓存空间不足以存放新的文件时，根据规则删除文件，直到剩余空间满足新的文件大小位置，再存放新文件。

具体的删除规则为：

文件访问过后，会更新文件的最近访问时间和总的访问次数，当缓存不够时，按照第一优先顺序为访问次数从少到多，第二顺序为时间从老到新的方式来删除文件。

输入描述
第一行为缓存最大值 m（整数，取值范围为 0 < m ≤ 52428800）

第二行为文件操作序列个数 n（0 ≤ n ≤ 300000）

从第三行起为文件操作序列，每个序列单独一行，文件操作定义为：

op file_name file_size

file_name 是文件名，file_size 是文件大小

输出描述
输出当前文件缓存中的文件名列表，文件名用英文逗号分隔，按字典顺序排序，如：

a,c

如果文件缓存中没有文件，则输出NONE

备注
如果新文件的文件名和文件缓存中已有的文件名相同，则不会放在缓存中
新的文件第一次存入到文件缓存中时，文件的总访问次数不会变化，文件的最近访问时间会更新到最新时间
每次文件访问后，总访问次数加1，最近访问时间更新到最新时间
任何两个文件的最近访问时间不会重复
文件名不会为空，均为小写字母，最大长度为10
缓存空间不足时，不能存放新文件
每个文件大小都是大于 0 的整数
用例1
输入
50
6
put a 10
put b 20
get a
get a
get b
put c 30
输出
a,c
用例2
输入
50
1
get file
输出
NONE
"""


# 输入
# 缓存最大数m
import collections


m = int(input())
# 文件操作序列个数n
n = int(input())
# 文件操作序列
ops = [input().split() for _ in range(n)]


# 方法1：使用字典 + 整形时间戳代替双向链表， 数据量过大会有测试用例不能通过
class FileCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}  # name:[访问次数，访问时间,文件大小]
        self.cur_time = 0

    def put(self, name, sz):
        # 存储文件是把文件放入文件缓存系统中
        # 如果新文件的文件名和文件缓存中已有的文件名相同，则不会放在缓存中
        if name in self.cache:
            return
        
        # 当缓存空间不足以存放新的文件时，根据规则删除文件，直到剩余空间满足新的文件大小位置，再存放新文件
        # 按照第一优先顺序为访问次数从少到多，第二顺序为时间从老到新的方式来删除文件。
        i = 0
        keys = sorted(self.cache, key=lambda x: (self.cache[x][0], self.cache[x][1]))
        while i < len(keys) and self.cap < sz:
            remove_key = keys[i]
            i += 1
            self.cap += self.cache[remove_key][2]
            self.cache.pop(remove_key)

        # 新的文件第一次存入到文件缓存中时，文件的总访问次数不会变化，文件的最近访问时间会更新到最新时间
        if self.cap >= sz:
            self.cap -= sz
            self.cache[name] = [1, self.cur_time, sz]
    

    def get(self, name):
        # 读取文件是从文件缓存系统中访问已存在，如果文件不存在，则不作任何操作。
        if name not in self.cache:
            return
        
        # 文件访问过后，会更新文件的最近访问时间和总的访问次数
        self.update(name)

    def update(self, name):
        if name in self.cache:
            self.cache[name][0] += 1
            self.cache[name][1] = self.cur_time
            self.cur_time += 1


# 输出当前文件缓存中的文件名列表
def main1():
    fc = FileCache(m)
    for op in ops:
        if op[0] == 'put':
            fc.put(op[1], int(op[2]))
        else:
            # op == 'get'
            fc.get(op[1])

    ans = fc.cache.keys()
    print(','.join(ans) if ans else "NONE")


# 方法2：设计双向链表，参考“03-数组&链表\链表\146. LRU 缓存.py”
# 使用有序字典代表双向链表
class LRUCache:
    def __init__(self, cap: int):
        # 文件系统剩余可用容量
        self.cap = cap 
        # cache中的key表示缓存系统中存在的文件名, value代表该文件的访问次数
        self.cache = collections.defaultdict(int)  
        # freq_to_node中的key是访问次数，value是一个有序字典（存储相同访问次数的文件名）
        self.freq_to_node = collections.defaultdict(collections.OrderedDict)
        # 最小访问次数
        self.min_freq = 0

    def get(self, key: int) -> None:
        # 如果文件不存在，则不作任何操作
        if key not in self.cache:
            return 
        
        # 如果键key存在于cache，
        # 1. 先删除freq_to_node中该访问次数中有序字典中key节点（调用有序字典pop方法）
        freq = self.cache[key] 
        self.freq_to_node[freq].pop(key)
        # 2. 如果删除之后，该访问次数没有节点，需要判断是否要更新min_freq
        if not self.freq_to_node[freq]:
            if freq == self.min_freq:
                self.min_freq += 1
            self.freq_to_node.pop(freq)
        # 3.最后将该节点增加到freq_to_node中访问次数为freq+1的有序字典中
        self.freq_to_node[freq+1].
       
        # 先增加该节点访问次数
        self.freq_to_node
        self.freq_of_key[key] += 1

    def put(self, key: int, val: int) -> None:
        # 如果新文件的文件名和文件缓存中已有的文件名相同，则不会放在缓存中
        # 这种情况不需要调用move_to_end方法将节点移动到链表末尾，并增加该节点访问次数
        if key in self.cache:
            return

        # 当缓存空间不足以存放新的文件时，根据规则删除文件，直到剩余空间满足新的文件大小位置，再存放新文件
        # 按照第一优先顺序为访问次数从少到多，第二顺序为时间从老到新的方式来删除文件。
        while self.cap < val and self.cache:
            # 1.调用有序字典popitem方法，删除最早的节点FIFO
            self.cache.popitem(last=False)
        self.cache[key] = val  # 更新节点值,或者添加节点到链表末尾

        if len(self.cache) > self.cap:  # 判断链表是否已满
            self.cache.popitem(last=False)  # 删除链表头部节点
