"""
https://blog.csdn.net/qfc_128220/article/details/127634016
题目描述
警察在侦破一个案件时，得到了线人给出的可能犯罪时间，形如 “HH:MM” 表示的时刻。

根据警察和线人的约定，为了隐蔽，该时间是修改过的，

解密规则为：利用当前出现过的数字，构造下一个距离当前时间最近的时刻，则该时间为可能的犯罪时间。

每个出现数字都可以被无限次使用。

输入描述
形如HH:SS字符串，表示原始输入。

输出描述
形如HH:SS的字符串，表示推理处理的犯罪时间。

备注
1.可以保证现任给定的字符串一定是合法的。

例如，“01:35”和“11:08”是合法的，“1:35”和“11:8”是不合法的。

2.最近的时刻可能在第二天。

用例
输入	输出
20:12	20:20
23:59	22:22
12:58	15:11
18:52	18:55
23:52	23:53
09:17	09:19
07:08	08:00
"""

# 方法1:dfs + 正则
def solution1():
    import re
    p = re.compile(r'(([01][0-9])|([2][0-3]))[0-5][0-9]')
    s = input().replace(':', '')

    chrs = list(set(s))
    chrs.sort()


    def dfs(chrs, path, res):
        if len(path) == 4:
            tmp = ''.join(path)
            if re.match(p, tmp):
                res.append(tmp)
            return

        for c in chrs:
            path.append(c)
            dfs(chrs, path, res)
            path.pop()


    res = []
    dfs(chrs, [], res)
    res.sort()
    idx = res.index(s)
    nxt_idx = (idx + 1 + len(res)) % len(res)
    ans = res[nxt_idx]
    print(ans[0:2] + ':' + ans[2:])


# 方法2: 规则匹配
def solution2():
    s = list(input().replace(':', ''))  # 20:12
    digits = list(set(s))
    digits.sort()  # 0 1 2

    # 判断四位
    def check(s):
        flag = False
        for c in digits:
            # re.compile(r'(([01][0-9])|([2][0-3]))[0-5][0-9]')
            if c > s[3]:
                s[3] = c
                return s
        
        for c in digits:
            if c > s[2] and c <= '5':
                s[2] = c
                s[3] = digits[0]
                return s
        
        
        for c in digits:
            if s[0] == '0' or s[0] == '1':
                if c > s[1] and c <= '9':
                    s[1] = c
                    s[2] = s[3] = digits[0] 
                    return s
            if s[0] == '2':
                if c > s[1] and c <= '3':
                    s[1] = c
                    s[2] = s[3] = digits[0] 
                    return s
            
        for c in digits:
            if c > s[0] and c <= '2':
                s[0] = c
                s[2] = s[3] = s[1] = digits[0]
        
        # 23:59	22:22
        return digits[0] * 4


    ans = check(s)  # ['2', '0', '2', '0']
    ans = ''.join(ans)
    print(ans[0:2] + ':' + ans[2:])
