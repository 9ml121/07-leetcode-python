"""
你会得到一个双链表，其中包含的节点有一个下一个指针、一个前一个指针和一个额外的 子指针 。这个子指针可能指向一个单独的双向链表，也包含这些特殊的节点。这些子列表可以有一个或多个自己的子列表，以此类推，以生成如下面的示例所示的 多层数据结构 。

给定链表的头节点 head ，将链表 扁平化 ，以便所有节点都出现在单层双链表中。让 curr 是一个带有子列表的节点。子列表中的节点应该出现在扁平化列表中的 curr 之后 和 curr.next 之前 。

返回 扁平列表的 head 。列表中的节点必须将其 所有 子指针设置为 null 。



示例 1：



输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：

示例 2：



输入：head = [1,2,null,3]
输出：[1,3,2]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：

示例 3：

输入：head = []
输出：[]
说明：输入中可能存在空列表。


提示：

节点数目不超过 1000
1 <= Node.value <= 105


如何表示测试用例中的多级链表？

以 示例 1 为例：

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
序列化其中的每一级之后：

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
合并所有序列化结果，并去除末尾的 null 。

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
"""
import unittest


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __str__(self):
        output = ''
        p = self
        while p:
            output += str(p.val) + '->'
            p = p.next
        output += 'NULL'
        return output


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """扁平化多级双向链表
        方法 2：迭代解法 第一版
        """
        p = head
        while p:
            if p.child:
                tmpNext = p.next
                # 1.head ⇋ head.child
                child_head = p.child
                p.next, child_head.prev = child_head, p
                p.child = None
                # 2. head.child.child_tail ⇋ head.next
                child_tail = child_head
                while child_tail.next:
                    child_tail = child_tail.next
                if tmpNext:
                    child_tail.next = tmpNext
                    tmpNext.prev = child_tail
            p = p.next

        return head


class Solution2:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """扁平化多级双向链表
        方法 2：迭代解法 第二版(利用栈实现)
        """
        if not head:
            return None
        prev = dummy = Node(0, None, head, None)
        stack = [head]
        while stack:
            curr = stack.pop()
            prev.next, curr.prev = curr, prev
            # 先压next节点，后压child节点，先驱节点 prev指向弹出的栈顶节点，不断移动
            if curr.next:
                stack.append(curr.next)  # 如果有下一个节点，将其加入栈中
            if curr.child:
                stack.append(curr.child)  # 如果有子节点，将其加入栈中
                curr.child = None
            # 更新当前节点(注意：如果cur既没有子节点，也没有next节点，那么先驱节点prev就是当前节点的尾节点)
            prev = curr
        dummy.next.prev = None  # 将头节点的前驱节点置空
        return dummy.next


class Solution3:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """扁平化多级双向链表
        方法 3：递归思路 第一版
        """
        # 如果链表为空，直接返回None
        if not head:
            return None

        # 定义扁平化函数：返回的是node最后一个有效节点
        def flatten_dfs(node) -> 'Optional[Node]':
            # 如果当前节点是叶子节点，直接返回该节点
            if not node.next and not node.child:
                return node
            # 如果当前节点有子节点，先处理子节点
            if node.child:
                # 递归处理子节点，并返回子节点的尾节点
                child_tail = flatten_dfs(node.child)
                # 将子节点插入到当前节点和下一个节点之间
                child_head = node.child
                node.child = None
                child_head.prev = node
                child_tail.next = node.next
                if node.next:
                    node.next.prev = child_tail
                node.next = child_head
                # 关键：更新当前节点为子节点的尾节点！！！
                node = child_tail
            # 如果当前节点有下一个节点，递归处理下一个节点
            if node.next:
                node = flatten_dfs(node.next)
            # 返回当前节点
            return node

        # 调用扁平化函数，对链表进行扁平化操作
        flatten_dfs(head)
        # 返回扁平化后的链表
        return head


class Solution4:
    def flatten(self, head: 'Node') -> 'Node':
        """扁平化多级双向链表
        方法 4：递归思路 第2版, 类似二叉树前序遍历
        """
        # 定义一个变量p，用于记录当前节点
        p = None

        # 定义dfs函数，用于遍历节点
        def dfs(node) -> None:
            nonlocal p
            if not node:
                return
            # 分别获取当前节点的子节点和下一个节点
            child, next = node.child, node.next
            # 将当前节点的子节点和下一个节点置为空(下一个节点不管也可以，有系统垃圾回收)
            node.child = None

            # todo 前序位置：构建 p ⇋ node
            if p is not None:
                p.next = node
                node.prev = p
            # 将p指向当前节点
            p = node
            # 递归遍历子节点和下一个节点
            dfs(child)
            dfs(next)

        # 调用dfs函数遍历节点
        dfs(head)
        # 返回头节点
        return head


if __name__ == '__main__':
    """
    1->2->3
       |
       4->5
    """
    # head = Node(1)
    # head.next = Node(2)
    # head.next.prev = head
    # head.next.next = Node(3)
    # head.next.next.prev = head.next
    # head.next.child = Node(4)
    # head.next.child.next = Node(5)
    # head.next.child.next.prev = head.next.child
    # s = Solution2()
    # result = s.flatten(head)
    # while result:
    #     print(result.value)
    #     result = result.next

    # 构造测试用例
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node3.child = node7
    node7.next = node8
    node8.next = node9
    node9.next = node10
    node11 = Node(11)
    node12 = Node(12)
    node8.child = node11
    node11.next = node12
    s = Solution2()
    result = s.flatten(node1)
    while result:
        print(result.val)
        result = result.next
