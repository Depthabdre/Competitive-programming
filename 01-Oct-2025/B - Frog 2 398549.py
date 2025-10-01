# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

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
    n , k = numbers()
    nums = numbers()
    dp = [float('inf') for i in range(n + k)]
    for i in range(k):
        nums.append(nums[-1])
        dp[n + i] = 0
    for i in range(n - 1 , -1 , -1):
        for j in range(1 , k + 1):
            dp[i] = min (dp[i] , (dp[i+j] +  abs(nums[i] - nums[i+j])) ) 
    print(dp[0])
    
    return


for _ in range(test_cases(1)):
    solve()
