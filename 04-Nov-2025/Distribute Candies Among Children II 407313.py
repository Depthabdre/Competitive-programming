# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for x in range(min(limit, n) + 1):
            remaining = n - x
            if remaining > 2 * limit:
                continue
            low = max(0, remaining - limit)
            high = min(limit, remaining)
            ans += high - low + 1
        return ans
