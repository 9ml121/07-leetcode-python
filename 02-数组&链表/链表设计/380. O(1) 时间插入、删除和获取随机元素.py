"""
实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int value) 当元素 value 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int value) 当元素 value 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。



示例：

输入
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出
[null, true, false, true, 2, true, false, 2]

解释
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。


提示：

-231 <= value <= 231 - 1
最多调用 insert、remove 和 getRandom 函数 2 * 105 次
在调用 getRandom 方法时，数据结构中 至少存在一个 元素。
"""
import random


class RandomizedSet2:
    """实现O(1)时间插入，删除和获取随机元素类
    第1版：用python set集合实现，不满足随机获取元素的时间要求
    """
    def __init__(self):
        self.hashSet = set()

    def insert(self, val: int) -> bool:
        if val not in self.hashSet:
            self.hashSet.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashSet:
            self.hashSet.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        if len(self.hashSet) > 0:
            # todo set转 list是 O(n)的时间复杂度
            return random.choice(list(self.hashSet))


class RandomizedSet:
    """实现O(1)时间插入，删除和获取随机元素类
    第2版：用python中哈希字典和列表实现
    """

    def __init__(self):
        self.val2idx = dict()
        self.arr = list()
        self.size = 0  # 数组长度

    def insert(self, val: int) -> bool:
        """数组从尾部添加元素，O(1)时间"""
        if val not in self.val2idx:
            self.arr.append(val)
            self.val2idx[val] = self.size
            self.size += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """数组从尾部删除元素，O(1)时间
        从字典获取待删除元素索引，然后将该索引下标值改为数组末尾元素，最后删除数组和字典末尾元素
        """
        if val in self.val2idx:
            idx = self.val2idx[val]
            lastVal = self.arr[-1]
            self.arr[idx] = lastVal
            self.val2idx[lastVal] = idx
            # 注意：一定要更新完数组和字典之后，在做删除操作
            self.arr.pop()
            self.size -= 1
            del self.val2idx[val]
            return True
        return False

    def getRandom(self) -> int:
        """从数组中查找随机元素是O(1)操作"""
        if self.size > 0:
            return random.choice(self.arr)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(value)
# param_2 = obj.remove(value)
# param_3 = obj.getRandom()
