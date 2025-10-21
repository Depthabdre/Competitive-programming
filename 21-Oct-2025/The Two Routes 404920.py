# Problem: The Two Routes - https://codeforces.com/problemset/problem/601/A

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
    graph = defaultdict(set)
    n , e = numbers()
 
    for i in range(e):
        a , b = numbers()
        graph[a].add(b)
        graph[b].add(a)
   
    if n in graph[1]:
        roadGraph = defaultdict(set)
        for i in range(1 , n + 1):
            for j in range(1 , n + 1):
                if j not in graph[i] and j != i:
                    roadGraph[i].add(j)
        visited = set()
        queue = deque([1])
        visited.add(1)
        distance = 1
       
        while queue:
            leng = len(queue)
            
            for i in range(leng):
                curr = queue.popleft()
                
                for edge in roadGraph[curr]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append(edge)
                    if edge == n:
                         print( distance)
                         return
            distance += 1
        print(-1)
    else:
        visited = set()
        queue = deque([1])
        visited.add(1)
        distance = 1
        while queue:
            leng = len(queue)
          
            for i in range(leng):
                curr = queue.popleft()
                
                for edge in graph[curr]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append(edge)
                    if edge == n:
                        print( distance)
                        return
            distance += 1
        print(-1)
        
    
    return


for _ in range(test_cases(1)):
    solve()
