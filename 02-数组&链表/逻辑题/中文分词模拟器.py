"""
题目描述
给定一个连续不包含空格的字符串，该字符串仅包含英文小写字母及英文标点符号（逗号、分号、句号），同时给定词库，对该字符串进行精确分词。

说明：

精确分词：字符串分词后，不会出现重叠。即"ilovechina"，不同词库可分割为"i,love,china"，"ilove,china"，不能分割出现重叠的"i,ilove,china"，i 出现重叠
标点符号不成词，仅用于断句
词库：根据外部知识库统计出来的常用词汇例：dictionary = ["i", "love", "china", "lovechina", "ilove"]
分词原则：采用分词顺序优先且最长匹配原则

"ilovechina"，假设分词结果 [i,ilove,lo,love,ch,china,lovechina]，则输出 [ilove,china]

错误输出：[i,lovechina]，原因："ilove" > 优先于 "lovechina" 成词

错误输出：[i,love,china]，原因："ilove" > "i"遵循最长匹配原则
输入描述
第一行输入待分词语句 "ilovechina"

字符串长度限制：0 < length < 256
第二行输入中文词库 "i,love,china,ch,na,ve,lo,this,is,this,word"

词库长度限制：1 < length < 100000
输出描述
按顺序输出分词结果 "i,love,china"

用例
输入	ilovechina
i,love,china,ch,na,ve,lo,this,is,the,word
输出	i,love,china
说明	无
输入	iat
i,love,china,ch,na,ve,lo,this,is,the,word,beauti,tiful,ful
输出	i,a,t
说明	
单个字母，

不在词库中且不成词则输出单个字母

输入	ilovechina,thewordisbeautiful
i,love,china,ch,na,ve,lo,this,is,the,word,beauti,tiful,ful
输出	i,love,china the,word,is,beauti,ful
说明	标点符号为英文标点符号
"""

import re
import collections

# 输入
# 第一行输入待分词语句 0 < length < 256
sentences = re.split(r'[,;.]', input())
# 第二行输入中文词库，1 < length < 100000
words_dict = re.split(r'[,;.]', input())
# print(sentences, words_dict)


# 输出：按顺序输出分词结果
# 遍历待分词语句的切割语句，按照分词顺序优先且最长匹配原则在词库查找
dq = collections.deque(sentences)
words_set = set(words_dict)
ans = []
while dq:
    s = dq.popleft()
    if not s:
        # 测试用例：have.
        continue

    i = len(s)
    # 按照s从后向前遍历，查找i之前的单词是否在词库存在
    while i > 0:
        word = s[:i]
        # 如果存在，加入到ans,并将i之后的单词添加到dq
        # 根据测试用例，词库中的词不能重复用！
        if word in words_set:
            ans.append(word)
            words_set.remove(word)
            if i < len(s):
                dq.appendleft(s[i:])
            break
        i -= 1

    # 如果不存在，则不在词库中且不成词则输出单个字母
    if i == 0:
        ans.append(s[0])
        if len(s) > 1:
            dq.appendleft(s[1:])
print(','.join(ans))
