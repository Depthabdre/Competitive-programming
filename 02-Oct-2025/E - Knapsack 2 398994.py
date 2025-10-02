# Problem: E - Knapsack 2 - https://atcoder.jp/contests/dp/tasks/dp_e

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
    n , W = numbers()
    weights , values = [] , []
    for _ in range(n):
        wt , val = numbers()
        weights.append(wt)
        values.append(val)
    dp = [inf for i in range(sum(values) + 1)]
    dp[0] = 0
    for ind in range(n):
        dp2 = list(dp)
        for amt in range(values[ind] , sum(values) + 1):
        
            dp2[amt] = min(dp[amt - values[ind]] + weights[ind] , dp[amt])
            if dp2[amt] > W:
                dp2[amt] = inf
            
            
                
        dp = dp2
    
    ans = 0
    for i in range(1, len(dp)):
        if  dp[i] <= W:
            ans = i
    print(ans)
    





for _ in range(test_cases(1)):
    solve()
