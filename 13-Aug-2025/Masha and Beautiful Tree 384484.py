# Problem: Masha and Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

# Abdre
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
    len_permutation = number()
    permutations = numbers()
    min_number_of_operation = 0
    
    @bootstrap
    def divide_and_conquer(left_index, right_index):
        nonlocal min_number_of_operation
        nonlocal permutations

        if left_index == right_index:               # base case → return
            yield [permutations[left_index]]
            return


        # divide
        mid = (left_index + right_index) // 2
        left_part  = yield divide_and_conquer(left_index,  mid)      # recursive call → yield
        right_part = yield divide_and_conquer(mid + 1, right_index)  # recursive call → yield

        # conquer
        if not left_part or not right_part:        # impossible to sort
            
            yield []
            return 

        if left_part[0] - right_part[-1] == 1:
            # need one swap
            min_number_of_operation += 1
            right_part.extend(left_part)
            yield right_part
            return 

        elif right_part[0] - left_part[-1] == 1:
            # already in order
            left_part.extend(right_part)
            yield left_part
            return 

        else:
            # missing middle natural number → impossible
            yield []
            return 

    
    answer = divide_and_conquer(0 , len_permutation - 1)
    if answer:
        print(min_number_of_operation)
    else:
        print(-1)
        
    return


for _ in range(test_cases()):
    solve()
