"""
给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
返回一个表示每个字符串片段的长度的列表。



示例 1：
输入：s = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
示例 2：

输入：s = "eccbbbbdec"
输出：[10]


提示：

1 <= s.n <= 500
s 仅由小写英文字母组成
"""
from typing import List

'''
思路：
1.问题的本质是先要知道每个字符在s中的最后索引位置，因为划分的每个子字符串之间是没有重复字母的
2.第一个子字符串开始位置是S第一位，结束位置呢？ 是这个字符串里每个字符在S中的最后索引的最大值
方法：
1. 遍历s,将s中每个字符和最后索引存进dic
2. 再遍历s,start_index默认为0，在dict查找s每个字符的最后索引的最大值last_index，
   当i == last_index,说明已经到了第一个符合要求的子字符串结束位置，将长度存进res
3. 再更新start_index = last_index + 1,重复上一步操作
4. 将所有结果存进结果表
'''


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        char_idxs = {c:i for i,c in enumerate(s)}
        res = []
        start_index = 0
        last_index = 0

        for i in range(len(s)):
            last_index = max(char_idxs[s[i]], last_index)
            if i == last_index:
                res.append(last_index - start_index + 1)
                # 重置start
                start_index = last_index + 1
        return res


cls = Solution()
# s = "eaaaabaaec"
# s = "ababcbacadefegdehijhklij"
# s = "eccbbbbdec"
s = "qiejxqfnqceocmy"  # [11,1,1,1,1] [13,1,1]
print(cls.partitionLabels(s))
