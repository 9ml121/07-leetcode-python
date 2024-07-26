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

from typing import List


# 方法1：快速排序
class Solution:
    def frequencySort(self, s: str) -> str:
        # 计算字符频率
        counter = collections.Counter(s)
        # 将counter对象转换为包含字符和频率二元元祖的列表
        char_to_freq = [(char, freq) for char, freq in counter.items()]
        # 对字符频率列表进行快速排序(非原地排序)
        sorted_freq = self.quick_sort(char_to_freq)
        # 构建排序之后的字符串
        sorted_str = ''
        for char, freq in sorted_freq:
            sorted_str += char * freq
        return sorted_str

    # 定义快速排序函数
    def quick_sort(self, arr: List[tuple[str, int]]) -> List[tuple[str, int]]:
        n = len(arr)
        if n <= 1:
            return arr
        pivot = arr[n // 2][1]  # 基准值选择中间的元素
        gt = [x for x in arr if x[1] > pivot]
        equal = [x for x in arr if x[1] == pivot]
        lt = [x for x in arr if x[1] < pivot]
        return self.quick_sort(gt) + equal + self.quick_sort(lt)


if __name__ == '__main__':
    solu = Solution()
    s = "tree"
    print(solu.frequencySort(s))
