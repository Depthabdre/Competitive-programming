# Problem: Number of Parallelograms - https://codeforces.com/contest/660/problem/D

from collections import defaultdict
import sys
input = sys.stdin.readline

number = lambda: int(input())
numbers = lambda: list(map(int, input().split()))
test_cases = lambda inp=0: number() if not inp else inp

def solve():
    n = number()
    points = [tuple(numbers()) for _ in range(n)]

    mid_point_count = defaultdict(int)

    for i in range(n):
        for j in range(i + 1, n):
            cx = points[i][0] + points[j][0]
            cy = points[i][1] + points[j][1]
            
            mid_point_count[(cx, cy)] += 1

    ans = 0
    for cnt in mid_point_count.values():
        ans += cnt * (cnt - 1) // 2

    print(ans)

for _ in range(test_cases(1)):
    solve()
