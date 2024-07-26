"""
题目解析和算法源码
https://blog.csdn.net/qfc_128220/article/details/134725034?spm=1001.2014.3001.5501

题目描述
石头剪刀布游戏有 3 种出拳形状：石头、剪刀、布。分别用字母A、B、C表示。

游戏规则：

出拳形状之间的胜负规则如下：

A > B； B > C； C > A；

">" 左边一个字母，表示相对优势形状。右边一个字母，表示相对劣势形状。

当本场次中有且仅有一种出拳形状优于其他出拳形状，则该形状的玩家是胜利者。否则认为是平局。

例如1：三个玩家出拳分别是A，B，C。由于三方优势循环（即没有任何一方优于其他出拳者），判断为平局。

例如2：三个玩家出拳分别是A，B，B。出拳A的获胜。

例如3：三个玩家出拳全部是A。判为平局。

当发生平局，没有赢家。有多个胜利者时，同为赢家。

输入描述
在一场游戏中，每个玩家的信息为一行。玩家数量不超过1000。每个玩家信息有2个字段，用空格隔开；

玩家ID：一个仅由英文字母和数字组成的字符串
出拳形状：以英文大写字母表示，A、B、C形状。
~出拳时间：正整数，越小表示时间越早~
例如：

abc1 A xyz B

解释：玩家abc1出拳为石头（A）。玩家xyz出拳为剪刀（B）

输出描述
输出为赢家的玩家ID列表（一个或多个），每个ID一行，按字符串升序排列。如果没有赢家，输出为”NULL“字符串。

例如：

abc1

用例1
输入
abc1 A
xyz B
输出
abc1
说明
A比B有优势，abc1胜出

用例2
输入
abc1 A
xyz A
输出
NULL
说明
没有优胜的出拳形状，平局

用例3
输入
abc1 A
def A
alic A
xyz B
输出
abc1
alic
def
说明
A为优胜方，有三个赢家
"""

import collections

val_to_names = collections.defaultdict(list)
while True:
    try:
        name, val = input().split()
        val_to_names[val].append(name)
    except:
        break


sz = len(val_to_names)
if sz == 1 or sz == 3:
    print('NULL')
else:
    if 'A' not in val_to_names:
        ans = 'B'
    elif 'B' not in val_to_names:
        ans = 'C'
    else:
        ans = 'A'
    win_names = val_to_names[ans]
    win_names.sort()
    for name in win_names:
        print(name)
