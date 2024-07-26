"""
设计一个 map ，满足以下几点:

字符串表示键，整数表示值
返回具有前缀等于给定字符串的键的值的总和
实现一个 MapSum 类：

MapSum() 初始化 MapSum 对象
void insert(String key, int val) 插入 key-val 键值对，字符串表示键 key ，整数表示值 val 。如果键 key 已经存在，那么原来的键值对 key-value 将被替代成新的键值对。
int sum(string prefix) 返回所有以该前缀 prefix 开头的键 key 的值的总和。


示例 1：

输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);
mapSum.sum("ap");           // 返回 3 (apple = 3)
mapSum.insert("app", 2);
mapSum.sum("ap");           // 返回 5 (apple + app = 3 + 2 = 5)


提示：

1 <= key.length, prefix.length <= 50
key 和 prefix 仅由小写英文字母组成
1 <= val <= 1000
最多调用 50 次 insert 和 sum
"""
import collections


# 方法一：暴力扫描
class MapSum2:
    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key, val in self.map.items():
            if key.startswith(prefix):
                res += val
        return res


# 方法二：字典树
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.val = 0


class MapSum:
    def __init__(self):
        self.root = Trie()
        self.key_to_val = {}  # 存储已经插入的所有 key:val对象

    def insert(self, key: str, val: int) -> None:
        diff = val  # 要插入的 key每个前缀要增加的值
        if key in self.key_to_val:  # 如果key之前已经插入过
            diff -= self.key_to_val[key]

        self.key_to_val[key] = val

        node = self.root
        for c in key:
            node = node.children[c]
            node.val += diff

    def sum(self, prefix: str) -> int:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.val


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

if __name__ == '__main__':
    # ["MapSum", "insert", "sum", "insert", "insert", "sum"]
    # [[], ["apple", 3], ["ap"], ["app", 2], ["apple", 2], ["ap"]]
    # [null,null,3,null,null,4]

    # ["MapSum", "insert", "sum", "insert", "insert", "sum"]
    # [[], ["appled", 2], ["ap"], ["apple", 3], ["apple", 2], ["a"]]
    # [null, null, 2, null, null, 4]

    mapSum = MapSum()
    mapSum.insert("apple", 3);
    mapSum.sum("ap");  # 返回3(apple=3)
    mapSum.insert("app", 2);
    mapSum.sum("ap");  # 返回5(apple + app = 3 + 2 = 5)
