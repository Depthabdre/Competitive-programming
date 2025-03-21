# Problem: Christmas Spruce - https://codeforces.com/contest/913/problem/B



n = int(input()) - 1
arr = [0]
count = {}
for _ in range(n):
    temp = int(input())
    arr.append(temp)


for i in range(n   , 0 , -1):
    if i not  in count:
        count[arr[i] - 1] = count.get(arr[i] - 1, 0) + 1
    elif i  in count:
        count[arr[i] - 1] = count.get(arr[i] - 1 , 0)


for key in count:
    if count[key] < 3:
        print("No")
        break
else:
    print("Yes")
    
        