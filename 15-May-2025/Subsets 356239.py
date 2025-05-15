# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total = 1 << n         
        res = []

        for mask in range(total):           
            subset = []
            for j in range(n):              
                if (mask >> j) & 1:        
                    subset.append(nums[j])  
            res.append(subset)

        return res
