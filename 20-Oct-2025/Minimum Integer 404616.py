# Problem: Minimum Integer - https://codeforces.com/problemset/problem/1101/A

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
    num_query = number()
    queries = []
    for i in range(num_query):
        temp = numbers()
        queries.append(temp)
    for i in range(num_query):
        a , b , c = queries[i]
        num1 = a // c
        if num1 > 0 and a != c:
            print(c)
            
        else:
            num2 = ceil(b / c)
            if num2 == (b/c):
                print(c * (num2 + 1))
            else:   
                print(c * num2)
    
    return


for _ in range(test_cases(1)):
    solve()
