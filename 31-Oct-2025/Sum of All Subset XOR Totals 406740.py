# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subset = []

        def backtrack(index, temp):
            if index == len(nums):
                subset.append(temp[:])
                return
           
            temp.append(nums[index])
            backtrack(index + 1, temp)
            temp.pop()
            backtrack(index + 1, temp)

        backtrack(0, [])
        result = 0
        for subs in subset:
            temp = 0
            for num in subs:
                temp ^= num
            result += temp
        return result




