"""
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：
LFUCache(int capacity)
    - 用数据结构的容量 capacity 初始化对象
int get(int key)
    - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
void put(int key, int value)
    - 如果键 key 已存在，则变更其值；
    - 如果键不存在，请插入键值对。
    - 当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。
    在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。

为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。


示例：
输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // 返回 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // 返回 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3


提示：

0 <= capacity <= 10^4
0 <= key <= 10^5
0 <= value <= 10^9
最多调用 2 * 105 次 get 和 put 方法
"""
import collections


# 方法1：字典 + 双向链表
class Node:
    # 4.定义双向链表节点类，其中包含键、值、频率以及前驱和后继节点的引用。
    # 这个节点类将被用作双向链表的节点。
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.freq = 0
        self.prev = None
        self.next = None


class DoublyLinkedList:
    # 5.定义双向链表类，初始化虚拟头节点和尾节点，并将它们连接起来。
    def __init__(self):
        self.head = Node()  # dummy head node
        self.tail = Node()  # dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_head(self, node):
        # 在头节点后添加节点
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self, node):
        # 删除节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_last(self) -> Node:
        # 移除尾节点
        if self.head.next == self.tail:
            return
        last_node = self.tail.prev
        self.remove_node(last_node)
        return last_node


class LFUCache:
    def __init__(self, capacity: int):
        # LFU（Least Frequently Used）最不频繁使用缓存类
        # 1.缓存最大容量、键对应的节点、频次对应的节点、最小频次和有效节点数
        self.capacity = capacity
        # 2.哈希表 key_to_node 来存储键值对，每个键对应一个双向链表节点Node，用于快速查找键对应的节点。
        self.key_to_node = {}
        # 3.哈希表 freq_to_head 来存储频率和双向链表头节点的映射关系。
        # 其中，频率是指节点在缓存中被访问的次数。作用是快速找到访问频率最低的所有链表
        self.freq_to_node = collections.defaultdict(DoublyLinkedList)
        self.min_freq = 0  # 记录最小频次
        self.size = 0  # 记录有效节点数

    def get(self, key: int) -> int:
        # 如果键 key 存在于缓存中，则获取键的值，否则返回 -1
        if key not in self.key_to_node:
            return -1

        node = self.key_to_node[key]
        self.increase_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # 插入或更新键值
        if self.capacity == 0:
            return

        if key in self.key_to_node:
            # 1.若键已存在，则更新值并增加频次
            node = self.key_to_node[key]
            node.val = value
            self.increase_freq(node)
        else:
            # 2.如果是插入一个新的建，需要先判断缓存是否已满
            if self.size == self.capacity:
                # 如果缓存已满，需要删除最小频率对应的链表中的最老节点。
                self.remove_min_freq_key()
                self.size -= 1

            # 3.将新节点插入到频率为 1 的链表中，并将最小频次更新为1
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            self.freq_to_node[1].add_to_head(new_node)
            self.min_freq = 1
            self.size += 1

    def increase_freq(self, node: Node) -> None:
        # 增加节点频次
        freq = node.freq
        # 1.先删除旧频次node节点
        freq_node = self.freq_to_node[freq]
        freq_node.remove_node(node)
        # 2.当频率为 1 的链表为空时，我们需要更新 min_freq 变量为 2。
        if freq_node.head.next == freq_node.tail and freq == self.min_freq:
            self.min_freq += 1

        # 增加节点的频次并将其添加到新频次的链表头节点后面
        node.freq += 1
        self.freq_to_node[freq + 1].add_to_head(node)

    # 淘汰频次最低且最旧的键
    def remove_min_freq_key(self) -> None:
        last_node = self.freq_to_node[self.min_freq].remove_last()
        del self.key_to_node[last_node.key]


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# 方法2：三哈希表 + 调用OrderedDict
class LFUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val = {}
        self.key_to_freq = {}
        # freq 到 keys 的映射, keys应该是一个有序集合，以便正确选择最近最久未使用的键进行淘汰
        self.freq_to_keys = collections.defaultdict(collections.OrderedDict)
        # 记录最小频率
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        # 增加 key 对应的 freq
        self._increaseFreq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # 若 key 已存在，修改对应的 value 即可
        if key in self.key_to_val:
            self.key_to_val[key] = value
            # key 对应的 freq + 1
            self._increaseFreq(key)
            return

        # 如果键 key 是第一次添加， 先判断缓存是否已达到容量限制
        # 容量已满，需要淘汰频次最低且最旧的键
        if len(self.key_to_val) == self.capacity:
            self._remove_min_freq_key()
        # 插入新键值对，并将其频次设为1
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        # 插入新 key 后最小的 freq 肯定是 1
        self.minFreq = 1
        self.freq_to_keys[1][key] = None

    # 去除 最近最久未使用 的键
    def _remove_min_freq_key(self) -> None:
        # freq 最小的 key 列表
        orderedDict = self.freq_to_keys[self.minFreq]
        # 弹出最小频次的有序字典中的第一个键(FIFO)
        deleted_key, _ = orderedDict.popitem(last=False)
        del self.key_to_val[deleted_key]
        del self.key_to_freq[deleted_key]

    # 增加 key 对应的 freq
    def _increaseFreq(self, key) -> None:
        freq = self.key_to_freq[key]
        # 将 key 从 freq 对应的有序字典中删除
        del self.freq_to_keys[freq][key]
        self.freq_to_keys[freq + 1][key] = None
        self.key_to_freq[key] += 1
        # 如果 freq 对应的有序字典空了，并且这个 freq 恰好是 minFreq，更新 minFreq
        if len(self.freq_to_keys[freq]) == 0:
            self.minFreq += 1


if __name__ == '__main__':
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))  # 返回 1
    lfu.put(3, 3)
    print(lfu.get(2))  # 返回 -1
    print(lfu.get(3))  # 返回 3
    lfu.put(4, 4)
    print(lfu.get(1))  # 返回 -1
    print(lfu.get(3))  # 返回 3
    print(lfu.get(4))  # 返回 4
