"""
给你一个字符数组 chars ，请使用下述算法压缩：

从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

如果这一组长度为 1 ，则将字符追加到 s 中。
否则，需要向 s 追加字符，后跟这一组的长度。
压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。
需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

请在 修改完输入数组后 ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

 

示例 1：

输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释："aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。

示例 2：
输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：唯一的组是“a”，它保持未压缩，因为它是一个字符。

示例 3：
输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
 

提示：
1 <= chars.length <= 2000
chars[i] 可以是小写英文字母、大写英文字母、数字或符号
"""


from typing import List

# todo 考察快慢指针（三指针）
class Solution:
    def compress(self, chars: List[str]) -> int:
        # 要求原地压缩字符数组 chars
        n = len(chars)
        # l代表每个新字符的开始位置，nums[l..r]区间都是连续相同字符
        l = 0
        # write代表下一个要修改的位置，nums[0..write)是最后修改完的结果字符
        write = 0
        for r in range(n):
            if r == n - 1 or chars[r+1] != chars[r]:
                # 1.下一个字符跟前面字符不一样，或者遍历到数组结尾，在write下标写入字符
                chars[write] = chars[r]
                write += 1
                
                # 2.如果字符重复个数大于1，在write下标写入压缩字符个数: str(r-l+1)
                if r > l:
                    for d in str(r-l+1):
                        # 如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符
                        chars[write] = d
                        write += 1
                        
                l = r+1

        
        # 删除结尾多余字符
        del chars[write:]
        # 返回该数组的新长度。
        return len(chars)  
