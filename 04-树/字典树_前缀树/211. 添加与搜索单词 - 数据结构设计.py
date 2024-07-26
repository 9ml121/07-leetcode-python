"""
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 WordDictionary ：
WordDictionary() 初始化词典对象
void addWord(word) 将 word 添加到数据结构中，之后可以对它进行匹配
bool search(word) 如果数据结构中存在字符串与 word 匹配，则返回 true ；否则，返回  false 。
word 中可能包含一些 '.' ，每个 . 都可以表示任何一个字母。


示例：

输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // 返回 False
wordDictionary.search("bad"); // 返回 True
wordDictionary.search(".ad"); // 返回 True
wordDictionary.search("b.."); // 返回 True


提示：
1 <= word.length <= 25
addWord 中的 word 由小写英文字母组成
search 中的 word 由 '.' 或小写英文字母组成
最多调用 10^4 次 addWord 和 search
"""


class Trie:
    def __init__(self) -> None:
        self.children = [None] * 26  # trie数组
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        node = self.root
        for i, c in enumerate(word):
            idx = ord(c) - ord('a')

            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.isWord = True

    def search(self, word: str) -> bool:
        def dfs(node: Trie, i: int) -> bool:
            if i == len(word):
                return node.isWord
            if word[i] == '.':
                #  如果当前字符是点号，由于点号可以表示任何字母，因此需要对当前结点的所有非空子结点继续搜索下一个字符。
                for child in node.children:
                    if child is not None and dfs(child, i + 1):
                        return True
            else:
                # 如果当前字符是字母，则判断当前字符对应的子结点是否存在，如果子结点存在则移动到子结点，继续搜索下一个字符，
                # 如果子结点不存在则说明单词不存在，返回 false
                idx = ord(word[i]) - ord('a')
                child = node.children[idx]
                if child is not None and dfs(child, i + 1):
                    return True

            return False

        return dfs(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
