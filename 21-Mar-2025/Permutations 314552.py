# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        possib = [False] * len(nums)
        path = []
        ans = []

        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if possib[i] == True:
                    continue
                path.append(nums[i])
                possib[i] = True
                backtrack()
                path.pop()
                possib[i] = False

        backtrack()
        return ans
            

        