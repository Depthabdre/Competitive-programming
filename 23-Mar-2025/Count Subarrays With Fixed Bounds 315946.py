# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        min_position = -1
        max_position = -1
        left = 0
        
        for right in range(len(nums)):
            if nums[right] < minK or nums[right] > maxK:
                left = right + 1
                min_position = -1
                max_position = -1
            if nums[right] == minK:
                min_position = right
            if nums[right] == maxK:
                max_position = right
            
            if min_position != -1 and max_position != -1:
                count += max(0, min(min_position, max_position) - left + 1)
        
        return count
