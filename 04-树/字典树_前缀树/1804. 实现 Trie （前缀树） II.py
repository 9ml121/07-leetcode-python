"""
前缀树（trie ，发音为 "try"）是一个树状的数据结构，用于高效地存储和检索一系列字符串的前缀。前缀树有许多应用，如自动补全和拼写检查。

实现前缀树 Trie 类：

Trie() 初始化前缀树对象。
void insert(String word) 将字符串 word 插入前缀树中。
int countWordsEqualTo(String word) 返回前缀树中字符串 word 的实例个数。
int countWordsStartingWith(String prefix) 返回前缀树中以 prefix 为前缀的字符串个数。
void erase(String word) 从前缀树中移除字符串 word 。


示例 1:

输入
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase",
"countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
输出
[null, null, null, 2, 2, null, 1, 1, null, 0]

解释
Trie trie = new Trie();
trie.insert("apple");               // 插入 "apple"。
trie.insert("apple");               // 插入另一个 "apple"。
trie.countWordsEqualTo("apple");    // 有两个 "apple" 实例，所以返回 2。
trie.countWordsStartingWith("app"); // "app" 是 "apple" 的前缀，所以返回 2。
trie.erase("apple");                // 移除一个 "apple"。
trie.countWordsEqualTo("apple");    // 现在只有一个 "apple" 实例，所以返回 1。
trie.countWordsStartingWith("app"); // 返回 1
trie.erase("apple");                // 移除 "apple"。现在前缀树是空的。
trie.countWordsStartingWith("app"); // 返回 0


提示：

1 <= word.length, prefix.length <= 2000
word 和 prefix 只包含小写英文字母。
insert、 countWordsEqualTo、 countWordsStartingWith 和 erase 总共调用最多 3 * 10^4 次。
保证每次调用 erase 时，字符串 word 总是存在于前缀树中。
"""
import collections


class Trie:

    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.count_word = 0
        self.count_prefix = 0

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            node = node.children[c]
            node.count_prefix += 1
        node.count_word += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count_word

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count_prefix

    def erase(self, word: str) -> None:
        if self.countWordsEqualTo(word) == 0:
            return

        node = self
        for c in word:
            node = node.children[c]
            node.count_prefix -= 1
        node.count_word -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)