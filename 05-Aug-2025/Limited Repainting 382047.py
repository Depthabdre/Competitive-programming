# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

from sys import stdin
import sys
input = stdin.readline

def number(): return int(input().strip())
def numbers(): return list(map(int, input().strip().split()))
def word(): return input().strip()
def test_cases(): return number()

def solve():
    n, k = map(int, input().split())
    s = word()            # target colors ('R' or 'B')
    a = numbers()         # penalties

    left = 0
    right = max(a)        # Max possible penalty
    answer = right        # To store the minimum achievable penalty

    def can_cover_with_k_operations(max_penalty):
        count_segments = 0
        i = 0
        while i < n:
            # Start a new segment only if this blue cell has too high a penalty
            if s[i] == 'B' and a[i] > max_penalty:
                count_segments += 1
                j = i
                while j < n and (a[j] <= max_penalty or (s[j] == 'B' and a[j] > max_penalty)):
                    j += 1
                i = j  
            else:
                i += 1
        return count_segments <= k

    while left <= right:
        mid = (left + right) // 2
        if can_cover_with_k_operations(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)



for _ in range(test_cases()):
    solve()
