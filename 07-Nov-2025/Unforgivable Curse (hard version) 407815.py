# Problem: Unforgivable Curse (hard version) - https://codeforces.com/contest/1800/problem/E2

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
class uf:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return self.par[node]
    
    def union(self, u, v):
        par_u = self.find(u)
        par_v = self.find(v)

        if par_u == par_v:
            return False
        if self.size[par_u] < self.size[par_v]:
            par_u, par_v = par_v, par_u
        
        self.par[par_v] = par_u
        self.size[par_u] += self.size[par_v]
        return True
    
    def checker(self, u, v):
        return self.find(u) == self.find(v)



def solve():
    n , k = numbers()
    str1 = list(input())
    str2 = list(input())
    unifind = uf(n)
    
    for i in range(n):
        if i + k < n:
            unifind.union(i, i+k)
        if i + k + 1 < n:
            unifind.union(i, i+k+1)

    
    groups = defaultdict(list)
    for i in range(n):
        parent = unifind.find(i)
        groups[parent].append(i)
    for indices in groups.values():
        s_letters = sorted([str1[i] for i in indices])
        t_letters = sorted([str2[i] for i in indices])
        if s_letters != t_letters:
            print("NO")
            return 
    print("YES")


    
            
        
        
    
    return


for _ in range(test_cases()):
    solve()
