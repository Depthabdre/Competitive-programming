# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

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
    nums = numbers()
    nums.append(nums[-1])
    nums.append(nums[-1])
    dp = [float('inf') for i in range(n + 2)]
    dp[n] = 0
    dp[n + 1] = 0
    
    for i in range(n - 1 , -1 , -1):
        dp[i] = min ((dp[i+1] +  abs(nums[i] - nums[i+1])) , (dp[i+2] +  abs(nums[i] - nums[i+2])) )
    print(dp[0])
    
    return


for _ in range(test_cases(1)):
    solve()
