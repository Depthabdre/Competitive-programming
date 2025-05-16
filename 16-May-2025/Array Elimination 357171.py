# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

def gcd(a, b):
    if a > b: return gcd(b, a)
    if a == 0: return b
    return gcd(b % a, a)

nTest = int(input())
for _ in range(nTest):
    n = int(input())
    nums = list(map(int, input().split()))
    val = 0
    for _ in range(32):
        count = 0
        for i in range(n):
            count += nums[i] & 1
            nums[i] >>= 1
        
        val = gcd(val, count)
    
    ans = []
    if val == 0:
        for i in range(1, n + 1): 
            ans.append(i)
    else:
        for i in range(1, val + 1):
            if val % i == 0: 
                ans.append(i)
    print(*ans)
