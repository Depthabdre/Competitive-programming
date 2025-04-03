# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        freq_char = Counter(nums)
        for key in freq_char:
            if freq_char[key] > 1:
                ans.append(key)
        return ans
        