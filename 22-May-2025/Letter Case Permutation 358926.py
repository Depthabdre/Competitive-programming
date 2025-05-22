# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def toggle_char(c):
            if c.isupper():
                return c.lower()
            elif c.islower():
                return c.upper()
            else:
                return c  # return as-is if it's not a letter
        letter_count = sum(1 for c in s if c.isalpha())
        letter_count = 2 ** letter_count
        ans = []
        for i in range(letter_count):
            temp = []
            for char in s:
                if char.isalpha()  :
                    if  i & 1:
                        newcar = toggle_char(char)
                        temp.append(newcar)
                    else:
                        temp.append(char)

                    i >>= 1
                else:
                    temp.append(char)
            ans.append("".join(temp))
        
        return ans
                


        