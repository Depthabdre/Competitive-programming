# Problem: Divisibility by 2^n - https://codeforces.com/contest/1744/problem/D

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
def count_factor_two(n: int) -> int:
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    return count



def solve():
    n = number()
    nums = numbers()
    count = 0
    indexCount = []
    for i in range(n):
        count += count_factor_two(nums[i])
        if count_factor_two(i + 1) != 0:
            indexCount.append(count_factor_two(i + 1))
    indexCount.sort(reverse=True)
    if count >= n:
        print(0)
    else:
        for i in range(len(indexCount)):
            count += indexCount[i]
            if count >= n:
                print(i + 1)
                return
        print(-1)
    
    
    
    return


for _ in range(test_cases()):
    solve()
