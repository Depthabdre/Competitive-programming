# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEnd = True

    def search(self, word: str) -> bool:
        nodes = [self.root]
        for letter in word:
            new_nodes = []
            for node in nodes:
                if letter == ".":
                    for child in node.children:
                        if child:
                            new_nodes.append(child)
                else:
                    index = ord(letter) - ord('a')
                    if node.children[index]:
                        new_nodes.append(node.children[index])
            if not new_nodes:
                return False
            nodes = new_nodes
        return any(node.isEnd for node in nodes)
