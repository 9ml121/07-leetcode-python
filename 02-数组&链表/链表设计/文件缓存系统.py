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
m = int(input())
# 文件操作序列个数n
n = int(input())
# 文件操作序列
ops = [input().split() for _ in range(n)]

# 方法1: 用时间戳模拟每个文件访问时间，时间复杂度较高
# 标准解法参考：
# 03-数组&链表/链表/文件缓存系统2.py
# 03-数组&链表/链表/146. LRU 缓存.py
class FileCache:
    def __init__(self, cap):
        self.cap = cap
        self.used = 0
        self.cache = {}  # name:[访问次数，访问时间,文件大小]
        self.cur_time = 0

    def put(self, name, sz):
        # 存储文件是把文件放入文件缓存系统中
        # 如果新文件的文件名和文件缓存中已有的文件名相同，则不会放在缓存中
        if name not in self.cache:
            # 当缓存空间不足以存放新的文件时，根据规则删除文件，直到剩余空间满足新的文件大小位置，再存放新文件
            # 按照第一优先顺序为访问次数从少到多，第二顺序为时间从老到新的方式来删除文件。
            i = 0
            keys = sorted(self.cache, key=lambda x: (
                self.cache[x][0], self.cache[x][1]))
            while self.cache and self.used + sz > self.cap:
                key = keys[i]
                i += 1
                self.used -= self.cache[key][2]
                self.cache.pop(key)

            # 新的文件第一次存入到文件缓存中时，文件的总访问次数不会变化，文件的最近访问时间会更新到最新时间
            if self.used + sz <= self.cap:
                self.used += sz
                self.cache[name] = [1, self.cur_time, sz]
        # 每次文件访问后，总访问次数加1，最近访问时间更新到最新时间
        self.update(name)

    def get(self, name):
        # 读取文件是从文件缓存系统中访问已存在，如果文件不存在，则不作任何操作。
        if name in self.cache:
            # 文件访问过后，会更新文件的最近访问时间和总的访问次数
            self.update(name)

    def update(self, name):
        if name in self.cache:
            self.cache[name][0] += 1
            self.cache[name][1] = self.cur_time
            self.cur_time += 1


# 输出当前文件缓存中的文件名列表
fc = FileCache(m)
for op in ops:
    if op[0] == 'put':
        fc.put(op[1], int(op[2]))
    else:
        # op == 'get'
        fc.get(op[1])

ans = list(fc.cache.keys())
ans.sort()
print(','.join(ans) if ans else "NONE")
