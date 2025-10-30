# Problem: Number of Ways to Reach a Position After Exactly k Steps - https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = endPos - startPos
        numPositive= (k + diff ) / 2
        absDiff = abs(endPos - startPos)
        print(f"positive is {numPositive}")
        if (numPositive  != int(numPositive)) or (absDiff > k):
            return 0
        else:
            numPositive = int(numPositive)
            numNegative = k - numPositive
            print(f"num neg is {numNegative}")
        
            MOD = 10**9 + 7

            answer = 1
            for i in range(k, 0, -1):
                answer = (answer * i) % MOD

            temp = 1
            for i in range(numNegative, 0, -1):
                temp = (temp * i) % MOD

            for i in range(numPositive, 0, -1):
                temp = (temp * i) % MOD  
    
            result = (answer * pow(temp, MOD-2, MOD)) % MOD

            return result



