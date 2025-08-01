# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.result = None  # store the smallest valid number

        def backtrack(path, used):
            if len(path) == len(pattern) + 1:
                number = ''.join(map(str, path))
                if self.result is None or number < self.result:
                    self.result = number
                return

            for digit in range(1, 10):
                if digit in used:
                    continue

                if len(path) > 0:
                    prev = path[-1]
                    idx = len(path) - 1
                    if pattern[idx] == 'I' and not (prev < digit):
                        continue
                    if pattern[idx] == 'D' and not (prev > digit):
                        continue

                path.append(digit)
                used.add(digit)
                backtrack(path, used)
                path.pop()
                used.remove(digit)

        backtrack([], set())
        return self.result
