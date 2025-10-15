# Problem: Row GCD - https://codeforces.com/problemset/problem/1458/a

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
    numsA = numbers()
    numsB = numbers()
    numsA.sort(reverse=True)
    gcdA = 0
    for i in range(n-1):
        gcdA = gcd(gcdA , numsA[i] - numsA[i+1])
    ans = []
    for i in range(m):
        ans.append(gcd((numsB[i] + numsA[0]) , gcdA))
    print(*ans)
    
    return


for _ in range(test_cases(1)):
    solve()
