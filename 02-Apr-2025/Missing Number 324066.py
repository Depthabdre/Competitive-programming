# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        len_nums = len(nums)
        for i in range(len_nums ):
            if nums[i] != i:
                return i
        return len_nums