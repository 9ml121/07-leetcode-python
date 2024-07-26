"""
题目来源
https://www.nowcoder.com/practice/66ca0e28f90c42a196afd78cc9c496ea?tpId=37&tags=&title=&difficulty=&judgeStatus=&rp=1&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D37%26type%3D37&gioEnter=menu

题目描述
原理：ip地址的每段可以看成是一个0-255的整数，把每段拆分成一个二进制形式组合起来，然后把这个二进制数转变成一个长整数。


举例：一个ip地址为10.0.3.193

每段数字	相对应的二进制数
10	00001010
0	00000000
3	00000011
193	11000001
组合起来即为：00001010 00000000 00000011 11000001,

转换为10进制数就是：167773121，

即该IP地址转换后的数字就是它了。

数据范围：保证输入的是合法的 IP 序列

输入描述
输入IP地址
输入10进制型的IP地址

输出描述
输出转换成10进制的IP地址
输出转换后的IP地址

用例
输入：
10.0.3.193
167969729

输出：
167773121
10.3.3.193
"""


# 输入
# 输入IP地址
# ip = input()
# 输入10进制型的IP地址
# dec = input()

# 测试数据
ip = '10.0.3.193'  # 167773121
dec = '167969729'  # 10.3.3.193

# todo 输出ip地址和代表的整数互相转换的结果
# ip地址转换为整数，写法1
def ip2dec(ip):
    # 1.将ip地址切分4段，转换为1个32位的二进制字符串
    arr = ip.split('.')
    bin_s = ''
    for item in arr:
        ip = bin(int(item))[2:]
        # s最多8位，不足8位补充左侧为0到8位
        ip = ip.rjust(8, '0')
        bin_s += ip

    # 2.将32位二进制字符串转换位10进制整数
    return int(bin_s, 2)


print(ip2dec(ip))


# ip地址转换为整数，写法2
def ip2dec2(ip:str):
    arr = ip.split('.')
    # todo 将4个ip地址段按照位移运算 << 和 或操作 | 转换为1个10进制整数
    ans = 0
    for item in arr:
        ans = ans << 8 | int(item)

    return ans


print(ip2dec2(ip))

# dec = '167969729' => 10.3.3.193
# 整数转换为ip地址
def dec2ip(dec:str):
    # 1.将长整数转换为32位二进制字符串
    bin_s = bin(int(dec))[2:]
    # print(bin_s)
    bin_s = bin_s.rjust(32, '0')
    # print(bin_s)
    
    # 2.将32位二进制切割为4个8位二进制字符串，再转换为10进制整数
    paths = []
    for i in range(0, 32, 8):
        path = bin_s[i:i+8]
        path = int(path, 2)
        paths.append(path)
    
    return '.'.join(map(str, paths))
print(dec2ip(dec))


    