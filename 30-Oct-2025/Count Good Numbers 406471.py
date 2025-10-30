# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def binary_exponentiation(base, exponent):
            result = 1
            MOD = 10**9 + 7
            while exponent > 0:
                if exponent & 1:
                    result = (result * base) % MOD
                base = (base * base) % MOD  
                exponent >>= 1
            return result
        if n % 2 == 0:
            expo5 = n // 2 
            expo4 = n // 2
        else:
            expo5 = ceil(n / 2)
            expo4 = n // 2
        ans = binary_exponentiation(4 , expo4) * binary_exponentiation(5 , expo5)
        ans %= (10**9 + 7)
        return ans
        