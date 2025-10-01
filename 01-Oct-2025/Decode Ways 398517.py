# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def dp(index , hold):
            if hold == '0':
                return 0
            if index >= len(s):
                return 1
            if s[index] == '0' and (not hold):
                return 0
            if (index , hold) in memo:
                return memo[(index , hold)]
            
            ans = 0
            if len(hold) == 2:
                ans = dp(index + 1 , s[index])
            if hold:
                temp = int(hold) * 10 + int(s[index])
                if temp <= 26:
                    take = dp(index + 1 , str(temp))
                    notake = dp(index + 1 , s[index])
                    ans = take + notake
                else:
                    ans = dp(index + 1 , s[index])
            else:
                ans = dp(index + 1 , s[index])
            memo[(index , hold)] = ans

            return memo[(index , hold)]

        return dp(0 , "")
        