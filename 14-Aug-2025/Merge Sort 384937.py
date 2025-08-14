# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

from math import ceil

len_arr , max_call = map(int,input().split())

arr = []
calls = 0
for i in range(len_arr):
    arr.append(i+1)

def recursive(left , right):
    global max_call
    global arr
    if  right - left <= 1 :
        return
    if max_call == 0:
        return 
    if max_call < 0:
        return 
    mid = (left + right)  // 2 
    arr[mid-1] , arr[mid ] = arr[mid ] , arr[mid - 1 ]
    max_call -= 2
    recursive(left,mid)
    recursive(mid,right)
        
first_part = len_arr // 2
second_part = ceil(len_arr / 2)
max_moves = (2 ** first_part - 1) + (2 ** second_part - 1) + 1
if max_call % 2 == 0 or max_call > max_moves:
    print(-1)
else:
    max_call -= 1
    recursive(0 , len_arr)
    if max_call <= 0:
        print(" ".join(map(str,arr)))
    else:
        print(-1)
        
            
            
            
            