# Problem: D - Knapsack 1 - https://atcoder.jp/contests/dp/tasks/dp_d

# Abdre
from math import ceil, sqrt, log, log2, pow, floor, gcd, inf, isqrt, lcm
import sys, math, heapq as heap, itertools
from collections import defaultdict, Counter, deque
from bisect import bisect_right, bisect_left
from random import randint

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc



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
    n, w = numbers()
    nums = [numbers() for _ in range(n)]

    if n == 0:
        print(0)
        return

    dp = [0 for i in range(w+1)]
    
    
    for inwt , val in nums:
        for upwt in range(w  , -1 , -1):
            if upwt - inwt >= 0:
                dp[upwt] = max(dp[upwt - inwt] + val , dp[upwt])
        
    print(dp[w])
    
    return 
            





for _ in range(test_cases(1)):
    solve()
