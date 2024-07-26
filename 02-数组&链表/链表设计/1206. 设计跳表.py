"""
不使用任何库函数，设计一个 跳表 。

跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

例如，一个跳表包含 [30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作：


Artyom Kalinin [CC BY-SA 3.0], via Wikimedia Commons

跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

了解更多 : https://en.wikipedia.org/wiki/Skip_list

在本题中，你的设计应该要包含这些函数：

bool search(int target) : 返回target是否存在于跳表中。
void add(int num): 插入一个元素到跳表。
bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。



示例 1:

输入
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
输出
[null, null, null, null, false, null, true, false, true, false]

解释
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除


提示:

0 <= num, target <= 2 * 104
调用search, add,  erase操作次数不大于 5 * 104
"""
"""
设计跳表的关键是要实现快速的搜索、插入和删除操作，并保持跳表的结构和有序性。
以下是设计跳表的一种解题思路：

1.定义跳表的节点结构，每个节点包括一个值和若干个指向下一个节点的指针。
2.创建一个跳表对象，并初始化一个空的头节点。头节点的值可以是任意值，通常设置为负无穷大或正无穷大。
3.实现搜索操作：
    - 从头节点开始，按层级向下搜索，比较节点的值与目标值的大小。
    - 如果节点的值等于目标值，则找到了目标节点，返回 True。
    - 如果节点的值大于目标值或者到达了当前层级的末尾节点，则进入下一层级。
    - 重复上述步骤，直到到达最底层或者找到了合适的位置。
4.实现插入操作：
    - 执行搜索操作，找到插入位置的前一个节点。
    - 创建一个新节点，将其值设置为待插入的值。
    - 更新节点的指针，将新节点插入到跳表中。
    - 根据一定的概率，随机决定是否在上层级插入指向新节点的指针。
5.实现删除操作：
    - 执行搜索操作，找到待删除节点。
    - 更新节点的指针，将其从跳表中移除。
    - 同时更新上层级的指针，保持跳表的结构和有序性。

以上是一种基本的跳表设计思路，实际的实现可能会有一些细节上的差异。
在实际设计过程中，还可以考虑对跳表进行优化，例如动态调整层级的数量、使用索引节点等。
"""

import random


class Node:
    def __init__(self, val, max_level):
        self.val = val
        self.next = [None] * max_level

    def __repr__(self):
        return f"Node(value={self.val}, next={self.next})"


class Skiplist:
    # MAX_LEVEL = 32
    # SKIPLIST_P = 0.25
    MAX_LEVEL = 3
    SKIPLIST_P = 0.50

    def __init__(self):
        self.head = Node(-1, Skiplist.MAX_LEVEL)
        self.cur_level = 0

    def search(self, target):
        cur = self.head
        for i in range(self.cur_level - 1, -1, -1):
            # 找到第i层最大的小于target的元素
            while cur.next[i] is not None and cur.next[i].val < target:
                cur = cur.next[i]
        # 已经在第一层
        cur = cur.next[0]
        # 当前元素的值是否等于 target
        return cur is not None and cur.val == target

    def add(self, num):
        # 存放更新的位置
        update = [self.head] * Skiplist.MAX_LEVEL
        cur = self.head
        for i in range(self.cur_level - 1, -1, -1):
            # 找到所有层的前驱结点
            while cur.next[i] is not None and cur.next[i].val < num:
                cur = cur.next[i]
            update[i] = cur
        random_level = self.random_level()
        # 更新最高的层数
        self.cur_level = max(self.cur_level, random_level)
        new_node = Node(num, random_level)
        # 插入随机出来的所有level
        for i in range(random_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num):
        update = [self.head] * Skiplist.MAX_LEVEL
        cur = self.head
        for i in range(self.cur_level - 1, -1, -1):
            # 找到第i层最大的小于target的元素
            while cur.next[i] is not None and cur.next[i].val < num:
                cur = cur.next[i]
            update[i] = cur
        cur = cur.next[0]
        # 判断num是否存在
        if cur is None or cur.val != num:
            return False
        for i in range(self.cur_level):
            if update[i].next[i] != cur:
                break
            # 删除第i层的值和num相等的元素
            update[i].next[i] = cur.next[i]
        # 有可能最上层只有一个元素，缩短层数
        while self.cur_level > 1 and self.head.next[self.cur_level - 1] is None:
            self.cur_level -= 1
        return True

    def random_level(self):
        """
        * 该 randomLevel 方法会随机生成 1~MAX_LEVEL 之间的数，且
        * 1/2 的概率返回 2
        * 1/4 的概率返回 3
        * 1/8 的概率返回 4 以此类推
        """
        level = 1
        # 当 level < MAX_LEVEL，且随机数小于设定的晋升概率时，level + 1
        while random.random() < Skiplist.SKIPLIST_P and level < Skiplist.MAX_LEVEL:
            level += 1
        return level

    def __repr__(self):
        return f"Skiplist(head={self.head}, cur_level={self.cur_level})"


if __name__ == '__main__':
    # 创建一个跳表对象
    skiplist = Skiplist()
    # 向跳表中添加元素
    skiplist.add(1)
    skiplist.add(2)
    skiplist.add(3)
    # 在跳表中搜索元素
    print(skiplist.search(0))  # 返回 False
    skiplist.add(4)
    print(skiplist.search(1))  # 返回 True
    # 在跳表中删除元素
    skiplist.erase(0)  # 返回 False，0 不在跳表中
    skiplist.erase(1)  # 返回 True
    print(skiplist.search(1))  # 返回 False，1 已被擦除
