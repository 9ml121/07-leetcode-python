"""
题目描述：
小王设计了一个简单的猜字谜游戏，游戏的谜面是一个错误的单词，比如nesw，玩家需要猜出谜底库中正确的单词。猜中的要求如下：
    对于某个谜面和谜底单词，满足下面任一条件都表示猜中：
        1）变换顺序以后一样的，比如通过变换w和e的顺序，“nwes”跟“news”是可以完全对应的；
        2）字母去重以后是一样的，比如“woood”和“wood”是一样的，它们去重后都是“wod”

请你写一个程序帮忙在谜底库中找到正确的谜底。谜面是多个单词，都需要找到对应的谜底，如果找不到的话，返回"not found"

输入描述：
1、谜面单词列表，以","分隔
2、谜底库单词列表，以","分隔

输出描述：
匹配到的正确单词列表，以“,”分隔
如果找不到，返回"not found"
补充说明：
1、单词的数量N的范围：0 < n < 1000
2、词汇表的数量M的范围： 0 < M < 1000
3、单词的长度P的范围：0 < P < 20
4、输入的字符只有小写英文字母，没有其它字符

示例1
输入：
conection
connection,today
输出：
connection

示例2
输入：
bdni,wooood
bind,wrong,wood
输出：
bind,wood

"""

# 1）变换顺序以后一样的，比如通过变换w和e的顺序，“nwes”跟“news”是可以完全对应的；
# 2）字母去重以后是一样的，比如“woood”和“wood”是一样的，它们去重后都是“wod”

# s1 = input().split(',')
# s2 = input().split(',')
questions = ['bdni', 'wooood', 'aa']
answers = ['bind', 'wrong', 'wood']


# 用set去重，sort排序
def convert(s: str):
    return ''.join(sorted(set(s)))


dic = {}
for ans in answers:
    dic[convert(ans)] = ans

res = []
for q in questions:
    res.append(dic.get(convert(q), 'not found'))

print(','.join(res))
