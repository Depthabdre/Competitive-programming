# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 1

        start_window = 0 
        max_len = 1

        for i in range(1,len(nums)):
            temp = i - 1
            while temp >= start_window and nums[temp] & nums[i] == 0:
                print(nums[temp] , nums[i])
                print(nums[temp] & nums[i])
                temp -= 1
            start_window = temp + 1
            max_len = max(max_len , i - start_window + 1)
        return max_len
        