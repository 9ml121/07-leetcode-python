"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/128165419

OJ用例
https://hydro.ac/d/HWOD2023/p/OD386/solution

题目描述
有一个文件，包含以一定规则写作的文本，请统计文件中包含的文本数量。

规则如下：

文本以 ";" 分隔，最后一条可以没有 ";" ，但空文本不能算语句，比如

COMMAND A; ;

只能算一条语句。 注意，无字符/空白字符/制表符都算作"空"文本；

文本可以跨行，比如下面，是一条文本，而不是三条

COMMAND A

AND

COMMAND B;

文本支持字符串，字符串为成对的单引号(')或者成对的双引号(")，字符串可能出现用转义字符(\)处理的单双引号("your input is\"")和转义字符本身，比如

COMMAND A "Say \"hello\"";

支持注释，可以出现在字符串之外的任意位置注释以”--“开头，到换行结束，比如

COMMAND A; -- this is comment

COMMAND -- comment

A AND COMMAND B;

注意字符串内的”--“，不是注释。

输入描述
文本文件

输出描述
包含的文本数量

用例1
输入
COMMAND TABLE IF EXISTS "UNITED STATE";
COMMAND A GREAT (
ID ADSAB,
download\_length INTE-GER, -- test
file\_name TEXT,
guid TEXT,
mime\_type TEXT,
notifica-tionid INTEGER,
original\_file\_name TEXT,
pause\_reason\_type INTEGER,
resumable\_flag INTEGER,
start\_time INTEGER,
state INTEGER,
folder TEXT,
path TEXT,
total\_length INTE-GER,
url TEXT
);
输出
2



用例1
输入
abc;abc;abc;
输出
3

用例2
输入
'abc''abc';
输出
1

用例3
输入
'abc''abc';'';'	';' 	'
输出
4

用例4
输入
--add
hello
输出
1

用例5
输入
--add comment
hello
world;
--delete comment
hi
输出
2

用例6
输入
say "hello\n world";
输出
1

用例7
输入
say "hello;\n world";
输出
1

用例8
输入
hello; ;;	;
输出
1

用例9
输入
'--hello world';
输出
1

用例10
输入
--hello world;
输出
0

用例11
输入
hello--world
输出
1

用例12
输入
'hello;\nworld;'
输出
1

用例13
输入
hello
world
welcome;
 ;
	;
'hi';
"hey\"hey\"";
"\\";
--123;
123;
输出
5

用例14
输入
hello world--
输出
1

用例15
输入
hello world;--hello;
输出
1

用例16
输入
hello world -- hey
输出
1

用例17
输入
-----
hello
输出
1

用例18
输入
hello.world;
输出
1

用例19
输入
hello,world;
hello world.
hello world;
输出
2

用例20
输入
'hello hi/?/'
hello;
hi;
输出
2

"""
import sys


# 处理有换行的输入：
# 方法1：使用字符串来构建整个输入文本
# s = sys.stdin.read()


# todo 方法2：注意sys.stdin处理有换行的文本输入，该读取方式只适用于Python3编译器
# lines = []
# for line in sys.stdin:
#     lines.append(line)
#     # print(lines)

# # 将文件内容压缩为一行，换行使用换行符\n代替
# s = "\n".join(lines)
# print(s)

# 测试用例
s = 'hello; ;;	;'

# 输出：包含的文本数量
ans = 0
# 是否有文本内容
text = False
# 是否有双引号
dq = False
# 是否有单引号
sq = False
i = 0
# 遍历每一行：
while i < len(s):
    if s[i] == ';':
        # 1.处理分号
        if not dq and not sq and text:
            ans += 1
            text = False
        i += 1
    elif s[i].isspace():
        # 2.处理空白
        i += 1
    elif s[i] == '-' and i+1 < len(s) and s[i+1] == '-' and not dq and not sq:
        # 3. 处理注释
        # 如果当前字符和下一个字符都是减号 - ， 并且不在字符串内， 则标记为注释开始。
        # 在注释内部， 忽略所有字符直到遇到换行符， 然后标记注释结束。
        while i < len(s) and s[i] != '\n':
            i += 1
    else:
        # 4. 处理字符串：
        if s[i] == '"' and not sq:
            dq = not dq
        elif s[i] == "'" and not dq:
            sq = not sq
        text = True
        i += 1

# 处理最后一个文本
if text:
    ans += 1

print(ans)
