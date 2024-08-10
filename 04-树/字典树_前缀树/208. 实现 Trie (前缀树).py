"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word)
    向前缀树中插入字符串 word 。

boolean search(String word)
    如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。

boolean startsWith(String prefix)
    如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


示例：
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True


提示：
1 <= word.length, prefix.length <= 2000
word 和 prefix 仅由小写英文字母组成
insert、search 和 startsWith 调用次数 总计 不超过 3 * 104 次
"""

import collections


# 实现方法 1：利用字典存储多叉树的孩子节点
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False


class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for w in word:
            curr = curr.children[w]
        curr.isword = True

    def search(self, word: str) -> bool:
        curr = self.root
        for w in word:
            curr = curr.children.get(w)
            if not curr:
                return False
        return curr.isword

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for w in prefix:
            curr = curr.children.get(w)
            if not curr:
                return False
        return True


# 实现方法 2：利用数组存储多叉树的孩子节点
class Trie:
    def __init__(self):
        self.children = [None] * 26  # 该节点的所有子节点。
        self.isEnd = False  # 表示从根节点到当前节点为止，该路径是否形成了一个有效的字符串。

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self
        for c in word:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]

        return node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
