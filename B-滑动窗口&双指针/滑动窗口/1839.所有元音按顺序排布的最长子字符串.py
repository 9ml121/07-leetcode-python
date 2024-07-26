"""
当一个字符串满足如下条件时，我们称它是 美丽的 ：
1.所有 5 个英文元音字母（'a' ，'e' ，'i' ，'o' ，'u'）都必须 至少 出现一次。
2.这些元音字母的顺序都必须按照 字典序 升序排布（也就是说所有的 'a' 都在 'e' 前面，所有的 'e' 都在 'i' 前面，以此类推）
比方说，字符串 "aeiou" 和 "aaaaaaeiiiioou" 都是 美丽的 ，但是 "uaeio" ，"aeoiu" 和 "aaaeeeooo" 不是美丽的 。

限定条件
1.给你一个只包含英文元音字母的字符串 word ，请你返回 word 中 最长美丽子字符串的长度 。如果不存在这样的子字符串，请返回 0 。
2。子字符串 是字符串中一个连续的字符序列。

输入：word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
输出：13
解释：最长子字符串是 "aaaaeiiiiouuu" ，长度为 13 。

输入：word = "aeeeiiiioooauuuaeiou"
输出：5
解释：最长子字符串是 "aeiou" ，长度为 5 。

输入：word = "a"
输出：0
解释：没有美丽子字符串，所以返回 0 。
"""


# 关键条件
# 1.所有 5 个英文元音字母（'a', 'e', 'i', 'o', 'u'）都必须 至少 出现一次
# 2.这些元音字母的顺序都必须按照 字典序 升序排布（也就是说所有的 'a' 都在 'e' 前面，所有的 'e' 都在 'i' 前面，以此类推）
# 3.word只包含这5个元音字母

# 解法1：不用元音判断，直接通过比大小解题（O(n)）
class Solution2:
    def longestBeautifulSubstring(self, word: str) -> int:
        '''
        # 不用元音判断，直接通过比大小解题 a < e < i < o < u
        1.首先如果数组长度小于5的话，不可能满足美丽的定义，将这种情况提前排除
        2.遍历时分了几种情况判断：
            - 如果当前字符比上一个不小（顺序意义），那么当前子串长度+1
            - 如果当前字符比上一个大，那么子串中元音字母种类+1
            - 如果当前字符比上一个小，那么肯定当前字串不美丽，以当前字符为首继续进行遍历
        3.如果当前子字符串没有以a开头的话，那么在进行下一个子字符串开始遍历之前，元音种类一定不会达到5，所以只要判断种类即可
        4.当元音种类为5的时候，持续维护更新最终结果，取出最大值即可
        '''
        sub_len = 1  # 当前子串长度
        cnt = 1  # 子串中元音字母种类
        mx = 0  # 符合要求的最长字串长度
        for i in range(1, len(word)):
            if word[i] >= word[i - 1]:
                sub_len += 1
            if word[i] > word[i - 1]:
                cnt += 1
            if word[i] < word[i - 1]:
                sub_len = 1
                cnt = 1
            if cnt == 5 and sub_len > mx:
                # aeiouu
                mx = sub_len

        return mx


# 解法2：双指针 + 滑动窗口
'''
解题思路
这种求满足某种条件的子字符串问题，是典型的滑动窗口套路题了。

这种题的思路一般是设置一个滑动窗口，每次试探地将元素从右侧加入窗口，
如果满足条件则顺利加入；
如果遇到的元素加入后使得条件变得不满足，那么试图从左侧移除元素，直到条件满足。

在窗口滑动的过程中，右指针和左指针的移动分别有如下规律：
右指针
right++ 即只向右移动一个位置，每次试探一个新元素。
左指针
left++ 向右移动一个位置
left=right 即清空窗口中所有元素
left移到窗口中某个合适位置（比如刚好使得窗口中没有重复元素-lC003题）

本题中窗口要满足的条件即元素按字典序排列和5个元音字母必须全部出现，
对于第一个条件只需要比较新元素和窗口中元素的字典序即可，
对于第二个条件我们使用一个hash set来统计窗口中字符的种类。
'''


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        i = 0
        j = 0
        arr = set()  # 统计窗口中字符的种类
        window = []  # 统计每次右移窗口中的元素
        mx = 0  # 满足条件的最大子序列长度
        while j < len(word):
            # 2。判断右指针右移的结果，如果符合条件，窗口右扩
            if not window or word[j] >= window[-1]:
                arr.add(word[j])
                window.append(word[j])
                # 3。满足条件，记录答案
                if len(arr) == 5 and len(window) > mx:
                    mx = len(window)
            # 4。如果不符合条件，窗口左侧收缩
            else:
                i = j
                arr.clear()
                window.clear()
                arr.add(word[i])
                window.append(word[i])
            # 1。右指针每次只向右移动一个位置，试探一个新元素
            j += 1

        return mx


# 测试
cls = Solution()
# s = 'aeiou'
s = 'aeiueaeiouuu'
# s = 'aaaaaaeiiiioou'
# s = '"aeeeiiiioooauuuaeiou"'
cls.longestBeautifulSubstring(s)


# 方法三：状态机
class Solution3:
    """
    1.我们可以将a,e,i,o,u 看成 5个状态。
        当我们在遍历字符串的每个字符时，都会处于其中的一个状态。
        如果当前在 u 状态，那么就可以对答案进行更新。
    2.下面给出了状态转移图，其中蓝色的 a,e,i,o 表示正常状态，绿色的 u 表示目标状态，红色的 x 表示非法状态。
    3.图中也标注了两个状态之间的转移方式，对于没有标注的转移，一律转移到 x 非法状态。
        这样一来，我们只需要从 x 状态开始，在对字符串进行一次遍历的同时，在状态机上进行转移即可。
        在转移的同时，我们需要记录到目前为止成功转移的次数 cnt，当到达 u状态时，我们就可以用 cnt来更新答案。
    4.转移次数 cnt  的计算规则如下：
        当我们转移到 x状态时，会将 cnt 清零；
        当我们转移到 a 状态时，如果上一个状态不为 a，那么会将 cnt 置为 111；
        对于其余的情况，将 cnt 增加 1 即可。
    """
    TRANSIT = {
        ("a", "e"), ("e", "i"), ("i", "o"), ("o", "u"),
        ("a", "a"), ("e", "e"), ("i", "i"), ("o", "o"), ("u", "u"),
        ("x", "a"), ("e", "a"), ("i", "a"), ("o", "a"), ("u", "a"),
    }

    def longestBeautifulSubstring(self, word: str) -> int:
        cur, ans = 0, 0
        status = "x"

        for ch in word:
            if (status, ch) in Solution.TRANSIT:
                if status != "a" and ch == "a":
                    cur = 1
                else:
                    cur = cur + 1
                status = ch
            else:
                cur = 0
                status = "x"
            if status == "u":
                ans = max(ans, cur)

        # return ans
        print(ans)


# 测试
cls = Solution()
# s = 'a'
# s = 'aeiou'
# s = "aeiuo"
s = "aeioueaaeiou"
cls.longestBeautifulSubstring(s)