# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

len_arr1 = int(input())
arr1 = list(map(int, input().split()))
len_arr2 = int(input())
arr2 = list(map(int, input().split()))

i, j, count = 0, 0, 0

if sum(arr1) != sum(arr2): 
    print(-1)
else:
    sum1, sum2 = arr1[0], arr2[0]

    while i < len_arr1 and j < len_arr2:
        if sum1 == sum2:
            i += 1
            j += 1
            if i < len_arr1 and j < len_arr2:  
                sum1, sum2 = arr1[i], arr2[j]
        elif sum1 < sum2:
            i += 1
            if i < len_arr1:  
                sum1 += arr1[i]
            count += 1
        else:
            j += 1
            if j < len_arr2:  
                sum2 += arr2[j]

    print(len_arr1 - count)
