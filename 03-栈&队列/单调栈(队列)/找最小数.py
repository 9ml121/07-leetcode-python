"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/127342038

题目描述
给一个正整数NUM1，计算出新正整数NUM2，NUM2为NUM1中移除N位数字后的结果，需要使得NUM2的值最小。

输入描述
输入的第一行为一个字符串，字符串由0-9字符组成，记录正整数NUM1，NUM1长度小于32。
输入的第二行为需要移除的数字的个数，小于NUM1长度。
输出描述
输出一个数字字符串，记录最小值NUM2。

用例1
输入
2615371
4
输出
131
"""

# todo 考察单调栈 + 贪心， 类似 04-栈&队列\栈\单调栈(队列)\402. 移掉 K 位数字.py
# 输入
# num1 = input()
# k = int(input()) # 移除k位数

# 测试数据
num1 = '2615137'
num1 = '2015137'
k = 4

# 输出：移除之后的数字最小值
# todo st非严格单调递增， 维护留下来的数字, 保证移除k位之后的数字最小
st = []
for c in num1:
    while st and c < st[-1] and k > 0:
        st.pop()
        k -= 1
    st.append(c)

# num1本来就单调递增，比如num=122，k=1, 那就移除最后k位数
while k > 0 and st:
    st.pop()
    k -= 1

ans = ''.join(st)
print(int(ans))
