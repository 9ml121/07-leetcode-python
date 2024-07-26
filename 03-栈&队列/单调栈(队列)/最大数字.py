"""
题目描述
给定一个由纯数字组成以字符串表示的数值，现要求字符串中的每个数字最多只能出现2次，超过的需要进行删除；
删除某个重复的数字后，其它数字相对位置保持不变。

如”34533″，数字3重复超过2次，需要删除其中一个3，删除第一个3后获得最大数值”4533″

请返回经过删除操作后的最大的数值，以字符串表示。

输入描述
第一行为一个纯数字组成的字符串，长度范围：[1,100000]

输出描述
输出经过删除操作后的最大的数值

用例
输入	34533
输出	4533
说明	无

输入	5445795045
输出	5479504
说明	无
"""

# todo 单调栈 + 计数器， 单调栈来维护去除「关键字符」后得到的字符串， 计数器用来统计使用数字个数
# 类似：04-栈&队列\单调栈(队列)\316. 去除重复字母.py

'''
题目要求：
1。要求字符串中的每个数字最多只能出现2次，超过的需要进行删除；
2。删除某个重复的数字后，其它数字相对位置保持不变。
问： 请返回经过删除操作后的最大的数值

分析思路：
1。对于要求1，可以用一个字典记录每个数字出现的次数，超过2的要删除多余的。比如有3个5，那该删除哪个位置上的5呢？
2。题目问的是删除之后的最大值，删除规则如下: 
    a) 比如3535754，结果是要删除第二个5，判断依据呢？ 
        因为第一个5后面的数字比5小，第二个5后面数字比5大。
        
    b) 那如果数字是3535450，结果是删除最后一个5，判断依据呢？
        也就是前面2个5如果根据a)的判断都保留了，那后面出现的5必须都要删除
3. 对于要求2，删除之后其他数字相对位置不变。要满足这个要求，只能用数组/栈来记录保留下来的数字

根据以上分析思路，开始写代码
'''

import collections
def getResult(s: str):
    # st存储最后的结果, 要求是经过删除操作后的最大的数值
    st = []

    # canUse记录s剩余数字的可用个数
    canUse = collections.Counter(s)
    # keep记录st中已使用的数字个数
    keep = collections.Counter()

    for c in s:
        # 处理b删除逻辑：数字是535450，结果是删除最后一个5
        # 如果前面该字符已经保留了2个了，则后续再出现该数字字符不保留
        if keep[c] == 2:
            canUse[c] -= 1
            continue

        # 处理a删除逻辑: 数字是535754，结果是要删除第二个5
        # 1.canUse[st[-1]] + keep[st[-1]] > 2 代表栈顶元素top是需要删除的元素
        # 2.如果栈顶元素的后面数字c比它大，可以立刻删除top，来保证删除之后的数字最大
        while st and canUse[st[-1]] + keep[st[-1]] > 2 and st[-1] < c:
            top = st.pop()
            keep[top] -= 1

        st.append(c)
        canUse[c] -= 1
        keep[c] += 1

    return ''.join(st)





if __name__ == '__main__':
    # 1.输入获取
    s = '5676755478'  # 6755678
    # s = '5445795045'  # 5479504
    print(getResult(s))
