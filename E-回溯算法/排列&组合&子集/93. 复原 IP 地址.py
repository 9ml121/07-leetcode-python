"""
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。
你 不能 重新排序或删除 s 中的任何数字。
你可以按 任何 顺序返回答案。

示例 1：
输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

示例 2：
输入：s = "0000"
输出：["0.0.0.0"]

示例 3：
输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


提示：
1 <= s.length <= 20
s 仅由数字组成
"""
from typing import List


# todo 回溯算法思考模式
# 1.原问题 ==》 子问题： 子问题和原问题是相似的，这种从原问题到子问题的过程，适合用递归解决
# 2.回溯有一个 增量构造答案 的过程，这个过程通常用递归实现 
# 3.通过递归达到多层循环的目的

# 回溯写法1
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 返回s切割之后所有可能的有效 IP 地址
        n = len(s)
        ans = []

        def dfs(i=0, ip_idx=0, path=[''] * 4):
            if i < n and ip_idx == 4:
                # ip已经有4个子段，但是s还有数字没用
                return

            if i == n and ip_idx < 4:
                # s已经用完，但是ip子段不足4个
                return

            if i == n and ip_idx == 4:
                # s已经用完，并且ip有4个子段，收集结果
                ans.append('.'.join(path))
                return

            # 1.当前ip子段长度为1位
            if i < n:
                path[ip_idx] = s[i]
                dfs(i + 1, ip_idx + 1, path)

            # 2.当前ip子段长度为2位
            if s[i] != '0' and i + 1 < n:
                path[ip_idx] = s[i: i + 2]
                dfs(i + 2, ip_idx + 1, path)

            # 3.当前ip子段长度为3位
            if s[i] != '0' and i + 2 < n and int(s[i: i + 3]) <= 255:
                path[ip_idx] = s[i: i + 3]
                dfs(i + 3, ip_idx + 1, path)

        dfs()
        return ans
    
# 回溯写法2
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 返回s切割之后所有可能的有效 IP 地址
        n = len(s)
        ans = []

        def check_ip_segment(l, r):
            # 检查s[l..r]是否为一个合法的ip子段
            seg_len = r - l + 1  # 子段长度

            if seg_len == 1:
                return True

            if seg_len == 2 and s[l] != '0':
                # 子段不含前导0
                return True

            if seg_len == 3 and s[l] != '0' and int(s[l: r + 1]) <= 255:
                # 子段不能超过255
                return True

            return False

        def dfs(i=0, ip_idx=0, path=[''] * 4):
            if i == n:
                if ip_idx == 4:
                    # s所有数字都用完，并且ip子段有4个，收集结果
                    ans.append('.'.join(path))
                return

            # 剪枝: s[i:]长度超过合法ip长度限制，合法ip子段长度为[1..3]
            s_len = n-i
            ip_len = 4-ip_idx
            if s_len < ip_len * 1 or s_len > ip_len * 3:
                return

            for j in range(i, max(i + 3, n)):
                # 每个ip子段最多3位数
                if check_ip_segment(i, j):
                    path[ip_idx] = s[i:j+1]
                    dfs(j + 1, ip_idx + 1, path)

        dfs()
        return ans





        
    


if __name__ == '__main__':
    s = "25525511135"
    print(Solution().restoreIpAddresses(s))
