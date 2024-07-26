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

# 方法2: 利用orderDict(双向链表)维护文件访问fifo
import collections


class FileCache:
    def __init__(self, cap) -> None:
        self.cap = cap
        # {key: freq}
        self.cache = collections.defaultdict(int)
        self.min_freq = 0
        # {freq: {key: val}}
        self.freq_links = collections.defaultdict(collections.OrderedDict)

    def get(self, key):
        if key not in self.cache:
            return

        # 在缓存中，需要更新lfu和访问次数
        # 1. 先删除原来访问次数links中的key
        orig_freq = self.cache[key]
        links = self.freq_links[orig_freq]
        val = links.pop(key)
        #   注意：这里删除完key，还需要判断是否更新min_freq
        if not links:
            if orig_freq == self.min_freq:
                self.min_freq += 1
            self.freq_links.pop(orig_freq)
        # 2. 在原来访问次数+1的links中添加key
        new_links = self.freq_links[orig_freq+1]
        new_links[key] = val
        # 3. cache中访问次数+1
        self.cache[key] += 1

    def put(self, key, val):
        if key in self.cache:
            return

        while self.cap < val and self.cache:
            # 按照freq 和 fifo 删除
            links = self.freq_links[self.min_freq]
            if links:
                k, v = links.popitem(last=False)  # fifo
                self.cap += v
                self.cache.pop(k)
            else:
                self.freq_links.pop(self.min_freq)
                self.min_freq += 1

        # 首次添加文件，访问次数为1, 分别更新min_freq， cache, freq_links
        if self.cap >= val:
            self.cap -= val
            self.min_freq = 1
            self.cache[key] = 1
            self.freq_links[1][key] = val

# 输入
# cap = int(input())
# n = int(input())
# cmds = [input().split() for _ in range(n)]

# 测试用例：
cap = 50
cmds = [['put', 'a', '10'], ['put', 'b', '20'], ['get', 'a'], [
    'get', 'a'], ['get', 'b'], ['get', 'b'], ['put', 'c', '30']]

fc = FileCache(cap)
for cmd in cmds:
    op = cmd[0]
    key = cmd[1]
    if op == 'put':
        val = cmd[2]
        fc.put(key, int(val))
    else:
        fc.get(key)

# 按字典顺序排序
ans = list(fc.cache.keys())
ans.sort()
print(','.join(ans) if ans else 'NONE')