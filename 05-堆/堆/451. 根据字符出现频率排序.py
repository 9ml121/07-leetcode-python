"""
给定一个字符串 s ，根据字符出现的 频率 对其进行 降序排序 。一个字符出现的 频率 是它出现在字符串中的次数。

返回 已排序的字符串 。如果有多个答案，返回其中任何一个。



示例 1:

输入: s = "tree"
输出: "eert"
解释: 'e'出现两次，'r'和't'都只出现一次。
因此'e'必须出现在'r'和't'之前。此外，"eetr"也是一个有效的答案。
示例 2:

输入: s = "cccaaa"
输出: "cccaaa"
解释: 'c'和'a'都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。
示例 3:

输入: s = "Aabb"
输出: "bbAa"
解释: 此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意'A'和'a'被认为是两种不同的字符。


提示:

1 <= s.length <= 5 * 105
s 由大小写英文字母和数字组成
"""
import collections
import heapq


# 方法1：调用counter对象的most_common方法
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        freqSortList = counter.most_common()
        res = ''
        for key, freq in freqSortList:
            res += key * freq
        return res

    def frequencySort2(self, s: str) -> str:
        return ''.join([char * freq for char, freq in collections.Counter(s).most_common()])


"""
除了使用Counter和列表推导式的解法外，还可以使用堆排序的方法来解决这个问题。 
 
堆排序的思路是首先使用Counter统计字符串中每个字符的频率，然后将字符和频率存储在一个最大堆中。
然后依次从堆中取出频率最大的字符，并将其重复频率次数拼接到结果字符串中。
"""

# 方法2：堆排序
class Solution2:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)

        max_heap = [(-freq, key) for key, freq in counter.items()]

        heapq.heapify(max_heap)
        res = ''
        while max_heap:
            freq, key = heapq.heappop(max_heap)
            res += key * (-freq)
        return res


# 方法3：桶排序
class Solution3:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        max_freq = max(counter.values())
        buckets = [[] for _ in range(max_freq + 1)]
        for key, freq in counter.items():
            buckets[freq].append(key)
        res = ''
        for freq in range(max_freq, 0, -1):
            for key in buckets[freq]:
                res += key * freq
        return res
