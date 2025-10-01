# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        unit_stone = {}
        memo = {}
        last_unit = stones[-1]

        for i in range(len(stones)):
            unit_stone[stones[i]] = i + 1

        def dp(curr_unit , curr_jump):
            if curr_unit == last_unit:
                return True
            if curr_unit > last_unit:
                return False
            if (curr_unit , curr_jump) in memo:
                return memo[(curr_unit , curr_jump)]
            if not (curr_unit in unit_stone):
                return False
            ans = False
            temp_ans = False
            for i in range(-1 , 2):
                if curr_jump + i > 0 and (curr_unit + curr_jump + i) in unit_stone:
                    temp_ans = dp(curr_unit + curr_jump + i, curr_jump + i)
                ans = ans or temp_ans
            memo[(curr_unit , curr_jump)] = ans
            return ans
        return dp(0 , 0)




        