# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

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
    n , num_ege , num_gov = numbers()
    gov_nodes = numbers()
    edges = []
    for i in range(num_ege):
        j , k = numbers()
        edges.append([j,k])
    uni_find = uf(n)
    par_gove = {}
    for i , j in edges:
        uni_find.union(i , j)
    for node in gov_nodes:
        pars = uni_find.find(node)
        par_gove[pars] = pars
    free_count = 0
    max_child = 0
    num_ege_non_gov = {}
    total = 0
    for i in range(1 , n + 1):
        par = uni_find.find(i)
        if not par in par_gove:
            free_count += 1
        else:
            max_child = max(max_child , uni_find.size[par])
            
        if not par in num_ege_non_gov and  par in par_gove:
            num_child = uni_find.size[par]
            total += (num_child)*(num_child - 1) // 2
            num_ege_non_gov[par] = 1
            
    total += (free_count)*(free_count-1) // 2
    total += (free_count * max_child)
    total -= num_ege
    print(total)
    
        
   
            
    
    return


for _ in range(test_cases(1)):
    solve()
