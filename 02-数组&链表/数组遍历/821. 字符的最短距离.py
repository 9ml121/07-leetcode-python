"""
给你一个字符串 s 和一个字符 c ，且 c 是 s 中出现过的字符。

返回一个整数数组 answer ，其中 answer.length == s.length 且 answer[i] 是 s 中从下标 i 到离它 最近 的字符 c 的 距离 。

两个下标 i 和 j 之间的 距离 为 abs(i - j) ，其中 abs 是绝对值函数。

 

示例 1：
输入：s = "loveleetcode", c = "e"
输出：[3,2,1,0,1,0,0,1,2,2,1,0]
解释：字符 'e' 出现在下标 3、5、6 和 11 处（下标从 0 开始计数）。
距下标 0 最近的 'e' 出现在下标 3 ，所以距离为 abs(0 - 3) = 3 。
距下标 1 最近的 'e' 出现在下标 3 ，所以距离为 abs(1 - 3) = 2 。
对于下标 4 ，出现在下标 3 和下标 5 处的 'e' 都离它最近，但距离是一样的 abs(4 - 3) == abs(4 - 5) = 1 。
距下标 8 最近的 'e' 出现在下标 6 ，所以距离为 abs(8 - 6) = 2 。


示例 2：
输入：s = "aaab", c = "b"
输出：[3,2,1,0]
 

提示：
1 <= s.length <= 10^4
s[i] 和 c 均为小写英文字母
题目数据保证 c 在 s 中至少出现一次
"""


# todo 方法1：数组正反遍历2次, 贪心思想
# 类似F-贪心算法\135. 分发糖果.py
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        #  answer[i] 是s 中从下标 i 到离它 最近 的字符 c 的 距离 。
        # 1.从左往右遍历s, 查找下标i离他左边最近字符c的距离
        n = len(s)
        ans = [-1] * n
        l = -n
        for i, ch in enumerate(s):
            if ch == c:
                l = i
            ans[i] = i-l
        
        # 2.从右往左遍历s, 查找下标i离他右边最近字符c的距离
        r = 2*n
        for i in range(n-1, -1, -1):
            ch = s[i]
            if ch == c:
                r = i
            ans[i] = min(ans[i], r-i)
        
        return ans



# 方法2：bfs
class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        #  answer[i] 是s 中从下标 i 到离它 最近 的字符 c 的 距离 。
        n = len(s)
        ans = [-1] * n
        q = []

        for i, char in enumerate(s):
            if char == c:
                ans[i] = 0
                q.append(i)

        d = 1
        while q:
            new_q = []
            for i in q:
                if i - 1 >= 0 and ans[i-1] == -1:
                    ans[i-1] = d
                    new_q.append(i-1)
                if i + 1 < n and ans[i+1] == -1:
                    ans[i+1] = d
                    new_q.append(i+1)

            d += 1
            q = new_q
        return ans
