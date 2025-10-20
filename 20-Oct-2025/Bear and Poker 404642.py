# Problem: Bear and Poker - https://codeforces.com/problemset/problem/574/C

from math import isqrt
import sys

# Fast input helpers
number = lambda: int(sys.stdin.readline().strip())
numbers = lambda: list(map(int, sys.stdin.readline().strip().split()))
test_cases = lambda inp=0: number() if not inp else inp


def reduce_num(num: int) -> int:
    """Remove all factors of 2 and 3 and return the remaining core number."""
    while num % 2 == 0:
        num //= 2
    while num % 3 == 0:
        num //= 3
    return num


def solve():
    n = number()
    nums = numbers()

    
    reduced = [reduce_num(x) for x in nums]

    
    if len(set(reduced)) == 1:
        print("Yes")
    else:
        print("No")


# Run test cases
for _ in range(test_cases(1)):
    solve()
