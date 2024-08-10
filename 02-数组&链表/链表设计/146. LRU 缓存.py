"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity)
    以 正整数 作为容量 capacity 初始化 LRU 缓存

int get(int key)
    如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。

void put(int key, int value)
    如果关键字 key 已经存在，则变更其数据值 value ；
    如果不存在，则向缓存中插入该组 key-value 。
    如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。

函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。



示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4


提示：
1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 10^5 次 get 和 put
"""

import collections


# 方法一：通过维护 key_to_node 哈希表和双向链表来管理缓存的状态，我们可以实现 LRU 缓存。
class Node(object):
    # 3.定义一个节点类 Node，其中包含键、值、前驱和后继节点的引用，这个节点类将被用作双向链表的节点
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:
    # 初始化方法，用于创建一个容量为capacity的 LRU 缓存对象
    def __init__(self, capacity: int):
        self.capacity = capacity
        # 1.使用字典来存储 key:node, 用来快速查找 key对应的节点
        self.key_to_node = {}
        # 2.使用双向链表来存储节点的访问顺序，链表的头部表示最近访问的节点，尾部表示最久未访问的节点
        # 初始化构建一头一尾2个虚拟节点， 初始化链表为 head <-> tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        # 4.当调用 get(key) 方法时，我们首先检查键是否存在于 key_to_node 哈希表中
        if key not in self.key_to_node:
            return -1
        # 如果 key 存在，先通过哈希表定位获取对应的节点，并将其移到链表的尾部表示最近访问，最后返回节点的值
        node = self.key_to_node[key]
        self._move_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # 5.当调用 put(key, value) 方法时，我们首先检查键是否存在于 key_to_node 哈希表中。
        if key in self.key_to_node:
            # 5.1 如果key存在，我们更新节点的值，并将其移到链表的尾部表示最近访问。
            node = self.key_to_node[key]
            node.val = value
            self._move_to_end(node)
        else:
            # 5.2 如果key是第一次添加，需要先判断缓存是否还有容量空间
            if len(self.key_to_node) == self.capacity:
                # 如果缓存已满，我们还需要删除链表的头部节点表示最久未访问，并从 key_to_node 哈希表中删除对应的键值对
                node = self._pop_head()
                del self.key_to_node[node.key]
            # 然后在 key_to_node 哈希表中创建新的键值对，并将新节点插入到链表的尾部
            newNode = Node(key, value)
            self.key_to_node[key] = newNode
            self._append_tail(newNode)

    def _move_to_end(self, node) -> None:
        # 将存在的节点移动到链表末尾
        # OrderedDict会先将这个节点从链表中删除，然后再将它插入到链表的末尾。
        self._pop(node)
        self._append_tail(node)

    def _pop_head(self) -> Node:
        # 删除头节点，并返回被删除的头节点
        node = self.head.next
        self._pop(node)
        return node

    def _pop(self, node) -> None:
        # 删除链表任意一个有效节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append_tail(self, node) -> None:
        # 将一个新的节点添加到双向链表的尾节点
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(str(curr.key))
            curr = curr.next
        return f'node: {"->".join(nodes)}, _map: {self.key_to_node}'


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# 方法2：直接调用collections.OrderedDict
"""
OrderedDict类似于java的LinkedHashMap， 底层是用双向链表 + 哈希字典实现有序的字典查找
还有一个LinkedHashSet,底层是用双向链表 + 哈希集合实现有序的集合查找
"""


class LRUCache2(collections.OrderedDict):
    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 首先判断键key是否存在于有序字典中
        # 1.如果不存在，返回-1
        if key not in self:
            return -1
        # 2.如果键key存在于有序字典中，先将节点移动到链表末尾，然后返回节点值
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        # 如果键key存在于有序字典中，则调用move_to_end方法将该节点移动到链表末尾
        if key in self:
            self.move_to_end(key)  # 将节点移动到链表末尾

        self[key] = value  # 更新节点值,或者添加节点到链表末尾

        if len(self) > self.capacity:  # 判断链表是否已满
            self.popitem(last=False)  # 删除链表头部节点


# 写法3
class LRUCache3:
    def __init__(self, capacity: int):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 首先判断键key是否存在于有序字典中
        # 1.如果不存在，返回-1
        if key not in self.cache:
            return -1
        # 2.如果键key存在于有序字典中，先将节点移动到链表末尾，然后返回节点值
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # 如果键key存在于有序字典中，则调用move_to_end方法将该节点移动到链表末尾
        if key in self.cache:
            self.cache.move_to_end(key)  # 将节点移动到链表末尾

        self.cache[key] = value  # 更新节点值,或者添加节点到链表末尾

        if len(self.cache) > self.capacity:  # 判断链表是否已满
            self.cache.popitem(last=False)  # 删除链表头部节点


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))  # returns 1
    cache.put(3, 3)
    print(cache.get(2))  # returns -1
    cache.put(4, 4)
    print(cache.get(1))  # returns -1
    print(cache.get(3))  # returns 3
    print(cache.get(4))  # returns 4

    # cache = LRUCache(2)
    # cache.put(2, 1)
    # cache.put(2, 2)
    # print(cache.get(2))  # returns 2
    # cache.put(1, 1)
    # cache.put(4, 1)
    # print(cache.get(2))  # returns -1
