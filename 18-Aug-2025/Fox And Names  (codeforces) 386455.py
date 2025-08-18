# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

# Abdre
from math import ceil, sqrt, log, log2, pow, floor, gcd, inf, isqrt, lcm
import string
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
    number_of_author = number()
    authors = []
    for i in range(number_of_author):
        author = word()
        authors.append(author)
    graph = defaultdict(list)
    incoming = {letter: 0 for letter in string.ascii_lowercase}
    is_poss = True
    for i in range(number_of_author - 1):
        j = 0
        is_same = True
       
        while len(authors[i]) > j and len(authors[i+1]) > j and is_same:
            if authors[i][j] == authors[i+1][j]:
                j += 1
                if len(authors[i+1]) <= j and len(authors[i]) > j:
                    is_poss= False
                continue
            else:
                graph[authors[i][j]].append(authors[i+1][j])
                incoming[authors[i+1][j]] += 1
                break
        if not is_poss: break
    queue = deque()
    for i in incoming:
        if incoming[i] == 0:
            queue.append(i)
    
    answer = []
    while queue:
        letter = queue.pop()
        answer.append(letter)
        
        for let in graph[letter]:
            incoming[let] -= 1
            if incoming[let] == 0:
                queue.append(let)
    if len(answer) < 26 or not is_poss:
        print("Impossible")
    else:
        print("".join(answer))
    
    return


for _ in range(test_cases(1)):
    solve()
