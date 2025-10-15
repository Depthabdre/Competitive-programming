# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trieNode = Trie()

        for word in dictionary:
            trieNode.insert(word)
        ans = []
        sent_words = sentence.split()

        for word in sent_words:
            curr_str = ""
            for char in word:
                curr_str += char
                if trieNode.search(curr_str):
                    ans.append(curr_str)
                    break
            else:
                ans.append(word)

        result_sentence = " ".join(ans)
        return result_sentence

        



        