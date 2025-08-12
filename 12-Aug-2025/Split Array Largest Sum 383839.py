# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = 0
        right = sum(nums)
        final_answer = right

        def checker(max_sum):
            split_remains = k - 1
            curr = 0
            possible_max_sum = 0
            for i in range(len(nums)):
                if curr + nums[i] > (max_sum) and split_remains > 0:
                    split_remains -= 1
                    curr = nums[i]
                elif curr + nums[i] <= (max_sum):
                    curr += nums[i]
                elif curr + nums[i] > (max_sum) and split_remains <= 0:
                    return -1
                possible_max_sum = max(possible_max_sum , curr)
           
            return possible_max_sum

        while left <= right:
            mid = (left + right) // 2
            ans = checker(mid)
            if ans != -1:
                right = mid - 1
                final_answer = min(final_answer , ans)
            else:
                left = mid + 1
               
        return final_answer
        