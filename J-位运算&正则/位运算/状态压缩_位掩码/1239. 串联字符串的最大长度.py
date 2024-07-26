"""
给定一个字符串数组 arr，字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串。

请返回所有可行解 s 中最长长度。

子序列 是一种可以从另一个数组派生而来的数组，通过删除某些元素或不删除元素而不改变其余元素的顺序。

 

示例 1：

输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是：
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
最大长度为 4。
示例 2：

输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。
示例 3：

输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26
 

提示：

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] 中只含有小写英文字母
"""


from typing import List

# 方法1：动态规划
"""
一个字符串可以作为答案当且仅当其中没有重复的字符(包括我们在拼接字符串以后,拼接的字符串也同理)
所以维护一个之前所有的合法的拼接字符串,判断当前所有能组成的合理的字符串，最后返回最大值即可。
"""
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串
        # 返回所有可行解 s 中最长长度
        
        def validStr(s):
            # 校验字符串s有没有重复元素
            return len(set(s)) == len(s)

        # dp数组保存已经找到的所有合法的拼接字符串
        dp = []
        for s in arr:
            if not validStr(s):
                # 1.s有重复字符，直接跳过
                continue
            
            # 2.s没有重复字符，尝试跟dp数组所有字符串进行拼接
            # todo 注意：循环对dp数组有添加元素，所以要先拷贝一份
            for s_ in list(dp):  
                if validStr(s_ + s):
                    dp.append(s_ + s)
            
            # 最后dp不要忘了添加s本身
            dp.append(s)
        
        # 最后结果就是dp数组元素长度最大值
        return len(max(dp, key=len)) if dp else 0


    # 上述写法优化：利用集合求交集判断2个集合是否有重复字符，利用并集操作来合并没有交集的2个集合​
    def maxLength2(self, arr: List[str]) -> int:
        # 字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串
        # 返回所有可行解 s 中最长长度
        
        # todo dp保存所有合法的拼接字符串集合
        dp = [set()]
        for s in arr:
            s_set = set(s)
            if len(s) != len(s_set):
                # s有重复元素
                continue
                
            for cur_set in dp[:]:
                # 检查2个集合是否有交集
                if s_set & cur_set:  # todo 求交集：等价于s_set.intersection(cur_set)
                    continue
                
                # 合并2个没有交集的集合
                dp.append(s_set | cur_set) # todo 求并集：等价于s_set.union(cur_set)
                
        return len(max(dp, key=len)) if dp else 0


# 方法2：回溯算法
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串
        # 返回所有可行解 s 中最长长度
        ans = 0
        # 检查字符串s是否有重复子串
        def is_unique(s: str):
            return len(s) == len(set(s))

        def dfs(i=0, path=''):
            nonlocal ans
            if i == len(arr):
                # 更新最大长度
                if is_unique(path):
                    ans = max(ans, len(path))
                return

            # 选择当前字符串
            if is_unique(path + arr[i]):
                dfs(i+1, path + arr[i])

            # 不选择当前字符串
            dfs(i+1, path)

        dfs()
        return ans

# todo 方法3：状态压缩 + 位掩码(推荐！)
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # 字符串 s 是将 arr 的含有 不同字母 的 子序列 字符串 连接 所得的字符串
        # 返回所有可行解 s 中最长长度
        ans = 0
        # todo masks数组保存arr所有已遍历的字符串可以组成的不重复字符串位掩码
        # 每个字符串位掩码是一个26位的二进制数字，每个位置数字为1代表当前表示的字符串存在，0代表不存在
        masks = [0]

        
        for s in arr:
            # 计算当前字符串s的位掩码
            mask = 0
            for c in s:
                if s.count(c) > 1:
                    # s有重复字符，位掩码为0
                    mask = 0
                    break
                
                mask |= (1 << (ord(c) - ord('a')))
            
            if mask == 0:
                # 跳过有重复字符的字符串
                continue

            for m in masks[:]: # todo 循环对数组有添加元素，这里要拷贝原始数组
                if m & mask == 0:  # todo  m & mask：等级于两个集合取交集(0代表2个位掩码没有位置相同元素)
                    concat_m = m | mask  # todo 合并掩码, m | mask:等价于两个集合取并集
                    masks.append(concat_m)
                    ans = max(ans, bin(concat_m)[2:].count('1')) # todo 位掩码中的1就代表1个字符
        return ans
