# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True for i in range(n)]
        primes[0] = primes[1] = False
        count = 0
        i = 2
        while i * i < n:
            if primes[i]:
                temp = i * i
                while temp < n:
                    primes[temp] = False
                    temp += i
            i += 1
        return sum(primes) 
        