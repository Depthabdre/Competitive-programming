# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque
len_nums , k = map(int,input().split())

nums = list(map(int,input().split()))
start = 0
total = 0
incque = deque()
decque = deque()

for i in range(len_nums):
    
    while incque and incque[-1] > nums[i]:
        incque.pop()
    while decque and decque[-1] < nums[i]:
        decque.pop()
    incque.append(nums[i])
    decque.append(nums[i])
    if (decque[0] - incque[0]) > k:
        temp = ((i-start)*(i-start+1)) // 2
        
        while decque and incque and (decque[0] - incque[0]) > k:
            if nums[start] == decque[0]:
                decque.popleft()
            if nums[start] == incque[0]:
                incque.popleft()
            start += 1
        total += (temp - (((i-start)*(i-start+1)) // 2))
total += ((len_nums -start)*(len_nums -start+1)) // 2

print(total)
    