"""
题目描述
给一个字符串，表示用’,’分开的人名。

然后给定一个字符串，进行快速人名查找，符合要求的输出。

快速人名查找要求︰人名的每个单词的连续前几位能组成给定字符串，一定要用到每个单词。

输入描述
第一行是人名，用’,’分开的人名
第二行是 查找字符串

输出描述
输出满足要求的人名

用例
输入	zhang san,zhang san san
        zs
输出	zhang san
说明	无

输入	zhang san san,zhang an sa,zhang hang,zhang seng,zhang sen a
zhas
输出	zhang an sa,zhang seng
说明	无

"""

# 获取输入
# names = list(input().split(','))
# search = input()
# print(names)

# 测试数据
names = ['zhang san san', 'zhang an sa',
         'zhang hang', 'zhang seng', 'zhang sen a']
search = 'zhas'


def check(parts, parts_idx, search_idx):
    """
    @parts: 人名组成
    @parts_idx:人名被匹配的字符索引位置
    @search_idx：缩写被匹配的字符索引位置
    return: 缩写单词search是否可以匹配当前人名parts
    """
    if search_idx == len(search):
        # 如果缩写被匹配完，且人名组成也匹配到最后一个，则说明当前人名可以匹配对应缩写
        return parts_idx == len(parts)
    
    if parts_idx == len(parts):
        # 如果缩写尚未匹配完，但是人名组成已经匹配完，则说明当前人名无法匹配对应缩写
        return False
    
    part_name = parts[parts_idx]
    for i in range(search_idx, len(search)):
        p = search[search_idx: i+1]
        if part_name.startswith(p):
            if check(parts, parts_idx+1, i+1):
                return True
        else:
            return False

    return False


# 算法
ans = []
for name in names:
    parts = name.split()
    if len(parts) > len(search):
        continue

    if check(parts, 0, 0):
        ans.append(name)

print(','.join(ans))
