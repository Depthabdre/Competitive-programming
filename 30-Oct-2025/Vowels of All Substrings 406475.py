# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        
        vowel = ['a' , 'e' , 'i' , 'o' , 'u']
        n = len(word)
        result = 0
        for index , char in enumerate(word):
            if char in vowel:
                temp = (index + 1) * (n-index)
                result += temp
        return result
