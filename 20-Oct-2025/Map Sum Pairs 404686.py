# Problem: Map Sum Pairs - https://leetcode.com/problems/map-sum-pairs/description/

# Trie
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str , val) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.count += val
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                return 0
            curr = curr.children[index]
        return curr.count

class MapSum:

    def __init__(self):
        self.TrieNode = Trie()
        self.keyValue = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        
        if self.TrieNode.search(key):
            self.TrieNode.insert(key , val - self.keyValue[key])
        else:
            self.TrieNode.insert(key , val)
        self.keyValue[key] = val

    def sum(self, prefix: str) -> int:

        return self.TrieNode.startsWith(prefix)

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)