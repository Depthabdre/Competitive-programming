# Problem: Dreamoon and Stairs - https://codeforces.com/problemset/problem/476/A

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
    n , m = numbers()
    mid = ceil(n / 2)
    
    for i in range(mid , n + 1):
        if i % m == 0:
            print(i)
            return 
    print(-1)
    
    return


for _ in range(test_cases(1)):
    solve()
