# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.count = 0

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
            curr.count += 1
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
        count = 0
        for letter in prefix:
            index = ord(letter) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
            count += curr.count
        return count 

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trieNode = Trie()
        for word in words:
            trieNode.insert(word)
        ans = []

        for word in words:
            runing_str = ""
            temp_ans = trieNode.startsWith(word)
            ans.append(temp_ans)
        return ans

        