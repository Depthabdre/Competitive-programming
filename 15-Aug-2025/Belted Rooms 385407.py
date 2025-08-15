# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

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
  
    n = int(input())
    s = input().strip()

    # Case 1: all in one direction (+ possibly '-')
    if '<' not in s or '>' not in s:
        print(n)
        return

    # Case 2: mixed directions -> check belts around each room
    count = 0
    for i in range(n):
        left_belt = s[(i - 1 + n) % n]  # belt from (i-1) to i
        right_belt = s[i]               # belt from i to (i+1)
        if left_belt == '-' or right_belt == '-':
            count += 1

    print(count)
        
   
    
    return


for _ in range(test_cases()):
    solve()
