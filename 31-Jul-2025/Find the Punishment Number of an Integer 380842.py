# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:

        def can_partition(s, target, index=0, current_sum=0):
            if index == len(s):
                return current_sum == target

            for end in range(index + 1, len(s) + 1):
                if s[index] == '0' and end > index + 1:
                    continue
                part = int(s[index:end])
                if can_partition(s, target, end, current_sum + part):
                    return True

            return False

        total = 0
        for i in range(1, n + 1):
            square_str = str(i * i)
            if can_partition(square_str, i):
                total += i * i

        return total
