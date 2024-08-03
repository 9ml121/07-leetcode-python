"""
题目描述
每个数字关联多个字母，关联关系如下：

0 关联 “a”,”b”,”c”
1 关联 “d”,”e”,”f”
2 关联 “g”,”h”,”i”
3 关联 “j”,”k”,”l”
4 关联 “m”,”n”,”o”
5 关联 “p”,”q”,”r”
6 关联 “s”,”t”
7 关联 “u”,”v”
8 关联 “w”,”x”
9 关联 “y”,”z”
输入一串数字后，通过数字和字母的对应关系可以得到多个字母字符串（要求按照数字的顺序组合字母字符串）；
屏蔽字符串：屏蔽字符串中的所有字母不能同时在输出的字符串出现，如屏蔽字符串是abc，则要求字符串中不能"同时出现a,b,c"!!，但是允许同时出现a,b或a,c或b,c等；

给定一个数字字符串和一个屏蔽字符串，输出所有可能的字符组合；

例如输入数字字符串78和屏蔽字符串ux，输出结果为uw，vw，vx；数字字符串78，可以得到如下字符串uw，ux，vw，vx；
由于ux是屏蔽字符串，因此排除ux，最终的输出是uw，vw，vx;

输入描述
第一行输入为一串数字字符串，数字字符串中的数字不允许重复，数字字符串的长度大于0，小于等于5；
第二行输入是屏蔽字符串，屏蔽字符串的长度一定小于数字字符串的长度，屏蔽字符串中字符不会重复；

输出描述
输出可能的字符串组合

注：字符串之间使用逗号隔开，最后一个字符串后携带逗号

用例
输入	78
        ux
输出	uw,vw,vx,
说明	无

输入	78
        x
输出	uw,vw,
说明	无
"""
# todo 回溯
# 类似：C-回溯算法\排列 & 组合 & 子集\17. 电话号码的字母组合.py

# 输入
# 数字字符串，数字不重复
# input_str = input()
# 屏蔽字符串：字符不重复，屏蔽字符串中的所有字母不能同时在输出的字符串出现
# filter_str = input()

# 测试数据
import itertools
input_str = '78'
filter_str = 'ux'



# 将数字字符串input_str, 转换为代表的字母列表str_list
str_list = []
mapping = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'st', 'uv', 'wx', 'yz']
for num in list(map(int, input_str)):
    str_list.append(mapping[num])
# print(str_list)  # ['uv', 'wx']

# 输出：输出可能的字符串组合
ans = []
n = len(str_list)


def dfs(i=0, path=[]):
    if i == n:
        # 要求按照数字的顺序组合字母字符串
        new_str = ''.join(sorted(path))
        if new_str.find(filter_str) == -1:
            # 屏蔽字符串中的所有字母不能同时在输出的字符串出现
            # 如屏蔽字符串是abc，则要求字符串中不能"同时出现a,b,c"!!，但是允许同时出现a,b或a,c或b,c等
            ans.append(new_str)
        
        return

    for ch in str_list[i]:
        path.append(ch)
        dfs(i + 1, path)
        path.pop()

dfs()
print(','.join(ans) + ',')


# 方法2：调用itertools
def get_result2(str_list, filter_str):
    str_combine = sorted(itertools.product(*str_list))
    for elem in str_combine:
        new_str = ''.join(elem)
        if new_str.find(filter_str) == -1:
            print(new_str, end=',')
