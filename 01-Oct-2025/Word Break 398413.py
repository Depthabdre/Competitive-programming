# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(curr_idx , curr_word):

            if curr_idx >= len(s) and  curr_word in wordDict:
                return True
            elif curr_idx >= len(s):
                return False
                
            take , notake = False , False

            if (curr_idx , curr_word) in memo:
                return  memo[(curr_idx , curr_word)]

            if curr_word in wordDict:
                take = dp(curr_idx + 1 , s[curr_idx]) 
                notake = dp(curr_idx + 1 , curr_word + s[curr_idx])
            else:
                notake = dp(curr_idx + 1 , curr_word + s[curr_idx])

            memo[(curr_idx , curr_word)] = take or  notake

            return  memo[(curr_idx , curr_word)]
        
        return dp(0 , "")

        