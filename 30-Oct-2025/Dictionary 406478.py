# Problem: Dictionary - https://codeforces.com/problemset/problem/1674/B

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
    letter = word()
    count = (ord(letter[0]) - ord('a')) * 25
    if ord(letter[0]) > ord(letter[1]):
        count2 = ord(letter[1]) - ord('a') + 1
    else:
        count2 = ord(letter[1]) - ord('a') 
    print(count + count2)
        
    
    return


for _ in range(test_cases()):
    solve()
