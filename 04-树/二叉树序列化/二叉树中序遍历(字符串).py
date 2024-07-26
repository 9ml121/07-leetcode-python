"""
题目描述
根据给定的二叉树结构描述字符串，输出该二叉树按照中序遍历结果字符串。中序遍历顺序为：左子树，根结点，右子树。

输入描述
由大小写字母、左右大括号、逗号组成的字符串:字母代表一个节点值，左右括号内包含该节点的子节点。

左右子节点使用逗号分隔，逗号前为空则表示左子节点为空，没有逗号则表示右子节点为空。

二叉树节点数最大不超过100。

注:输入字符串格式是正确的，无需考虑格式错误的情况。

输出描述
输出一个字符串为二叉树中序遍历各节点值的拼接结果。

用例
输入	a{b{d,e{g,h{,i}}},c{f}}
输出	dbgehiafc
说明	无

           a
         /   \
        b     c
       / \    /
      d   e  f
         / \
        g   h
            \
             i
"""

# 获取输入
s = 'a{b{d,e{g,h{,i}}},c{f}}'
stack = []
idx = []  # 记录'{'在stack当中存储的索引位置
for i in range(len(s)):
    c = s[i]
    if c == '}':
        lastIdx = idx.pop()
        # 括号里面有左节点：c{f}, e{g, *}
        # 括号里面没有左节点：h{, i}
        child = ''.join(stack[lastIdx+1:])
        parent = stack[lastIdx-1]
        stack = stack[:lastIdx-1]
        # 按照中序：左+父+右的顺序排序
        child_split = child.split(',')
        left, right = '', ''
        if len(child_split) == 1:
            left = child_split[0]
        else:
            left, right = child_split
        midOrder = left + parent + right
        stack.append(midOrder)
        continue

    if c == '{':
        idx.append(len(stack))
    stack.append(c)
print(''.join(stack))















