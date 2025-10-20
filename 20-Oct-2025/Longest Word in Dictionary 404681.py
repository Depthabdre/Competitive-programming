# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

# Trie
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
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
                return False
            curr = curr.children[index]
        return True

class Solution:
    def longestWord(self, words: List[str]) -> str:
        def smallest_lexicographical(s1, s2):
            return s1 if s1 < s2 else s2
        words.sort()
        ans = ""
        trieWord = Trie()
        for index , word in enumerate(words):
            if len(word) == 1:
                trieWord.insert(word)
                if len(ans) == 1:
                    ans = smallest_lexicographical(ans, word)
                elif len(ans) < len(word):
                        ans = word
                
            else:
                temp = word[0:len(word) -1]
                if trieWord.startsWith(temp):
                    trieWord.insert(word)
                    if len(ans) == len(word):
                        ans = smallest_lexicographical(ans, word)
                    elif len(ans) < len(word):
                        ans = word
        return ans

                


        return 
        