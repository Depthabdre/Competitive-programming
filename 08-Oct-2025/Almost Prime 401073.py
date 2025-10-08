# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

# Abdre
from math import ceil, sqrt, log, log2, pow, floor, gcd, inf, isqrt, lcm
import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint


number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
yes_no = lambda condition: 'YES' if condition else 'NO'
test_cases = lambda inp=0: number() if not inp else inp
rand = randint(1, 10000)
xor = lambda x: x ^ rand
prefix_sum = lambda arr: list(itertools.accumulate(arr))



def solve():
    
    n = number()
    
    def isAlmostPrime(n , primes):   
        d = 2
        while d * d <= n:
            while n % d == 0:
                primes.add(d)
                n //= d
            d += 1
        if n > 1:
            primes.add(n)
        return (len(primes) == 2)
    total = 0
    for i in range(1 , n + 1):
        if isAlmostPrime(i , set()):
            total += 1
    print(total)
            
    
    return


for _ in range(test_cases(1)):
    solve()