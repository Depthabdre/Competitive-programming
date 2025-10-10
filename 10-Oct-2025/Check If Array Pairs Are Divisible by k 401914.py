# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
        count = Counter([ x % k for x in arr])

        for i in range(k):
            if i == 0:
                if count[i] % 2 != 0:
                    return False
            else:
                if count[i] != count[k - i]:
                    return False
        return True



        