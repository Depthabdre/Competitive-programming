# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        total_one = bank[0].count('1')
        for i in range(1 , len(bank)):
            if bank[i].count('1') > 0:
                ans+= (total_one *bank[i].count('1'))
                total_one = bank[i].count('1')
        return ans
        