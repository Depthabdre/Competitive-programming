# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/

# Trie
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.lisIndex = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str , wordIndex ) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
            curr.lisIndex.append(wordIndex)
        curr.isEnd = True
        
    def search(self, word: str , trieNode) -> bool:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.isEnd
        
    def startsWith(self, prefix: str):
        curr = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                return []
            curr = curr.children[index]
        return curr.lisIndex


class WordFilter:

    def __init__(self, words: List[str]):
        self.root = Trie()
        self.revRoot = Trie()
        curr = self.root
        revCurr = self.revRoot
        for i in range(len(words)):
            curr.insert(words[i] , i)
            revCurr.insert(words[i][::-1] , i)
    def f(self, pref: str, suff: str) -> int:
        list_index_pre = self.root.startsWith(pref)
        list_index_suff = self.revRoot.startsWith(suff[::-1])
        list_index_pre.sort()
        list_index_suff.sort()
        i = len(list_index_pre) - 1
        j = len(list_index_suff) - 1
        largest_common = -1

        while i >= 0 and j >= 0:
            if list_index_pre[i] == list_index_suff[j]:
                largest_common = list_index_pre[i]
                break  
            elif list_index_pre[i] > list_index_suff[j]:
                i -= 1
            else:
                j -= 1

        return largest_common



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)