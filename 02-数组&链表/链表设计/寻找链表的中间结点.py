"""
题目来源：https://fcqian.blog.csdn.net/article/details/128049270
题目描述：
给定一个单链表 L，请编写程序输出 L 中间结点保存的数据。如果有两个中间结点，则输出第二个中间结点保存的数据。
例如：给定 L 为 1→7→5，则输出应该为 7；给定 L 为 1→2→3→4，则输出应该为 3。

输入描述：
每个输入包含 1 个测试用例。每个测试用例第 1 行给出链表首结点的地址、结点总个数正整数 n (≤105)。
结点的地址是 5 位非负整数，NULL 地址用 −1 表示。

接下来有 n 行，每行格式为：
Address Data Next
其中 Address 是结点地址，Data 是该结点保存的整数数据(0 ≤ Data ≤ 108)，Next 是下一结点的地址。

输出描述：
对每个测试用例，在一行中输出 L 中间结点保存的数据。如果有两个中间结点，则输出第二个中间结点保存的数据。

补充说明：
已确保输入的结点所构成的链表 L 不会成环，但会存在部分输入结点不属于链表 L 情况 。

示例1
输入：
    00100 4
    00000 4 -1
    00100 1 12309
    33218 3 00000
    12309 2 33218
输出：
3
说明：

示例2
输入：
    10000 3
    76892 7 12309
    12309 5 -1
    10000 1 76892
输出：
7
说明：
"""
# 1.获取输入
line1 = input().split()
head = line1[0]
n = int(line1[1])

dic = {}
for i in range(n):
    addr, data, next = input().split()
    dic[addr] = (data, next)
# print(dic)
# head = '10000'
# n = 3
# dic = {'76892': ('7', '12309'), '12309': ('5', '-1'), '10000': ('1', '76892')}

# 2.获取结果
linkedlist = []
nextNode = head
while nextNode != '-1' and nextNode:
    val, nextNode = dic.get(nextNode)
    linkedlist.append(val)
print(linkedlist)

mid = len(linkedlist) // 2
ans = linkedlist[mid]
print(ans)
