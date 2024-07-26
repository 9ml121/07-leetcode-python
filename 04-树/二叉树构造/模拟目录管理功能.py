"""
题目解析和算法源码
https://fcqian.blog.csdn.net/article/details/134387544?spm=1001.2014.3001.5502

OJ用例
题解 - 模拟目录管理功能 - Hydro

题目描述
实现一个模拟目录管理功能的软件，输入一个命令序列，输出最后一条命令运行结果。

支持命令：

创建目录命令：mkdir 目录名称，如 mkdir abc 为在当前目录创建abc目录，如果已存在同名目录则不执行任何操作。此命令无输出。
进入目录命令：cd 目录名称，如 cd abc 为进入abc目录，特别地，cd .. 为返回上级目录，如果目录不存在则不执行任何操作。此命令无输出。
查看当前所在路径命令：pwd，输出当前路径字符串。
约束：

目录名称仅支持小写字母；mkdir 和 cd 命令的参数仅支持单个目录，如：mkdir abc 和 cd abc；不支持嵌套路径和绝对路径，如 mkdir abc/efg，cd abc/efg，mkdir /abc/efg，cd /abc/efg 是不支持的。
目录符号为/，根目录/作为初始目录。
任何不符合上述定义的无效命令不做任何处理并且无输出。
输入描述
输入 N 行字符串，每一行字符串是一条命令。

输出描述
输出最后一条命令运行结果字符串。

备注
命令行数限制100行以内，目录名称限制10个字符以内。

用例1
输入
mkdir abc
cd abc
pwd
输出
/abc/
说明
在根目录创建一个abc的目录并进入abc目录中查看当前目录路径，输出当前路径/abc/。

"""

# 目录结构，其实就是一个树形结构。一个父目录下面可以有多个直接子目录，而一个子目录只能有一个父目录。
# 因此，本题需要定义出一个多叉树结构。


class Node:
    def __init__(self, name: str):
        self.name = name
        # todo childs节点可以使用 字典Map 来定义（key是目录名，val是对应目录名的TreeNode），从而实现快速查找对应目录
        self.childs = {}
        self.fa = None


class TreeNode:
    def __init__(self):
        # root是根目录，根目录 / 作为初始目录
        self.root = Node('/')
        self.cur_node = self.root

    def mkdir(self, path: str):
        # 在当前目录创建abc目录，如果已存在同名目录则不执行任何操作
        if path not in self.cur_node.childs:
            # /abc/  文件名称多加一个/，方便后面打印pwd
            node = Node(path + '/')
            node.fa = self.cur_node
            self.cur_node.childs[path] = node

    def cd(self, path: str):
        # cd abc 为进入abc目录，特别地，cd .. 为返回上级目录，如果目录不存在则不执行任何操作
        if path == '..' and self.cur_node.fa:
            self.cur_node = self.cur_node.fa
        else:
            if path in self.cur_node.childs:
                self.cur_node = self.cur_node.childs[path]

    def pwd(self) -> str:
        # 输出当前路径字符串
        paths = []  # ['c', 'b', 'a']
        # 倒序路径，即不停向上找父目录
        node = self.cur_node  # /a/b/c/
        while node:
            paths.append(node.name)
            node = node.fa

        # 倒序输出
        paths.reverse()
        # print(paths)
        return ''.join(paths)


# 初始化目录结构
tree = TreeNode()
# 记录最后一条命令的输出
ans = ''
while True:
    try:
        line = input().split()
        # 本地调试需要加这个条件
        # if len(line) == 0:
        #     break

        cmd = line[0]
        if cmd == 'pwd':
            ans = tree.pwd()
        elif cmd == 'mkdir' or cmd == 'cd':
            if len(line) == 2:
                path = line[1]
                if cmd == 'mkdir':
                    tree.mkdir(path)
                else:
                    tree.cd(path)
            ans = ''
        # 其他都为无效输入
        else:
            ans = ''
    except:
        break

print(ans)
