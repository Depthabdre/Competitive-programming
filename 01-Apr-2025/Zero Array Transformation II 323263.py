# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        def canMakeZero(k):
            decrement = [0] * (n + 1)
            
            for i in range(k):
                l, r, val = queries[i]
                decrement[l] += val
                if r + 1 < n:
                    decrement[r + 1] -= val
            
            current_decrement = 0
            for i in range(n):
                current_decrement += decrement[i]
                if nums[i] - current_decrement > 0:
                    return False
            
            return True
        
        left, right = 0, len(queries)
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if canMakeZero(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
