"""
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。
s 中使用至少一个空格将字符串中的 单词 分隔开。

返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。

注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。
返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

示例 1：
输入：s = "the sky is blue"
输出："blue is sky the"

示例 2：
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。

示例 3：
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。


提示：
1 <= s.length <= 10^4
s 包含英文大小写字母、数字和空格 ' '
s 中 至少存在一个 单词


进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。
"""
import collections
# todo 方法 3：原地反转所有单词的顺序(推荐！)
# 要反转字符串中的单词，一种常见的方法是先将整个字符串翻转，然后再对每个单词进行翻转。
# python中 str是不可变数据类型，需要将 str转换为列表，因此空间复杂度：O(N)


class Solution3:
    def reverseWords(self, s: str) -> str:
        # 实现内置 reversed()函数
        def reversedStr(s: str):
            # 将字符串转换为列表
            strList = list(s)
            left, right = 0, len(strList) - 1

            # 双指针翻转字符串
            while left < right:
                strList[left], strList[right] = strList[right], strList[left]
                left += 1
                right -= 1

            # 将列表转换为字符串
            return ''.join(strList)

        # 1.首先，将整个字符串进行翻转，得到一个翻转后的字符串。
        s = reversedStr(s)

        # 2.对每个单词进行翻转
        word_start, word_end = 0, 0
        res = []
        while word_start < len(s):
            if s[word_start] == " ":
                word_start += 1
                word_end += 1
            elif word_end == len(s) or s[word_end] == " ":
                res.append(reversedStr(s[word_start:word_end]))
                word_start = word_end + 1
                word_end = word_start
            else:
                word_end += 1

        return ' '.join(res)


# 方法 1：调用 split(), reversed()函数
# 时间复杂度 O(N)，空间复杂度 O(N)
class Solution:
    def reverseWords(self, s: str) -> str:
        # 注意：split() 方法将单词间的 “多个空格看作一个空格” ，因此不会出现多余的 “空单词”
        # 参考自 split()和split(' ')的区别
        return " ".join(reversed(s.split()))


# 方法 2：双向队列 + 双指针解法，相当于自己实现 reversed()函数
# 时间复杂度 O(N)，空间复杂度 O(N)
class Solution2:
    def reverseWords(self, s: str) -> str:
        left = 0
        right = len(s) - 1

        # 去除两边空格，相当于自己实现 s.strip()函数
        while left <= right and s[left] == " ":
            left += 1

        while left <= right and s[right] == " ":
            right -= 1

        # 利用双向队列实现内置 reversed() 和 s.split() 函数功能
        dq = collections.deque()
        word = []
        while left <= right:
            if s[left] != " ":
                word.append(s[left])
            if s[left] == " " and word:
                dq.appendleft(''.join(word))
                word = []
            left += 1
        dq.appendleft(''.join(word))  # 加入最后一个单词

        return ' '.join(dq)




if __name__ == '__main__':
    s = "a good   example"  # example good a
    print(Solution3().reverseWords(s))

