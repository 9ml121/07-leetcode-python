"""
题目解析和算法源码
华为OD机试 - 根据IP查找城市（Java & JS & Python & C & C++）-CSDN博客

题目描述
某业务需要根据终端的IP地址获取该终端归属的城市，可以根据公开的IP地址池信息查询归属城市。

地址池格式如下：

城市名=起始IP,结束IP

起始和结束地址按照英文逗号分隔，多个地址段采用英文分号分隔。比如：

City1=1.1.1.1,1.1.1.2;City1=1.1.1.11,1.1.1.16;City2=3.3.3.3,4.4.4.4;City3=2.2.2.2,6.6.6.6

一个城市可以有多个IP段，比如City1有2个IP段。

城市间也可能存在包含关系，如City3的IP段包含City2的IP段范围。

现在要根据输入的IP列表，返回最佳匹配的城市列表。

注：最佳匹配即包含待查询IP且长度最小的IP段，比如例子中3.4.4.4最佳匹配是City2=3.3.3.3,4.4.4.4，5.5.5.5的最佳匹配是City3=2.2.2.2,6.6.6.6

输入描述
输入共2行。

第一行为城市的IP段列表，多个IP段采用英文分号 ';' 分隔，IP段列表最大不超过500000。城市名称只包含英文字母、数字和下划线。最多不超过100000个。IP段包含关系可能有多层，但不超过100层。

第二行为查询的IP列表，多个IP采用英文逗号 ',' 分隔，最多不超过10000条。

输出描述
最佳匹配的城市名列表，采用英文逗号 ',' 分隔，城市列表长度应该跟查询的IP列表长度一致。

备注
无论是否查到匹配正常都要输出分隔符。举例：假如输入IP列表为IPa,IPb，两个IP均未有匹配城市，此时输出为","，即只有一个逗号分隔符，两个城市均为空；
可以假定用例中的所有输入均合法，IP地址均为合法的ipv4地址，满足 (1~255)​.(0~255)​.(0~255)​​​​​​​​.(0~255​​​​​​​) 的格式，且可以假定用例中不会出现组播和广播地址；
用例1
输入
City1=1.1.1.1,1.1.1.2;City1=1.1.1.11,1.1.1.16;City2=3.3.3.3,4.4.4.4;City3=2.2.2.2,6.6.6.6
1.1.1.15,3.3.3.5,2.2.2.3
输出
City1,City2,City3
说明
1）City1有2个IP段，City3的IP段包含City2的IP段；

2）1.1.1.15仅匹配City1=1.1.1.11,1.1.1.16，所以City1就是最佳匹配；2.2.2.3仅匹配City3=2.2.2.2,6.6.6.6，所以City3是最佳匹配；3.3.3.5同时匹配为City2=3.3.3.3,4.4.4.4和City3=2.2.2.2,6.6.6.6，但是City2=3.3.3.3,4.4.4.4的IP段范围更小，所以City3为最佳匹配；
"""

import re

# 1.获取输入
# 城市的IP段列表. City1=1.1.1.1, 1.1.1.2
ip_arrs = input().split(';')
# 查询的IP列表, 1.1.1.15
ip_searchs = input().split(',')
# print(ip_arrs)
# print(ip_searchs)

# 2.算法
# 1) 将ip地址转换为长整数,并计算每个城市ip段的区间长度
# 参考：05-字符串&整数&哈希/位运算/整数与IP地址间的转换.py
def ip2dec(ip: str):
    # a) 将ip切割为4个ip段，并转换为8位2进制，最后转换为1个10进制整数
    paths = ip.split('.')
    dec = 0
    for path in paths:
        dec = dec << 8 | int(path)
        # print(dec)
    return dec
# print(ip2dec('1.1.1.1'))


class City:
    def __init__(self, name: str, start: str, end: str):
        self.name = name
        self.start = ip2dec(start)
        self.end = ip2dec(end)
        self.lens = self.end - self.start

    def __repr__(self):
        return f'{self.name}({self.start}, {self.end}, {self.lens})'

# 2) 遍历每个查询ip在哪些城市的ip段区间内，并返回最小区间长度的城市，如果没有城市匹配，输出''
def main():
    # a.将ip区间段列表转换为city列表
    citys = []
    for item in ip_arrs:
        tmp = re.split(r'=|,', item)
        # print(tmp)
        city = City(*(tmp))
        # print(city)
        citys.append(city)
    # print(citys)

    # b.遍历查询每个ip属于那个城市
    ans = []
    for ip in ip_searchs:
        dec = ip2dec(ip)
        name = ''
        min_lens = float('inf')
        for city in citys:
            if city.start <= dec <= city.end and city.lens < min_lens:
                name = city.name
                min_lens = city.lens

        ans.append(name)
    # print(ans)
    return ','.join(ans)


print(main())
