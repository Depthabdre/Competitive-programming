# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solve(nums,fl):
            if not nums: return 0
            if fl:
                return max((nums[0] - solve(nums[1:],False)),(nums[-1] - solve(nums[:len(nums)-1],False)))
            else:
                return max((nums[0] - solve(nums[1:],True)),(nums[-1] - solve(nums[:len(nums)-1],True)))
        op = solve(nums,True)
        return  op>=0 
        