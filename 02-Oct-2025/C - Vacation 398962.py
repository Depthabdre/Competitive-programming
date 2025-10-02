# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

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
    len_vacation = number()
    vacation = [numbers() for _ in range(len_vacation)]
    
    dp = [[0]*3 for _ in range(len_vacation+1)]
    
    
    for i in range(len_vacation-1, -1, -1):
        for j in range(3):  # today's choice
            for k in range(3):  # next day's choice
                if j == k:
                    continue
                dp[i][j] = max(dp[i][j], vacation[i][j] + dp[i+1][k])
    
    print(max(dp[0][0], dp[0][1], dp[0][2]))

    
    
    return


for _ in range(test_cases(1)):
    solve()
