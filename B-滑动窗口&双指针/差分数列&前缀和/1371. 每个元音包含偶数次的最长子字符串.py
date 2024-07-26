"""
给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

 
示例 1：
输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。

示例 2：
输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。

示例 3：
输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
 

提示：
1 <= s.length <= 5 x 10^5
s 只包含小写英文字母。
"""


    
# todo 方法3：位掩码/状态压缩 + 前缀和（空间换时间）
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 返回字符串s的最长子字符串的长度：每个元音字母在子字符串中都恰好出现了偶数次
        ans = 0

        # "前缀子串"中各个元音的奇偶状态
        # 00000
        # aeiou
        # 元音字母和二进制位的对应关系如上，如果二进制位值为0，代表对应元音字符数量有偶数个，如果二进制位值为1，代表对应元音字符数量有奇数个
        # 初始未遍历时，没有子串，此时各个元音的数量都为0，即偶数个，因此所有二进制位值位0
        status = 0b00000

        # todo 哈希表map来记录某个压缩状态最早出现的位置，key是压缩状态，val是该压缩状态的最早出现位置。
        # 1.压缩状态用五位二进制数表示，因此最多有2^5=32种状态
        # 2.初始值-2是一个不可能的位置, 即初始时各个状态都没有出现过
        map = [-2] * 32
        # 00000 状态对应的十进制数为0，最早出现位置是-1，即未遍历，没有子串时
        map[0] = -1

        for i, c in enumerate(s):
            # 如果遍历的字符s[i]是元音字母，则变更对应二进制位的奇偶性
            if c == 'a':
                status ^= 0b10000  # 2**4
            elif c == 'e':
                status ^= 0b01000  # 2**3
            elif c == 'i':
                status ^= 0b00100  # 2**2
            elif c == 'o':
                status ^= 0b00010  # 2**1
            elif c == 'u':
                status ^= 0b00001  # 2**0

            if map[status] == -2:
                # 1.对应状态之前未出现，当前位置 i 就是该状态的最早出现位置
                map[status] = i
            else:
                # 2.当前位置 i 的状态为status，而最早出现status状态的位置是 map[status]，
                # 两个位置同奇偶性，因此他们形成的范围内子串是符合要求的
                # - 如果两个数字奇偶性相同，那么其相减一定是偶数。
                # - 如果两个数字奇偶性不同，那么其相减一定是奇数。
                ans = max(ans, i - map[status])

        return ans


"""
https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/medium/1371.find-the-longest-substring-containing-vowels-in-even-counts
todo 1.暴力法 + 剪枝
思路
首先拿到这道题的时候，我想到第一反应是滑动窗口行不行。 但是很快这个想法就被我否定了，因为滑动窗口（这里是可变滑动窗口）我们需要扩张和收缩窗口大小，而这里不那么容易。因为题目要求的是奇偶性，而不是类似“元音出现最多的子串”等。

突然一下子没了思路。那就试试暴力法吧。暴力法的思路比较朴素和直观。 那就是双层循环找到所有子串，然后对于每一个子串，统计元音个数，如果子串的元音个数都是偶数，则更新答案，最后返回最大的满足条件的子串长度即可。

这里我用了一个小的 trick。枚举所有子串的时候，我是从最长的子串开始枚举的，这样我找到一个满足条件的直接返回就行了（early return），不必维护最大值。这样不仅减少了代码量，还提高了效率。

- 时间复杂度：双层循环找出所有子串的复杂度是$O(n^2)$，统计元音个数复杂度也是$O(n)$，因此这种算法的时间复杂度为$O(n^3)$。
- 空间复杂度：$O(1)$

todo 2.前缀和 + 剪枝
思路
上面思路中对于每一个子串，统计元音个数，我们仔细观察的话，会发现有很多重复的统计。那么优化这部分的内容就可以获得更好的效率。

对于这种连续的数字问题，这里我们考虑使用前缀和来优化。

经过这种空间换时间的策略之后，我们的时间复杂度会降低到$O(n ^ 2)$，但是相应空间复杂度会上升到$O(n)$，这种取舍在很多情况下是值得的。

todo 方法3：前缀和 + 状态压缩
思路
前面的前缀和思路，我们通过空间（prefix）换取时间的方式降低了时间复杂度。但是时间复杂度仍然是平方，我们是否可以继续优化呢？

实际上由于我们只关心奇偶性，并不关心每一个元音字母具体出现的次数。因此我们可以使用是奇数，是偶数两个状态来表示，由于只有两个状态，我们考虑使用位运算。

我们使用 5 位的二进制来表示以 i 结尾的字符串中包含各个元音的奇偶性，其中 0 表示偶数，1 表示奇数，并且最低位表示 a，然后依次是 e，i，o，u。
比如 10110 则表示的是包含偶数个 a 和 o，奇数个 e，i，u，我们用变量 cur 来表示。

为什么用 0 表示偶数？1 表示奇数？

回答这个问题，你需要继续往下看。

其实这个解法还用到了一个性质，这个性质是小学数学知识：
    - 如果两个数字奇偶性相同，那么其相减一定是偶数。
    - 如果两个数字奇偶性不同，那么其相减一定是奇数。

看到这里，我们再来看上面抛出的问题为什么用 0 表示偶数？1 表示奇数？。因为这里我们打算用异或运算，而异或的性质是：

如果对两个二进制做异或，会对其每一位进行位运算，如果相同则位 0，否则位 1。这和上面的性质非常相似。
上面说奇偶性相同则位偶数，否则为奇数。因此很自然地用 0 表示偶数？1 表示奇数会更加方便。

复杂度分析
- 时间复杂度：$O(n)$。
- 空间复杂度：$O(n)$
"""

# todo 方法1：暴力法 + 剪枝  =>可以通过
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 返回字符串s的最长子字符串的长度：每个元音字母在子字符串中都恰好出现了偶数次
        n = len(s)
        # todo 先枚举最长的子串长度, 再枚举子串的开始位置，找到一个满足条件的直接返回（early return）
        for sz in range(n, 0, -1):
            for i in range(n - sz + 1):  # sz=j-i+1 => j=sz-1+i<n => i<n-sz+1
                sub = s[i:i + sz]
                has_odd_vowel = False
                for vowel in ['a', 'e', 'i', 'o', 'u']:
                    if sub.count(vowel) % 2 != 0:
                        has_odd_vowel = True
                        break

                if not has_odd_vowel:
                    return sz
        return 0

# 方法2：前缀和 + 剪枝（不推荐）
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 返回字符串s的最长子字符串的长度：每个元音字母在子字符串中都恰好出现了偶数次
        from collections import Counter
        n = len(s)
        # todo 前缀和数组pre[i]：代表s[i]之前出现的5个元音字符个数，初始化为一个空计数器
        preSum = [Counter() for _ in range(n+1)]

        # 先统计s每个位置之前出现的5个元音字符个数
        for i in range(1, n+1):
            preSum[i] = preSum[i - 1].copy()  # 注意：可变数据结构一定要拷贝
            c = s[i-1]
            if c in 'aeiou':
                preSum[i][c] += 1
          
                

        def check(l:int, r:int)->bool:
            # todo 利用前缀和数组pre, 计算5个元音字符在s[l..r]区间出现的次数是否都是偶数次
            for c in 'aeiou':
                if (preSum[r+1][c] - preSum[l][c]) % 2 != 0:
                    return False
            return True
        
        # todo 先枚举最长的子串长度, 再枚举子串的开始位置，找到一个满足条件子串直接返回（early return）
        for sz in range(n, 0, -1):
            for i in range(n - sz + 1):  # sz=j-i+1 => j=sz+i-1 < n => i<n-sz+1
                if check(i, i + sz - 1):
                    return sz
        return 0
    
# todo 方法3：前缀和 + 状态压缩（最优解）
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # 返回字符串s的最长子字符串的长度：每个元音字母在子字符串中都恰好出现了偶数次
        
        # map字典是将5个元音字母转换为一个5位二进制数字
        map = {
            "a": 2**0,  # 00001
            "e": 2**1,  # 00010
            "i": 2**2,  # 00100
            "o": 2**3,  # 01000
            "u": 2**4   # 10000
        }
        
        # todo seen的key最多有2^5=32个数字[0..31], 代表32种压缩状态，value代表每个状态在s中最早出现的位置
        # 初始状态:key=0，value=-1, 代表还没有出现元音字符
        seen = {0: -1}
        ans =0
        cur = 0 # cur代表s当前位置的压缩状态数字

        for i, c in enumerate(s):
            if c in map:
                cur ^= map[c]  # todo 二进制异或运算，模拟当前位置该字符出现的奇偶次，0代表偶数次，1代表奇数次
            
            # todo 2个二进制数字全部位置奇偶性相同，相减一定都是偶数
            if cur in seen:
                # s(seen[cur]..i] 里面元音字符都是偶数次
                ans = max(ans, i - seen[cur])
            else:
                seen[cur] = i
        return ans
