# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

nTest = int(input())
for _ in range(nTest):
    x = int(input())
    if x & 1 == 1:
        x >>= 1
        while x > 0 and x & 1 != 1:
            x >>= 1
        if x > 0:
            print(1)
        else:
            print(3)
    else:
        i = 1
        x >>= 1
        while x > 0 and x & 1 != 1:
            x >>= 1
            i += 1
        j = i
        x >>= 1
        while x > 0 and x & 1 != 1:
            x >>= 1
            i += 1
        if x > 0:
            print((1<<j))
        else:
            print((1<<j) + 1)
