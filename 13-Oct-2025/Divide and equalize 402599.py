# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

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
def trial_division_simple(n: int) -> list[int]:
    factorization: list[int] = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
    if n > 1:
        factorization.append(n)
    return factorization


def solve():
    n = number()
    nums = numbers()
    count = defaultdict(int)
    for num in nums:
        fact = trial_division_simple(num)
        for nm in fact:
            count[nm] += 1
    for key in count:
        if count[key]/ n != int(count[key]/ n):
            print("NO")
            return
    print("YES")
    
    
    return


for _ in range(test_cases()):
    solve()
