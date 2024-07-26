"""
有6条配置命令，它们执行的结果分别是：

命   令	执   行
reset	reset what
reset board	board fault
board add	where to add
board delete	no board at all
reboot backplane	impossible
backplane abort	install first
he he	unknown command
注意：he he不是命令。

为了简化输入，方便用户，以“最短唯一匹配原则”匹配（注：需从首字母开始进行匹配）：

1、若只输入一字串，则只匹配一个关键字的命令行。例如输入：r，根据该规则，匹配命令reset，执行结果为：reset what；输入：res，根据该规则，匹配命令reset，执行结果为：reset what；
2、若只输入一字串，但匹配命令有两个关键字，则匹配失败。例如输入：reb，可以找到命令reboot backpalne，但是该命令有两个关键词，所有匹配失败，执行结果为：unknown command

3、若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果仍不唯一，匹配失败。
例如输入：r b，找到匹配命令reset board 和 reboot backplane，执行结果为：unknown command。
例如输入：b a，无法确定是命令board add还是backplane abort，匹配失败。
4、若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果唯一，匹配成功。例如输入：bo a，确定是命令board add，匹配成功。
5、若输入两字串，第一关键字匹配成功，则匹配第二关键字，若无匹配，失败。例如输入：b addr，无法匹配到相应的命令，所以执行结果为：unknow command。
6、若匹配失败，打印“unknown command”

注意：有多组输入。
数据范围：数据组数：1≤t≤800 ，字符串长度1≤s≤20
进阶：时间复杂度：O(n) ，空间复杂度：O(n)
输入描述：
多行字符串，每行字符串一条命令

输出描述：
执行结果，每条命令输出一行

示例1
输入：
reset
reset board
board add
board delet
reboot backplane
backplane abort

输出：
reset what
board fault
where to add
no board at all
impossible
install first
"""
# 最短唯一匹配原则
# 1、若只输入一字串，则只匹配一个关键字的命令行
# 2、若只输入一字串，但匹配命令有两个关键字，则匹配失败
# 3、若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果仍不唯一，匹配失败
# 4、若输入两字串，则先匹配第一关键字，如果有匹配，继续匹配第二关键字，如果唯一，匹配成功。
# 5、若输入两字串，第一关键字匹配成功，则匹配第二关键字，若无匹配，失败
# 6、若匹配失败，打印“unknown command”

# 进阶：时间复杂度：O(n) ，空间复杂度：O(n)
command = [
    "reset",
    "reset board",
    "board add",
    "board delete",
    "reboot backplane",
    "backplane abort",
]
console = [
    "reset what",
    "board fault",
    "where to add",
    "no board at all",
    "impossible",
    "install first",
]

while True:
    try:
        l = input().split()
        # 1. 一字串
        if len(l) == 1:
            if command[0].startswith(l[0]):
                print(console[0])
            else:
                print("unknown command")

        # 2. 2字串
        elif len(l) == 2:
            tmp = []
            for i in range(1, len(command)):
                command2 = command[i].split()
                if command2[0].startswith(l[0]) and command2[1].startswith(l[1]):
                    tmp.append(i)
            if len(tmp) == 1:
                print(console[tmp[0]])
            else:
                print("unknown command")

        # 3. 其他
        else:
            print("unknown command")

    except:
        break
